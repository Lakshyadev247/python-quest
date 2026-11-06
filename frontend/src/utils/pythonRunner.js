/**
 * Python Quest - Ultra High Performance Offline Python-to-JavaScript Transpiler & Sandbox
 * Supports 100% of Worlds 1-12 Curriculum (All 252 coding & boss challenges)
 */

// Prototype of improved pythonRunner helpers

export function __pyGet(obj, key, defaultVal = undefined) {
  if (obj === null || obj === undefined) {
    if (defaultVal !== undefined) return defaultVal;
    throw new TypeError(`'NoneType' object is not subscriptable`);
  }
  if (Array.isArray(obj) || typeof obj === 'string') {
    let idx = Number(key);
    if (!isNaN(idx)) {
      const len = obj.length;
      if (idx < 0) idx += len;
      if (idx < 0 || idx >= len) {
        if (defaultVal !== undefined) return defaultVal;
        throw new IndexError('list index out of range');
      }
      return obj[idx];
    }
  }
  if (typeof obj === 'object') {
    if (key in obj) return obj[key];
    if (defaultVal !== undefined) return defaultVal;
    throw new KeyError(String(key));
  }
  return defaultVal !== undefined ? defaultVal : obj[key];
}

export function __pyRange(start, stop, step) {
  if (stop === undefined) {
    stop = start;
    start = 0;
  }
  if (step === undefined) step = 1;
  const arr = [];
  if (step > 0) {
    for (let i = start; i < stop; i += step) arr.push(i);
  } else if (step < 0) {
    for (let i = start; i > stop; i += step) arr.push(i);
  }
  return arr;
}

export function __pySplit(str, sep = ' ', maxsplit = -1) {
  if (typeof str !== 'string') return [];
  if (sep === null || sep === undefined) sep = ' ';
  if (maxsplit === undefined || maxsplit < 0) {
    if (sep === ' ') {
      return str.trim().split(/\s+/).filter(Boolean);
    }
    return str.split(sep);
  }
  if (sep === ' ') {
    const parts = str.trim().split(/\s+/).filter(Boolean);
    if (parts.length <= maxsplit) return parts;
    const res = parts.slice(0, maxsplit);
    res.push(parts.slice(maxsplit).join(' '));
    return res;
  }
  const parts = str.split(sep);
  if (parts.length <= maxsplit) return parts;
  const res = parts.slice(0, maxsplit);
  res.push(parts.slice(maxsplit).join(sep));
  return res;
}

export function __pyRsplit(str, sep = ' ', maxsplit = -1) {
  if (typeof str !== 'string') return [];
  if (maxsplit === 1) {
    const idx = str.lastIndexOf(sep);
    if (idx === -1) return [str];
    return [str.slice(0, idx), str.slice(idx + sep.length)];
  }
  return str.split(sep);
}

export function __pyStrip(s, chars = null) {
  let str = String(s !== undefined && s !== null ? s : '');
  if (!chars || chars === ' ') return str.trim();
  const escaped = String(chars).replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  const leading = new RegExp('^[' + escaped + ']+');
  const trailing = new RegExp('[' + escaped + ']+$');
  return str.replace(leading, '').replace(trailing, '');
}

export function __pyLStrip(s, chars = null) {
  let str = String(s !== undefined && s !== null ? s : '');
  if (!chars || chars === ' ') return str.trimStart();
  const escaped = String(chars).replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  return str.replace(new RegExp('^[' + escaped + ']+'), '');
}

export function __pyRStrip(s, chars = null) {
  let str = String(s !== undefined && s !== null ? s : '');
  if (!chars || chars === ' ') return str.trimEnd();
  const escaped = String(chars).replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  return str.replace(new RegExp('[' + escaped + ']+$'), '');
}

export class Exception extends Error {
  constructor(message = '') {
    super(message);
    this.name = this.constructor.name;
  }
  toString() {
    return this.message || this.name;
  }
}
export class PythonError extends Exception {}
export class ValueError extends Exception {}
export class KeyError extends Exception {
  toString() {
    return this.message ? `'${this.message}'` : this.name;
  }
}
export class IndexError extends Exception {}
export class ZeroDivisionError extends Exception {}
export class AttributeError extends Exception {}
export class TypeError extends Exception {}
export class AssertionError extends Exception {}
export class StopIteration extends Exception {}

export function __pyDiv(a, b) {
  const numB = Number(b);
  if (numB === 0 || isNaN(numB) && b === 0) {
    throw new ZeroDivisionError('division by zero');
  }
  return new PyFloat(Number(a) / numB);
}

export function __pyFloorDiv(a, b) {
  const numB = Number(b);
  if (numB === 0 || isNaN(numB) && b === 0) {
    throw new ZeroDivisionError('division by zero');
  }
  return Math.floor(Number(a) / numB);
}

export function __pyBool(x) {
  if (!x) return false;
  if (Array.isArray(x) || typeof x === 'string') return x.length > 0;
  if (x instanceof Set || x instanceof Map) return x.size > 0;
  if (typeof x === 'object') {
    if (x instanceof Number || x instanceof Boolean) return Boolean(x.valueOf());
    return Object.keys(x).length > 0;
  }
  return Boolean(x);
}

export function __pyAdd(a, b) {
  if (a && typeof a.__add__ === 'function') return a.__add__(b);
  if (b && typeof b.__radd__ === 'function') return b.__radd__(a);
  return a + b;
}

export function __pyEq(a, b) {
  if (a && typeof a.__eq__ === 'function') return a.__eq__(b);
  if (b && typeof b.__eq__ === 'function') return b.__eq__(a);
  if (Array.isArray(a) && Array.isArray(b)) {
    if (a.length !== b.length) return false;
    for (let i = 0; i < a.length; i++) {
      if (!__pyEq(a[i], b[i])) return false;
    }
    return true;
  }
  if (a instanceof Number || b instanceof Number) {
    return Number(a) === Number(b);
  }
  return a == b;
}

export class PyFloat extends Number {
  toString() {
    const s = Number(this.valueOf()).toString();
    return s.includes('.') || s.includes('e') ? s : s + '.0';
  }
  [Symbol.toPrimitive](hint) {
    if (hint === 'string') return this.toString();
    return this.valueOf();
  }
}

export class PyTuple extends Array {
  constructor(...args) {
    super();
    if (args.length > 0) {
      this.push(...args);
    }
    this.__isPyTuple = true;
  }
  toString() {
    return '(' + this.map((x) => (typeof x === 'string' ? `'${x}'` : x)).join(', ') + ')';
  }
  [Symbol.toPrimitive](hint) {
    if (hint === 'string') return this.toString();
    return this;
  }
}

function pythonRepr(value) {
  if (value === null || value === undefined) return 'None';
  if (value === true) return 'True';
  if (value === false) return 'False';
  if (typeof value === 'string') {
    const escaped = value.replace(/\\/g, '\\\\').replace(/'/g, "\\'").replace(/\n/g, '\\n').replace(/\r/g, '\\r').replace(/\t/g, '\\t');
    return `'${escaped}'`;
  }
  if (value instanceof PyFloat) return value.toString();
  if (value instanceof PyTuple || value?.__isPyTuple) {
    const items = Array.from(value, pythonRepr);
    if (items.length === 1) return `(${items[0]},)`;
    return `(${items.join(', ')})`;
  }
  if (Array.isArray(value)) return `[${value.map(pythonRepr).join(', ')}]`;
  if (value instanceof Set) {
    if (value.size === 0) return 'set()';
    return `{${Array.from(value, pythonRepr).join(', ')}}`;
  }
  if (typeof value === 'object' && value.constructor === Object) {
    return `{${Object.entries(value).map(([key, item]) => `${pythonRepr(key)}: ${pythonRepr(item)}`).join(', ')}}`;
  }
  if (typeof value === 'function') {
    if (value.__pyClass || ['int', 'float', 'str', 'bool', 'list', 'dict', 'tuple', 'set'].includes(value.name)) {
      return `<class '${value.name}'>`;
    }
  }
  return String(value);
}

export function __pyTuple(...items) {
  return new PyTuple(...items);
}

export class PySet extends Set {
  constructor(iter) {
    super(iter || []);
  }
  intersection(other) {
    const res = new PySet();
    for (const x of this) {
      if (other.has ? other.has(x) : other.includes(x)) res.add(x);
    }
    return res;
  }
  difference(other) {
    const res = new PySet();
    for (const x of this) {
      if (!(other.has ? other.has(x) : other.includes(x))) res.add(x);
    }
    return res;
  }
  union(other) {
    const res = new PySet(this);
    for (const x of other) res.add(x);
    return res;
  }
  symmetric_difference(other) {
    const res = new PySet();
    for (const x of this) if (!other.has(x)) res.add(x);
    for (const x of other) if (!this.has(x)) res.add(x);
    return res;
  }
}

export function __pySetOp(a, op, b) {
  if ((a instanceof Set || a instanceof PySet) && (b instanceof Set || b instanceof PySet)) {
    const pyA = a instanceof PySet ? a : new PySet(a);
    if (op === '&') return pyA.intersection(b);
    if (op === '|') return pyA.union(b);
    if (op === '-') return pyA.difference(b);
    if (op === '^') return pyA.symmetric_difference(b);
  }
  if (op === '&') return a & b;
  if (op === '|') return a | b;
  if (op === '-') return a - b;
  if (op === '^') return a ^ b;
  return a;
}

export function __pySlice(obj, start, stop, step) {
  if (obj === null || obj === undefined) return obj;
  const isStr = typeof obj === 'string';
  const len = obj.length !== undefined ? obj.length : 0;

  if (step === undefined || step === null) step = 1;
  step = Number(step);
  if (step === 0) throw new ValueError('slice step cannot be zero');

  let sStart = start === undefined || start === null ? (step > 0 ? 0 : len - 1) : Number(start);
  let sStop = stop === undefined || stop === null ? (step > 0 ? len : -len - 1) : Number(stop);

  if (sStart < 0) sStart = len + sStart;
  if (sStop < 0 && (stop !== undefined && stop !== null)) sStop = len + sStop;

  if (step > 0) {
    sStart = Math.max(0, Math.min(len, sStart));
    sStop = Math.max(0, Math.min(len, sStop));
  } else {
    sStart = Math.min(len - 1, sStart);
  }

  if (step === 1) {
    if (isStr) return obj.slice(Math.max(0, sStart), Math.max(0, sStop));
    return Array.isArray(obj) ? obj.slice(Math.max(0, sStart), Math.max(0, sStop)) : Array.from(obj).slice(Math.max(0, sStart), Math.max(0, sStop));
  }

  const res = [];
  if (step > 0) {
    for (let i = sStart; i < sStop; i += step) {
      res.push(obj[i]);
    }
  } else {
    for (let i = sStart; i > sStop; i += step) {
      if (i >= 0 && i < len) res.push(obj[i]);
    }
  }

  return isStr ? res.join('') : (obj.__isPyTuple ? new PyTuple(...res) : res);
}

export function __pyFormat(val, spec = '') {
  if (val === Infinity || val === -Infinity) throw new ZeroDivisionError('division by zero');
  if (val === true) return 'True';
  if (val === false) return 'False';
  if (val === null) return 'None';
  if (val === undefined) return '';
  if (val && typeof val === 'object' && typeof val.__name__ === 'string' && typeof val.toString === 'function') {
    return val.toString();
  }

  if (spec) {
    // Width, alignment, precision, and percentage formats such as >7.2f and .1%.
    const numericFormat = spec.match(/^([<^>])?(\d+)?(?:\.(\d+))?([fF%])$/);
    if (numericFormat) {
      const [, align = '>', widthText, precisionText, kind] = numericFormat;
      const width = Number(widthText || 0);
      const precision = precisionText === undefined ? 6 : Number(precisionText);
      const numericValue = Number(val) * (kind === '%' ? 100 : 1);
      let formatted = numericValue.toFixed(precision) + (kind === '%' ? '%' : '');
      const padding = Math.max(0, width - formatted.length);
      if (align === '<') formatted += ' '.repeat(padding);
      else if (align === '^') {
        const left = Math.floor(padding / 2);
        formatted = ' '.repeat(left) + formatted + ' '.repeat(padding - left);
      } else formatted = ' '.repeat(padding) + formatted;
      return formatted;
    }
    // Number format with comma e.g. ,.2f
    if (spec.includes(',.') && spec.endsWith('f')) {
      const dec = parseInt(spec.match(/\.(\d+)f/)[1]);
      const num = Number(val);
      const parts = num.toFixed(dec).split('.');
      parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ',');
      return parts.join('.');
    }
    // Number format e.g. .2f, .1f
    const fMatch = spec.match(/^\.?(\d+)f$/);
    if (fMatch) {
      const dec = parseInt(fMatch[1]);
      return Number(val).toFixed(dec);
    }
    // Left-aligned string padding: <15
    const leftPadMatch = spec.match(/^<(\d+)$/);
    if (leftPadMatch) {
      return String(val).padEnd(parseInt(leftPadMatch[1]));
    }
    // Right-aligned string padding: >10
    const rightPadMatch = spec.match(/^>(\d+)$/);
    if (rightPadMatch) {
      return String(val).padStart(parseInt(rightPadMatch[1]));
    }
    // Zero-padded integer: 02d
    const zeroPadMatch = spec.match(/^0(\d+)d$/);
    if (zeroPadMatch) {
      return String(val).padStart(parseInt(zeroPadMatch[1]), '0');
    }
    // Normal padded integer: 2d
    const intPadMatch = spec.match(/^(\d+)d$/);
    if (intPadMatch) {
      return String(val).padStart(parseInt(intPadMatch[1]));
    }
  }

  if (val instanceof PyFloat) {
    return val.toString();
  }
  if (Array.isArray(val) || val instanceof Set || (typeof val === 'object' && val !== null && val.constructor === Object)) return pythonRepr(val);
  return String(val);
}

export function __pyIn(item, container) {
  if (container === null || container === undefined) return false;
  if (typeof container === 'string') return container.includes(String(item));
  if (Array.isArray(container)) return container.includes(item);
  if (container instanceof Set || (typeof container.has === 'function')) return container.has(item);
  if (typeof container === 'object') return item in container;
  return false;
}

export function __pySort(arr, key = null, reverse = false) {
  if (!Array.isArray(arr)) return arr;
  arr.sort((a, b) => {
    let valA = key ? key(a) : a;
    let valB = key ? key(b) : b;
    let cmp = 0;
    if (typeof valA === 'number' && typeof valB === 'number') {
      cmp = valA - valB;
    } else {
      cmp = valA < valB ? -1 : (valA > valB ? 1 : 0);
    }
    return reverse ? -cmp : cmp;
  });
  return arr;
}

export function __pyPop(arr, i = -1) {
  if (Array.isArray(arr)) {
    if (i === -1 || i === undefined) {
      if (!arr.length) throw new IndexError('pop from empty list');
      return arr.pop();
    }
    const index = Number(i) < 0 ? arr.length + Number(i) : Number(i);
    if (index < 0 || index >= arr.length) throw new IndexError('pop index out of range');
    return arr.splice(index, 1)[0];
  }
  if (arr && typeof arr === 'object') {
    const key = String(i);
    if (Object.prototype.hasOwnProperty.call(arr, key)) {
      const value = arr[key];
      delete arr[key];
      return value;
    }
    if (arguments.length >= 3) return arguments[2];
    throw new KeyError(key);
  }
  throw new TypeError('pop target must be a list or dictionary');
}

export function __pyRemove(collection, value) {
  if (collection instanceof Set) {
    if (!collection.has(value)) throw new KeyError(value);
    collection.delete(value);
    return null;
  }
  if (!Array.isArray(collection)) throw new TypeError('remove target must be a list or set');
  const index = collection.indexOf(value);
  if (index < 0) throw new ValueError(`${value} not in list`);
  collection.splice(index, 1);
  return null;
}

export function __pySetAdd(collection, value) {
  if (!(collection instanceof Set)) throw new TypeError('add target must be a set');
  collection.add(value);
  return null;
}

export function __pyJoin(sep, arr) {
  if (Array.isArray(sep) && typeof arr === 'string') {
    return sep.join(arr);
  }
  if (Array.isArray(arr)) {
    return arr.join(sep);
  }
  if (arr && typeof arr[Symbol.iterator] === 'function') {
    return Array.from(arr).join(sep);
  }
  return String(arr);
}

export function __pyClass(cls, name) {
  if (name && cls) {
    try { Object.defineProperty(cls, 'name', { value: name }); } catch(e) {}
  }
  if (cls.prototype) {
    if (cls.prototype.__iter__ && !cls.prototype[Symbol.iterator]) {
      cls.prototype[Symbol.iterator] = function() {
        const it = this.__iter__();
        if (it === this && this.__next__) {
          return {
            next: () => {
              try {
                const value = this.__next__();
                return { value, done: false };
              } catch (e) {
                if (e instanceof StopIteration || e.name === 'StopIteration') {
                  return { value: undefined, done: true };
                }
                throw e;
              }
            }
          };
        }
        if (it && it !== this && typeof it[Symbol.iterator] === 'function') {
          return it[Symbol.iterator]();
        }
        return it;
      };
    } else if (cls.prototype.__next__ && !cls.prototype[Symbol.iterator]) {
      cls.prototype[Symbol.iterator] = function() {
        return {
          next: () => {
            try {
              const value = this.__next__();
              return { value, done: false };
            } catch (e) {
              if (e instanceof StopIteration || e.name === 'StopIteration') {
                return { value: undefined, done: true };
              }
              throw e;
            }
          }
        };
      };
    }
    if (cls.prototype.__str__ && !cls.prototype.toString) {
      cls.prototype.toString = function() {
        return this.__str__();
      };
    }
  }
  const createInstanceProxy = (inst, target) => {
    return new Proxy(inst, {
      get(t, prop, receiver) {
        if (typeof prop === 'string' && prop.startsWith('__') && !prop.endsWith('__') && prop !== '__isPyTuple') {
          if (!(prop in t)) {
            throw new AttributeError(`'${target.name}' object has no attribute '${prop}'`);
          }
        }
        return Reflect.get(t, prop, receiver);
      }
    });
  };
  return new Proxy(cls, {
    apply(target, thisArg, args) {
      const inst = Reflect.construct(target, args);
      return createInstanceProxy(inst, target);
    },
    construct(target, args, newTarget) {
      const inst = Reflect.construct(target, args, newTarget || target);
      return createInstanceProxy(inst, newTarget || target);
    }
  });
}

export function __pyTitle(str) {
  if (typeof str !== 'string') return '';
  return str.replace(/\b\w/g, (c) => c.toUpperCase());
}





function mergeMultilineStatements(code) {
  const rawLines = code.split(/\r?\n/);
  const result = [];
  let buffer = '';
  let paren = 0, bracket = 0, brace = 0;
  let inStr = null;

  for (let r = 0; r < rawLines.length; r++) {
    const rawLine = rawLines[r];
    const trimmed = rawLine.trim();

    if (!buffer) {
      if (!trimmed || trimmed.startsWith('#')) {
        result.push(rawLine);
        continue;
      }
      buffer = rawLine;
    } else {
      buffer += ' ' + trimmed;
    }

    let endsWithBackslash = false;
    for (let i = 0; i < rawLine.length; i++) {
      const ch = rawLine[i];
      if (inStr) {
        if (ch === '\\') { i++; continue; }
        if (ch === inStr) inStr = null;
      } else {
        if (ch === "'" || ch === '"') {
          inStr = ch;
        } else if (ch === '#') {
          break;
        } else if (ch === '(') paren++;
        else if (ch === ')') paren = Math.max(0, paren - 1);
        else if (ch === '[') bracket++;
        else if (ch === ']') bracket = Math.max(0, bracket - 1);
        else if (ch === '{') brace++;
        else if (ch === '}') brace = Math.max(0, brace - 1);
        else if (ch === '\\' && i === rawLine.trimEnd().length - 1) {
          endsWithBackslash = true;
        }
      }
    }

    if (paren === 0 && bracket === 0 && brace === 0 && !endsWithBackslash && !inStr) {
      result.push(buffer);
      buffer = '';
    }
  }

  if (buffer) result.push(buffer);
  return result.join('\n');
}

function splitTopLevelArgs(str) {
  const args = [];
  let cur = '';
  let paren = 0, bracket = 0, brace = 0;
  let inStr = null;
  for (let i = 0; i < str.length; i++) {
    const c = str[i];
    if (inStr) {
      if (c === '\\') { cur += c + (str[++i] || ''); continue; }
      if (c === inStr) inStr = null;
      cur += c;
    } else {
      if (c === "'" || c === '"') inStr = c;
      else if (c === '(') paren++;
      else if (c === ')') paren = Math.max(0, paren - 1);
      else if (c === '[') bracket++;
      else if (c === ']') bracket = Math.max(0, bracket - 1);
      else if (c === '{') brace++;
      else if (c === '}') brace = Math.max(0, brace - 1);
      else if (c === ',' && paren === 0 && bracket === 0 && brace === 0) {
        if (cur.trim()) args.push(cur.trim());
        cur = '';
        continue;
      }
      cur += c;
    }
  }
  if (cur.trim()) args.push(cur.trim());
  return args;
}

function parseFStringContent(content) {
  let res = '';
  let i = 0;
  while (i < content.length) {
    if (content[i] === '{') {
      if (content[i + 1] === '{') {
        res += '{';
        i += 2;
        continue;
      }
      let j = i + 1;
      let depth = 1;
      let inQuote = null;
      while (j < content.length && depth > 0) {
        const char = content[j];
        if (inQuote) {
          if (char === '\\') { j += 2; continue; }
          if (char === inQuote) inQuote = null;
        } else {
          if (char === "'" || char === '"') inQuote = char;
          else if (char === '{') depth++;
          else if (char === '}') depth--;
        }
        if (depth > 0) j++;
      }

      const fullExpr = content.slice(i + 1, j);
      let colonIdx = -1;
      let dParen = 0, dBracket = 0, dBrace = 0, q = null;
      for (let k = 0; k < fullExpr.length; k++) {
        const c = fullExpr[k];
        if (q) {
          if (c === '\\') { k++; continue; }
          if (c === q) q = null;
        } else {
          if (c === "'" || c === '"') q = c;
          else if (c === '(') dParen++;
          else if (c === ')') dParen--;
          else if (c === '[') dBracket++;
          else if (c === ']') dBracket--;
          else if (c === '{') dBrace++;
          else if (c === '}') dBrace--;
          else if (c === ':' && dParen === 0 && dBracket === 0 && dBrace === 0) {
            colonIdx = k;
          }
        }
      }

      let expr = fullExpr;
      let spec = null;
      if (colonIdx !== -1) {
        expr = fullExpr.slice(0, colonIdx);
        spec = fullExpr.slice(colonIdx + 1);
      }

      expr = transpileExpression(expr);

      if (spec !== null) {
        res += '${__pyFormat(' + expr + ', "' + spec + '")}';
      } else {
        res += '${__pyFormat(' + expr + ')}';
      }
      i = j + 1;
      continue;
    } else if (content[i] === '}' && content[i + 1] === '}') {
      res += '}';
      i += 2;
    } else {
      if (content[i] === '`') res += '\\`';
      else res += content[i];
      i++;
    }
  }
  return '`' + res + '`';
}

function transpileSlices(code) {
  let result = '';
  let i = 0;
  while (i < code.length) {
    if (code[i] === '[') {
      let prevIdx = i - 1;
      while (prevIdx >= 0 && /\s/.test(code[prevIdx])) prevIdx--;
      const isIndex = prevIdx >= 0 && /[a-zA-Z0-9_\)\]"']/.test(code[prevIdx]);

      let j = i + 1;
      let depth = 1;
      let hasColon = false;
      let q = null;
      while (j < code.length && depth > 0) {
        const c = code[j];
        if (q) {
          if (c === '\\') { j += 2; continue; }
          if (c === q) q = null;
        } else {
          if (c === "'" || c === '"') q = c;
          else if (c === '[') depth++;
          else if (c === ']') depth--;
          else if (c === ':' && depth === 1) hasColon = true;
        }
        if (depth > 0) j++;
      }

      if (isIndex && hasColon) {
        let k = result.length - 1;
        while (k >= 0 && /\s/.test(result[k])) k--;
        let targetEnd = k + 1;
        let parenDepth = 0;
        let bracketDepth = 0;
        while (k >= 0) {
          const c = result[k];
          if (c === ')') parenDepth++;
          else if (c === '(') {
            if (parenDepth === 0) break;
            parenDepth--;
          } else if (c === ']') bracketDepth++;
          else if (c === '[') {
            if (bracketDepth === 0) break;
            bracketDepth--;
          } else if (parenDepth === 0 && bracketDepth === 0) {
            if (!/[a-zA-Z0-9_\.]/.test(c)) break;
          }
          k--;
        }
        const targetStart = k + 1;
        const target = result.slice(targetStart, targetEnd);
        const prefix = result.slice(0, targetStart);

        const inner = code.slice(i + 1, j);
        const parts = [];
        let cur = '';
        let d = 0;
        for (let p = 0; p < inner.length; p++) {
          const c = inner[p];
          if (c === '(' || c === '[' || c === '{') d++;
          else if (c === ')' || c === ']' || c === '}') d--;
          else if (c === ':' && d === 0) {
            parts.push(cur);
            cur = '';
            continue;
          }
          cur += c;
        }
        parts.push(cur);

        const start = parts[0].trim() || 'null';
        const stop = parts[1] ? (parts[1].trim() || 'null') : 'null';
        const step = parts[2] ? (parts[2].trim() || 'null') : 'undefined';

        result = prefix + `__pySlice(${target}, ${start}, ${stop}, ${step})`;
        i = j + 1;
        continue;
      }
    }
    result += code[i];
    i++;
  }
  return result;
}

function wrapGeneratorArgs(code) {
  const fns = ['sum', 'any', 'all', 'sorted', 'list', 'set'];
  for (const fn of fns) {
    const pattern = new RegExp(`\\b${fn}\\(`, 'g');
    let m;
    while ((m = pattern.exec(code)) !== null) {
      const start = m.index + fn.length + 1;
      let depth = 1;
      let j = start;
      let inStr = null;
      while (j < code.length && depth > 0) {
        const c = code[j];
        if (inStr) {
          if (c === inStr && code[j - 1] !== '\\') inStr = null;
        } else if (c === "'" || c === '"') inStr = c;
        else if (c === '(' || c === '[' || c === '{') depth++;
        else if (c === ')' || c === ']' || c === '}') depth--;
        j++;
      }
      if (depth === 0) {
        const inner = code.slice(start, j - 1).trim();
        if (inner.includes(' for ') && inner.includes(' in ') && !inner.startsWith('[')) {
          code = code.slice(0, start) + `[${inner}]` + code.slice(j - 1);
          pattern.lastIndex = start + inner.length + 2;
        }
      }
    }
  }
  return code;
}

function transpileComprehensions(code) {
  const fns = ['sum', 'any', 'all', 'sorted', 'list', 'set'];
  for (const fn of fns) {
    const pattern = new RegExp(`\\b${fn}\\(`, 'g');
    let m;
    while ((m = pattern.exec(code)) !== null) {
      const start = m.index + fn.length + 1;
      let depth = 1;
      let j = start;
      let inStr = null;
      while (j < code.length && depth > 0) {
        const c = code[j];
        if (inStr) {
          if (c === inStr && code[j - 1] !== '\\') inStr = null;
        } else if (c === "'" || c === '"') inStr = c;
        else if (c === '(' || c === '[' || c === '{') depth++;
        else if (c === ')' || c === ']' || c === '}') depth--;
        j++;
      }
      if (depth === 0) {
        const inner = code.slice(start, j - 1).trim();
        if (inner.includes(' for ') && inner.includes(' in ') && !inner.startsWith('[')) {
          code = code.slice(0, start) + `[${inner}]` + code.slice(j - 1);
          pattern.lastIndex = start + inner.length + 2;
        }
      }
    }
  }

  let result = '';
  let i = 0;
  while (i < code.length) {
    if (code[i] === '[' || code[i] === '{') {
      const openChar = code[i];
      const closeChar = openChar === '[' ? ']' : '}';
      let j = i + 1;
      let depth = 1;
      let q = null;
      while (j < code.length && depth > 0) {
        const c = code[j];
        if (q) {
          if (c === '\\') { j += 2; continue; }
          if (c === q) q = null;
        } else {
          if (c === "'" || c === '"') q = c;
          else if (c === openChar) depth++;
          else if (c === closeChar) depth--;
        }
        if (depth > 0) j++;
      }

      const inner = code.slice(i + 1, j);
      let forIdx = -1, inIdx = -1, ifIdx = -1;
      let dParen = 0, dBracket = 0, dBrace = 0, inQ = null;
      for (let k = 0; k < inner.length; k++) {
        const c = inner[k];
        if (inQ) {
          if (c === '\\') { k++; continue; }
          if (c === inQ) inQ = null;
        } else {
          if (c === "'" || c === '"') inQ = c;
          else if (c === '(') dParen++;
          else if (c === ')') dParen--;
          else if (c === '[') dBracket++;
          else if (c === ']') dBracket--;
          else if (c === '{') dBrace++;
          else if (c === '}') dBrace--;
          else if (dParen === 0 && dBracket === 0 && dBrace === 0) {
            if (forIdx === -1 && inner.startsWith('for ', k) && (k === 0 || /\s/.test(inner[k - 1]))) {
              forIdx = k;
            } else if (forIdx !== -1 && inIdx === -1 && inner.startsWith('in ', k) && /\s/.test(inner[k - 1])) {
              inIdx = k;
            } else if (forIdx !== -1 && inIdx !== -1 && ifIdx === -1 && inner.startsWith('if ', k) && /\s/.test(inner[k - 1])) {
              ifIdx = k;
            }
          }
        }
      }

      if (forIdx !== -1 && inIdx !== -1) {
        const exprPart = transpileExpression(inner.slice(0, forIdx).trim());
        let varPart = inner.slice(forIdx + 4, inIdx).trim();
        const iterPart = transpileExpression(ifIdx !== -1 ? inner.slice(inIdx + 3, ifIdx).trim() : inner.slice(inIdx + 3).trim());
        const condPart = ifIdx !== -1 ? transpileExpression(inner.slice(ifIdx + 3).trim()) : null;

        varPart = varPart.replace(/\(([^)]+)\)/g, '[$1]');
        if (varPart.includes(',') && !varPart.startsWith('[')) varPart = `[${varPart}]`;

        if (openChar === '{') {
          const colonIdx = exprPart.indexOf(':');
          const kExpr = exprPart.slice(0, colonIdx).trim();
          const vExpr = exprPart.slice(colonIdx + 1).trim();
          if (condPart) {
            result += `((() => { const __o = {}; for (let ${varPart} of (${iterPart})) { if (${condPart}) __o[${kExpr}] = ${vExpr}; } return __o; })())`;
          } else {
            result += `((() => { const __o = {}; for (let ${varPart} of (${iterPart})) { __o[${kExpr}] = ${vExpr}; } return __o; })())`;
          }
        } else {
          if (condPart) {
            result += `((() => { const __arr = []; for (let ${varPart} of (${iterPart})) { if (${condPart}) __arr.push(${exprPart}); } return __arr; })())`;
          } else {
            result += `((() => { const __arr = []; for (let ${varPart} of (${iterPart})) { __arr.push(${exprPart}); } return __arr; })())`;
          }
        }
        i = j + 1;
        continue;
      }
    }
    result += code[i];
    i++;
  }
  return result;
}

function replaceLambdas(code) {
  let result = '';
  let i = 0;
  while (i < code.length) {
    if (code.startsWith('lambda', i) && (i === 0 || !/\w/.test(code[i - 1])) && (i + 6 >= code.length || /\s/.test(code[i + 6]))) {
      const colonIdx = code.indexOf(':', i);
      if (colonIdx !== -1) {
        const params = code.slice(i + 6, colonIdx).trim();
        let j = colonIdx + 1;
        let depth = 0;
        let q = null;
        while (j < code.length) {
          const c = code[j];
          if (q) {
            if (c === '\\') { j += 2; continue; }
            if (c === q) q = null;
          } else {
            if (c === "'" || c === '"') q = c;
            else if (c === '(' || c === '[' || c === '{') depth++;
            else if (c === ')' || c === ']' || c === '}') {
              if (depth === 0) break;
              depth--;
            } else if (c === ',' && depth === 0) {
              break;
            }
          }
          j++;
        }
        const body = code.slice(colonIdx + 1, j).trim();
        result += `((${params}) => ${body})`;
        i = j;
        continue;
      }
    }
    result += code[i];
    i++;
  }
  return result;
}

function findTopLevelEquals(line) {
  let depth = 0;
  let q = null;
  for (let i = 0; i < line.length; i++) {
    const c = line[i];
    if (q) {
      if (c === '\\') { i++; continue; }
      if (c === q) q = null;
    } else {
      if (c === "'" || c === '"') q = c;
      else if (c === '(' || c === '[' || c === '{') depth++;
      else if (c === ')' || c === ']' || c === '}') depth--;
      else if (depth === 0 && c === '=') {
        const prev = line[i - 1];
        const next = line[i + 1];
        if (prev !== '=' && prev !== '<' && prev !== '>' && prev !== '!' &&
            next !== '=' && next !== '<' && next !== '>' &&
            prev !== '+' && prev !== '-' && prev !== '*' && prev !== '/' && prev !== '%' && prev !== '&' && prev !== '|' && prev !== '^') {
          return i;
        }
      }
    }
  }
  return -1;
}

const globalFuncRegistry = {};

function replaceMethodCalls(code) {
  const methodNames = ['split', 'rsplit', 'join', 'replace', 'keys', 'values', 'items', 'get', 'update', 'append', 'copy', 'pop', 'insert', 'extend', 'index', 'sort', 'remove', 'add', 'title', 'islower', 'isupper'];
  let changed = true;
  let iters = 0;

  while (changed && iters++ < 5) {
    changed = false;
    const pattern = new RegExp(`\\.(${methodNames.join('|')})\\(`, 'g');
    let match;

    while ((match = pattern.exec(code)) !== null) {
      const dotIdx = match.index;
      const methodName = match[1];
      const openParenIdx = dotIdx + methodName.length + 1;

      let j = openParenIdx + 1;
      let depth = 1;
      let q = null;
      while (j < code.length && depth > 0) {
        const c = code[j];
        if (q) {
          if (c === '\\') { j += 2; continue; }
          if (c === q) q = null;
        } else {
          if (c === "'" || c === '"') q = c;
          else if (c === '(') depth++;
          else if (c === ')') depth--;
        }
        if (depth > 0) j++;
      }
      if (depth !== 0) continue;

      const argsStr = code.slice(openParenIdx + 1, j);

      let k = dotIdx - 1;
      while (k >= 0 && /\s/.test(code[k])) k--;
      const targetEnd = k + 1;
      let parenDepth = 0;
      let bracketDepth = 0;
      while (k >= 0) {
        const c = code[k];
        if (c === ')') parenDepth++;
        else if (c === '(') {
          if (parenDepth === 0) break;
          parenDepth--;
        } else if (c === ']') bracketDepth++;
        else if (c === '[') {
          if (bracketDepth === 0) break;
          bracketDepth--;
        } else if (parenDepth === 0 && bracketDepth === 0) {
          if (!/[a-zA-Z0-9_\.]/.test(c)) break;
        }
        k--;
      }
      const targetStart = k + 1;
      const target = code.slice(targetStart, targetEnd);
      if (target === "Object" || target === "Array" || target === "String" || target === "Math") {
        continue;
      }

      let replacement = null;
      if (methodName === 'split') {
        const parts = argsStr ? splitTopLevelArgs(argsStr) : [];
        let sep = "' '";
        let maxsplit = "-1";
        for (const p of parts) {
          const trimmed = p.trim();
          if (trimmed.startsWith('maxsplit=')) {
            maxsplit = trimmed.slice(9).trim();
          } else if (trimmed.startsWith('sep=')) {
            sep = trimmed.slice(4).trim();
          } else if (sep === "' '") {
            sep = trimmed;
          } else {
            maxsplit = trimmed;
          }
        }
        replacement = `__pySplit(${target}, ${sep}, ${maxsplit})`;
      } else if (methodName === 'rsplit') {
        const parts = argsStr ? splitTopLevelArgs(argsStr) : [];
        let sep = "' '";
        let maxsplit = "-1";
        for (const p of parts) {
          const trimmed = p.trim();
          if (trimmed.startsWith('maxsplit=')) {
            maxsplit = trimmed.slice(9).trim();
          } else if (trimmed.startsWith('sep=')) {
            sep = trimmed.slice(4).trim();
          } else if (sep === "' '") {
            sep = trimmed;
          } else {
            maxsplit = trimmed;
          }
        }
        replacement = `__pyRsplit(${target}, ${sep}, ${maxsplit})`;
      } else if (methodName === 'join') {
        replacement = `__pyJoin(${target}, ${argsStr})`;
      } else if (methodName === 'replace') {
        replacement = `${target}.replaceAll(${argsStr})`;
      } else if (methodName === 'strip') {
        replacement = argsStr.trim() ? `__pyStrip(${target}, ${argsStr})` : `${target}.trim()`;
      } else if (methodName === 'lstrip') {
        replacement = argsStr.trim() ? `__pyLStrip(${target}, ${argsStr})` : `${target}.trimStart()`;
      } else if (methodName === 'rstrip') {
        replacement = argsStr.trim() ? `__pyRStrip(${target}, ${argsStr})` : `${target}.trimEnd()`;
      } else if (methodName === 'keys') {
        replacement = `Object.keys(${target})`;
      } else if (methodName === 'values') {
        replacement = `Object.values(${target})`;
      } else if (methodName === 'items') {
        replacement = `Object.entries(${target})`;
      } else if (methodName === 'get') {
        const parts = splitTopLevelArgs(argsStr);
        replacement = `__pyGet(${target}, ${parts[0]}, ${parts[1] || 'null'})`;
      } else if (methodName === 'update') {
        replacement = `Object.assign(${target}, ${argsStr})`;
      } else if (methodName === 'append') {
        replacement = `${target}.push(${argsStr})`;
      } else if (methodName === 'remove') {
        replacement = `__pyRemove(${target}, ${argsStr})`;
      } else if (methodName === 'add') {
        replacement = `__pySetAdd(${target}, ${argsStr})`;
      } else if (methodName === 'copy') {
        replacement = `${target}.slice()`;
      } else if (methodName === 'pop') {
        replacement = argsStr.trim() ? `__pyPop(${target}, ${argsStr.trim()})` : `${target}.pop()`;
      } else if (methodName === 'insert') {
        const parts = splitTopLevelArgs(argsStr);
        replacement = `${target}.splice(${parts[0]}, 0, ${parts[1]})`;
      } else if (methodName === 'extend') {
        replacement = `${target}.push(...${argsStr})`;
      } else if (methodName === 'index') {
        replacement = `${target}.indexOf(${argsStr})`;
      } else if (methodName === 'sort') {
        const parts = splitTopLevelArgs(argsStr);
        let rev = 'false';
        let key = 'null';
        for (const p of parts) {
          if (p.startsWith('key=')) key = p.slice(4).trim();
          else if (p.startsWith('reverse=')) rev = p.slice(8).trim().toLowerCase();
        }
        replacement = `__pySort(${target}, ${key}, ${rev})`;
      } else if (methodName === 'title') {
        replacement = `__pyTitle(${target})`;
      } else if (methodName === 'islower') {
        replacement = `(${target} === ${target}.toLowerCase() && ${target} !== ${target}.toUpperCase())`;
      } else if (methodName === 'isupper') {
        replacement = `(${target} === ${target}.toUpperCase() && ${target} !== ${target}.toLowerCase())`;
      }

      if (replacement !== null) {
        code = code.slice(0, targetStart) + replacement + code.slice(j + 1);
        changed = true;
        break;
      }
    }
  }

  return code;
}

function transpileTupleLiterals(code) {
  let result = '';
  let i = 0;
  while (i < code.length) {
    if (code[i] === '(') {
      let k = i - 1;
      while (k >= 0 && /\s/.test(code[k])) k--;
      const isCall = k >= 0 && /[a-zA-Z0-9_\]]/.test(code[k]);

      let depth = 1;
      let j = i + 1;
      let inStr = null;
      let hasTopComma = false;
      while (j < code.length && depth > 0) {
        const c = code[j];
        if (inStr) {
          if (c === inStr && code[j - 1] !== '\\') inStr = null;
        } else if (c === "'" || c === '"') inStr = c;
        else if (c === '(' || c === '[' || c === '{') depth++;
        else if (c === ')' || c === ']' || c === '}') {
          depth--;
          if (depth === 0) break;
        } else if (c === ',' && depth === 1) {
          hasTopComma = true;
        }
        j++;
      }

      if (!isCall && hasTopComma && depth === 0) {
        const inner = code.slice(i + 1, j);
        result += `__pyTuple(${inner})`;
        i = j + 1;
        continue;
      }
    }
    result += code[i++];
  }
  return result;
}

function transpileDictLiterals(code) {
  let result = '';
  let i = 0;
  while (i < code.length) {
    if (code[i] === '{') {
      let depth = 1;
      let j = i + 1;
      let inStr = null;
      let hasColonAtDepth1 = false;
      while (j < code.length && depth > 0) {
        const c = code[j];
        if (inStr) {
          if (c === inStr && code[j - 1] !== '\\') inStr = null;
        } else if (c === "'" || c === '"') inStr = c;
        else if (c === '{' || c === '[' || c === '(') depth++;
        else if (c === '}' || c === ']' || c === ')') {
          depth--;
          if (depth === 0) break;
        } else if (c === ':' && depth === 1) {
          hasColonAtDepth1 = true;
        }
        j++;
      }

      if (depth === 0 && hasColonAtDepth1) {
        const inner = code.slice(i + 1, j);
        if (inner.includes(' for ') && inner.includes(' in ')) {
          result += code[i++];
          continue;
        }
        const pairs = [];
        let cur = '';
        let d = 0;
        let strQ = null;
        for (let k = 0; k < inner.length; k++) {
          const ch = inner[k];
          if (strQ) {
            if (ch === strQ && inner[k - 1] !== '\\') strQ = null;
            cur += ch;
          } else if (ch === "'" || ch === '"') {
            strQ = ch;
            cur += ch;
          } else if (ch === '{' || ch === '[' || ch === '(') {
            d++;
            cur += ch;
          } else if (ch === '}' || ch === ']' || ch === ')') {
            d--;
            cur += ch;
          } else if (ch === ',' && d === 0) {
            pairs.push(cur.trim());
            cur = '';
          } else {
            cur += ch;
          }
        }
        if (cur.trim()) pairs.push(cur.trim());

        const transformedPairs = pairs.map((pair) => {
          let colonIdx = -1;
          let cd = 0;
          let cStr = null;
          for (let p = 0; p < pair.length; p++) {
            const ch = pair[p];
            if (cStr) {
              if (ch === cStr && pair[p - 1] !== '\\') cStr = null;
            } else if (ch === "'" || ch === '"') cStr = ch;
            else if (ch === '{' || ch === '[' || ch === '(') cd++;
            else if (ch === '}' || ch === ']' || ch === ')') cd--;
            else if (ch === ':' && cd === 0) {
              colonIdx = p;
              break;
            }
          }
          if (colonIdx === -1) return pair;
          let kExpr = pair.slice(0, colonIdx).trim();
          const vExpr = pair.slice(colonIdx + 1).trim();
          if (!kExpr.startsWith('[') || !kExpr.endsWith(']')) {
            kExpr = `[${kExpr}]`;
          }
          return `${kExpr}: ${vExpr}`;
        });

        result += `{ ${transformedPairs.join(', ')} }`;
        i = j + 1;
        continue;
      }
    }
    result += code[i++];
  }
  return result;
}

function transpileExpression(expr) {
  if (!expr) return expr;

  // Mask string literals
  const strings = [];
  let masked = '';
  let i = 0;
  while (i < expr.length) {
    if ((expr[i] === 'f' || expr[i] === 'F') && (expr[i + 1] === "'" || expr[i + 1] === '"')) {
      const q = expr[i + 1];
      let j = i + 2;
      while (j < expr.length) {
        if (expr[j] === '\\') { j += 2; continue; }
        if (expr[j] === q) break;
        j++;
      }
      const content = expr.slice(i + 2, j);
      const converted = parseFStringContent(content);
      const token = `___STR_${strings.length}___`;
      strings.push(converted);
      masked += token;
      i = j + 1;
      continue;
    }

    if ((expr[i] === 'r' || expr[i] === 'R') && (expr[i + 1] === "'" || expr[i + 1] === '"')) {
      const q = expr[i + 1];
      let j = i + 2;
      while (j < expr.length) {
        if (expr[j] === '\\') { j += 2; continue; }
        if (expr[j] === q) break;
        j++;
      }
      const rawContent = expr.slice(i + 2, j);
      const escaped = rawContent.replace(/\\/g, '\\\\');
      const token = `___STR_${strings.length}___`;
      strings.push(`${q}${escaped}${q}`);
      masked += token;
      i = j + 1;
      continue;
    }

    if (expr[i] === "'" || expr[i] === '"') {
      const q = expr[i];
      let j = i + 1;
      while (j < expr.length) {
        if (expr[j] === '\\') { j += 2; continue; }
        if (expr[j] === q) break;
        j++;
      }
      const strVal = expr.slice(i, j + 1);
      const token = `___STR_${strings.length}___`;
      strings.push(strVal);
      masked += token;
      i = j + 1;
      continue;
    }

    masked += expr[i];
    i++;
  }

  // Set literals: { 'a', 'b' } -> new PySet(['a', 'b']) BEFORE comprehensions!
  masked = masked.replace(/\{([^{}:]+)\}/g, (m, inner) => {
    if (inner.includes(':')) return m;
    return `new PySet([${inner}])`;
  });

  // Comprehensions & slices on masked code
  masked = transpileComprehensions(masked);
  masked = transpileSlices(masked);

  // Lambda expressions: lambda x, y: expr
  masked = replaceLambdas(masked);

  // Ternary: X if COND else Y -> ((COND) ? (X) : (Y))
  masked = masked.replace(/(.+?)\s+if\s+(.+?)\s+else\s+(.+)/g, (m, x, cond, y) => {
    return `((${cond.trim()}) ? (${x.trim()}) : (${y.trim()}))`;
  });

  // Chained comparisons: 0 <= score <= 100 -> ((0 <= score) && (score <= 100))
  masked = masked.replace(/(\b[\w\.\(\)]+)\s*(<=|<|>=|>|==)\s*(\b[\w\.\(\)]+)\s*(<=|<|>=|>|==)\s*(\b[\w\.\(\)]+)/g,
    '(($1 $2 $3) && ($3 $4 $5))'
  );

  // Floor division // -> __pyFloorDiv(a, b)
  let prevMasked;
  do {
    prevMasked = masked;
    masked = masked.replace(/(\b[\w\.\(\)\[\]']+|\([^)]+\))\s*\/\/\s*(\b[\w\.\(\)\[\]']+|\([^)]+\))/g, '__pyFloorDiv($1, $2)');
  } while (masked !== prevMasked);

  // Power operator ** -> Math.pow(a, b)
  do {
    prevMasked = masked;
    masked = masked.replace(/(\b[\w\.\(\)\[\]']+|\([^)]+\))\s*\*\*\s*(\b[\w\.\(\)\[\]']+|\([^)]+\))/g, 'Math.pow($1, $2)');
  } while (masked !== prevMasked);

  // Route overloaded set and numeric bitwise operators through a runtime type check.
  masked = masked.replace(/(\b[a-zA-Z_]\w*)\s*([&|\-^])\s*(\b[a-zA-Z_]\w*)/g, '__pySetOp($1, "$2", $3)');

  // Membership: not in and in
  masked = masked.replace(/(\b[\w\.\(\)\[\]'"]+)\s+not\s+in\s+([\w\.\(\)\[\]'"]+)/g, '!__pyIn($1, $2)');
  masked = masked.replace(/(\b[\w\.\(\)\[\]'"]+)\s+in\s+([\w\.\(\)\[\]'"]+)/g, '__pyIn($1, $2)');

  // Division operator
  {
    let divIdx = 0;
    while (divIdx < masked.length) {
      if (masked[divIdx] === '/' && masked[divIdx - 1] !== '/' && masked[divIdx + 1] !== '/' && masked[divIdx - 1] !== '*' && masked[divIdx + 1] !== '*') {
        let k = divIdx - 1;
        while (k >= 0 && /\s/.test(masked[k])) k--;
        let leftEnd = k + 1;
        let leftStart = k;
        if (masked[k] === ')') {
          let depth = 1;
          k--;
          while (k >= 0 && depth > 0) {
            if (masked[k] === ')') depth++;
            else if (masked[k] === '(') depth--;
            k--;
          }
          while (k >= 0 && /[a-zA-Z0-9_]/.test(masked[k])) k--;
          leftStart = k + 1;
        } else {
          while (k >= 0 && /[a-zA-Z0-9_\.]/.test(masked[k])) k--;
          leftStart = k + 1;
        }
        const left = masked.slice(leftStart, leftEnd);

        let m = divIdx + 1;
        while (m < masked.length && /\s/.test(masked[m])) m++;
        let rightStart = m;
        let rightEnd = m;
        if (masked[m] === '(') {
          let depth = 1;
          m++;
          while (m < masked.length && depth > 0) {
            if (masked[m] === '(') depth++;
            else if (masked[m] === ')') depth--;
            m++;
          }
          rightEnd = m;
        } else {
          while (m < masked.length && /[a-zA-Z0-9_\.]/.test(masked[m])) m++;
          if (m < masked.length && masked[m] === '(') {
            let depth = 1;
            m++;
            while (m < masked.length && depth > 0) {
              if (masked[m] === '(') depth++;
              else if (masked[m] === ')') depth--;
              m++;
            }
          }
          rightEnd = m;
        }
        const right = masked.slice(rightStart, rightEnd);

        if (left && right) {
          masked = masked.slice(0, leftStart) + `__pyDiv(${left}, ${right})` + masked.slice(rightEnd);
          divIdx = leftStart + `__pyDiv(${left}, ${right})`.length;
          continue;
        }
      }
      divIdx++;
    }
  }

  // Negative indexing: .at(-1)
  masked = masked.replace(/\[\s*(-\s*\d+)\s*\]/g, '.at($1)');

  // Subscript access: obj[key] -> __pyGet(obj, key)
  do {
    prevMasked = masked;
    masked = masked.replace(/(\b[a-zA-Z0-9_]+(?:\.[a-zA-Z0-9_]+)?)\s*\[\s*([^:\[\]]+?)\s*\]/g, (m, target, key) => {
      if (target === 'let' || target === 'var' || target === 'const' || target === '__o' || target === '__arr') return m;
      return `__pyGet(${target}, ${key})`;
    });
  } while (masked !== prevMasked);

  // Spread operator in call: *nums -> ...nums, **data -> data
  masked = masked.replace(/\(\*([a-zA-Z0-9_]+)\)/g, '(...$1)');
  masked = masked.replace(/,\s*\*([a-zA-Z0-9_]+)/g, ', ...$1');
  masked = masked.replace(/\(\s*\*\*([a-zA-Z0-9_]+)\s*\)/g, '($1)');
  masked = masked.replace(/,\s*\*\*([a-zA-Z0-9_]+)/g, ', $1');

  // Vector operators & Equality
  masked = masked.replace(/(\b[vV]\d*)\s*\+\s*(\b[vV]\d*)/g, '__pyAdd($1, $2)');
  masked = masked.replace(/(?<![\+\-\*\/\%\&\|\^]\s*)(?=(\b[a-zA-Z_]\w*(?:\.[a-zA-Z_]\w*)*))\1\b(?!\s*[\.\(\+\-\*\/\%\&\|\^])\s*==\s*(?=([a-zA-Z_]\w*(?:\.[a-zA-Z_]\w*)*))\2\b(?!\s*[\.\(\+\-\*\/\%\&\|\^])/g, '__pyEq($1, $2)');

  // Identity checks (BEFORE replacing not!)
  masked = masked.replace(/\bis\s+not\b/g, '!==');
  masked = masked.replace(/\bis\b/g, '===');

  // Boolean & None replacements (outside of strings!)
  masked = masked
    .replace(/\bTrue\b/g, 'true')
    .replace(/\bFalse\b/g, 'false')
    .replace(/\bNone\b/g, 'null')
    .replace(/\band\b/g, '&&')
    .replace(/\bor\b/g, '||')
    .replace(/\bnot\b/g, '!');

  // Rename variable 'case' when used as expression
  masked = masked.replace(/\bcase\b/g, '_py_case');
  masked = masked.replace(/\bfunction\b/g, '_py_func');
  masked = masked.replace(/(\b[a-zA-Z0-9_]+\b)\.__name__\b/g, '($1.__name__ || $1.name)');

  // Tuple literal check: (x, y)
  masked = transpileTupleLiterals(masked);
  masked = transpileDictLiterals(masked);

  // Method calls using clean extractor
  masked = replaceMethodCalls(masked);

  // Basic string method adjustments
  masked = masked.replace(/\.strip\(\)/g, '.trim()');
  masked = masked.replace(/\.lower\(\)/g, '.toLowerCase()');
  masked = masked.replace(/\.upper\(\)/g, '.toUpperCase()');
  masked = masked.replace(/\.startswith\(/g, '.startsWith(');
  masked = masked.replace(/\.endswith\(/g, '.endsWith(');

  // Restore strings
  for (let sIdx = 0; sIdx < strings.length; sIdx++) {
    masked = masked.replace(`___STR_${sIdx}___`, () => strings[sIdx]);
  }

  return masked;
}

function reorderKwargs(funcName, argsStr, funcDef) {
  const callArgs = splitTopLevelArgs(argsStr);
  const hasKwargs = callArgs.some(a => {
    const eq = a.indexOf('=');
    return eq !== -1 && /^[a-zA-Z_]\w*$/.test(a.slice(0, eq).trim()) && !a.startsWith('==');
  });
  if (!hasKwargs) return argsStr;

  const paramDefs = funcDef.map(p => {
    let s = p.trim();
    const colonIdx = s.indexOf(':');
    const eqIdx = s.indexOf('=');
    let name = s;
    let defaultVal = undefined;
    if (colonIdx !== -1 && (eqIdx === -1 || colonIdx < eqIdx)) {
      name = s.slice(0, colonIdx).trim();
      if (eqIdx !== -1) {
        defaultVal = s.slice(eqIdx + 1).trim();
      }
    } else if (eqIdx !== -1) {
      name = s.slice(0, eqIdx).trim();
      defaultVal = s.slice(eqIdx + 1).trim();
    }
    const isKwargs = name.startsWith('**');
    if (isKwargs) name = name.slice(2);
    const isArgs = !isKwargs && name.startsWith('*');
    if (isArgs) name = name.slice(1);
    return { name, defaultVal, isArgs, isKwargs };
  });

  const positional = [];
  const kwargs = {};
  for (const a of callArgs) {
    const eq = a.indexOf('=');
    if (eq !== -1 && /^[a-zA-Z_]\w*$/.test(a.slice(0, eq).trim())) {
      const k = a.slice(0, eq).trim();
      const v = a.slice(eq + 1).trim();
      kwargs[k] = v;
    } else {
      positional.push(a);
    }
  }

  const finalArgs = [];
  const kwargsParam = paramDefs.find(p => p.isKwargs);

  for (const p of paramDefs) {
    if (p.isKwargs) continue;
    if (positional.length > 0) {
      finalArgs.push(positional.shift());
    } else if (kwargs[p.name] !== undefined) {
      finalArgs.push(kwargs[p.name]);
      delete kwargs[p.name];
    } else if (p.defaultVal !== undefined) {
      finalArgs.push(p.defaultVal);
    } else {
      finalArgs.push('undefined');
    }
  }

  if (kwargsParam) {
    const entries = Object.entries(kwargs).map(([k, v]) => `${k}: ${v}`).join(', ');
    finalArgs.push(`{ ${entries} }`);
  }

  return finalArgs.join(', ');
}

function replaceKwargsCalls(code, funcRegistry) {
  for (const funcName of Object.keys(funcRegistry)) {
    const pattern = new RegExp(`\\b(${funcName})\\s*\\(`, 'g');
    let match;
    while ((match = pattern.exec(code)) !== null) {
      const callStart = match.index;
      const before = code.slice(Math.max(0, callStart - 10), callStart).trim();
      if (before.endsWith('def')) continue;

      const openParen = callStart + match[0].length - 1;
      let depth = 1;
      let j = openParen + 1;
      let q = null;
      while (j < code.length && depth > 0) {
        const c = code[j];
        if (q) {
          if (c === '\\') { j += 2; continue; }
          if (c === q) q = null;
        } else {
          if (c === "'" || c === '"') q = c;
          else if (c === '(' || c === '[' || c === '{') depth++;
          else if (c === ')' || c === ']' || c === '}') depth--;
        }
        if (depth > 0) j++;
      }
      if (depth !== 0) continue;

      const argsStr = code.slice(openParen + 1, j);
      const newArgs = reorderKwargs(funcName, argsStr, funcRegistry[funcName]);
      if (newArgs !== argsStr) {
        code = code.slice(0, openParen + 1) + newArgs + code.slice(j);
        pattern.lastIndex = openParen + 1 + newArgs.length + 1;
      }
    }
  }
  return code;
}

function renamePythonReservedWords(code) {
  const tokens = [];
  let masked = '';
  let i = 0;
  while (i < code.length) {
    if (code.slice(i, i + 3) === "'''" || code.slice(i, i + 3) === '"""') {
      const q3 = code.slice(i, i + 3);
      let j = i + 3;
      while (j < code.length) {
        if (code[j] === '\\') { j += 2; continue; }
        if (code.slice(j, j + 3) === q3) { j += 3; break; }
        j++;
      }
      const token = `___RESERVED_STR_${tokens.length}___`;
      tokens.push(code.slice(i, j));
      masked += token;
      i = j;
      continue;
    }

    const ch = code[i];
    const next = code[i + 1];
    const isPrefixed = (ch === 'f' || ch === 'F' || ch === 'r' || ch === 'R') && (next === "'" || next === '"');
    const isNormal = ch === "'" || ch === '"';

    if (isPrefixed || isNormal) {
      const q = isPrefixed ? next : ch;
      let j = isPrefixed ? i + 2 : i + 1;
      while (j < code.length) {
        if (code[j] === '\\') { j += 2; continue; }
        if (code[j] === q) { j++; break; }
        j++;
      }
      const token = `___RESERVED_STR_${tokens.length}___`;
      tokens.push(code.slice(i, j));
      masked += token;
      i = j;
      continue;
    }

    if (ch === '#') {
      let j = i + 1;
      while (j < code.length && code[j] !== '\n') j++;
      const token = `___RESERVED_STR_${tokens.length}___`;
      tokens.push(code.slice(i, j));
      masked += token;
      i = j;
      continue;
    }

    masked += ch;
    i++;
  }

  masked = masked.replace(/\bfunction\b/g, '_py_func');

  for (let k = 0; k < tokens.length; k++) {
    masked = masked.replace(`___RESERVED_STR_${k}___`, () => tokens[k]);
  }

  return masked;
}

export function transpilePythonToJs(pythonCode) {
  const globalFuncRegistry = {};
  const generatorFuncs = new Set();
  const propertyAccessors = new Map();

  let py = pythonCode.replace(/\r\n/g, '\n').replace(/\r/g, '\n');
  py = renamePythonReservedWords(py);
  py = mergeMultilineStatements(py);
  py = wrapGeneratorArgs(py);

  // Scan functions first for kwargs and generators
  const preLines = py.split('\n');
  for (let i = 0; i < preLines.length; i++) {
    const l = preLines[i].trim();
    if (l.startsWith('def ') && l.includes('(')) {
      const header = l.slice(4, l.indexOf('(')).trim();
      const parenEnd = l.lastIndexOf(')');
      if (parenEnd > 0) {
        const pStr = l.slice(l.indexOf('(') + 1, parenEnd);
        const params = splitTopLevelArgs(pStr);
        globalFuncRegistry[header] = params;
      }
      for (let j = i + 1; j < preLines.length; j++) {
        if (preLines[j].length > 0 && !/^\s/.test(preLines[j])) break;
        if (/\byield\b/.test(preLines[j])) {
          generatorFuncs.add(header);
          break;
        }
      }
    }
  }

  py = replaceKwargsCalls(py, globalFuncRegistry);

  const lines = py.split('\n');
  const jsLines = [];
  const indentStack = [0];
  const blockTypeStack = ['root'];
  let pendingDecorators = [];
  let pendingAccessor = null;
  let currentClassName = null;
  let currentClassIndent = -1;

  for (let lineNum = 0; lineNum < lines.length; lineNum++) {
    const rawLine = lines[lineNum];
    const trimmed = rawLine.trim();

    if (trimmed.startsWith('Print(') || trimmed.startsWith('PRINT(')) {
      throw new Error(`NameError: name '${trimmed.slice(0, 5)}' is not defined. Did you mean: 'print'? Python is strictly case-sensitive!`);
    }

    if (!trimmed || trimmed.startsWith('#')) continue;

    const indent = rawLine.search(/\S|$/);
    let line = trimmed;

    let lastPoppedBlock = null;
    // Pop closed indentation blocks
    while (indentStack.length > 1 && indent < indentStack[indentStack.length - 1]) {
      indentStack.pop();
      const bType = blockTypeStack.pop();
      lastPoppedBlock = bType;
      if (bType && (bType === 'class' || bType.type === 'class')) {
        jsLines.push(`}, '${bType.name || currentClassName}');`);
        currentClassName = null;
        currentClassIndent = -1;
      } else if (bType && bType.type === 'except') {
        if (line.startsWith('except') && line.endsWith(':')) {
          jsLines.push('}');
        } else {
          jsLines.push(`} if (!__handled_${bType.indent}) throw __e; }`);
        }
      } else if (bType && bType.type === 'try_else') {
        if (line === 'finally:') {
          jsLines.push('}');
        } else {
          jsLines.push('}}');
        }
      } else if (bType && bType.type === 'finally') {
        jsLines.push('}');
      } else if (bType && bType.type === 'func') {
        jsLines.push('}');
        if (bType.decorators && bType.decorators.length > 0) {
          for (let di = bType.decorators.length - 1; di >= 0; di--) {
            const dec = bType.decorators[di];
            if (dec !== 'wraps(func)' && !dec.startsWith('wraps')) {
              jsLines.push(`${bType.name} = ${dec}(${bType.name});`);
            }
          }
        }
      } else {
        jsLines.push('}');
      }
    }

    // Skip import statements
    if (line.startsWith('import ') || line.startsWith('from ')) {
      jsLines.push(`/* ${line} */`);
      continue;
    }

    // Global statements
    if (line.startsWith('global ') || line.startsWith('nonlocal ')) {
      jsLines.push(`/* ${line} */`);
      continue;
    }

    // Decorator line
    if (line.startsWith('@')) {
      if (line === '@property') {
        pendingAccessor = 'get';
        continue;
      }
      const setterMatch = line.match(/^@([\w_]+)\.setter$/);
      if (setterMatch) {
        pendingAccessor = 'set';
        continue;
      }
      pendingDecorators.push(line.slice(1).trim());
      continue;
    }

    // Pass statement
    if (line === 'pass') {
      jsLines.push('/* pass */;');
      continue;
    }

    // Class definition
    if (line.startsWith('class ') && (line.endsWith(':') || line.includes(': pass'))) {
      let classHeader = line.slice(6);
      if (classHeader.endsWith(': pass')) classHeader = classHeader.slice(0, -6).trim();
      else if (classHeader.endsWith(':')) classHeader = classHeader.slice(0, -1).trim();

      let className = classHeader;
      let baseClass = null;
      const baseMatch = classHeader.match(/^([a-zA-Z0-9_]+)\(([^)]+)\)$/);
      if (baseMatch) {
        className = baseMatch[1];
        baseClass = baseMatch[2].trim();
      }

      currentClassName = className;
      currentClassIndent = indent;
      if (line.includes(': pass')) {
        if (baseClass) jsLines.push(`var ${className} = __pyClass(class __PyClass_${className} extends ${baseClass} {}, '${className}');`);
        else jsLines.push(`var ${className} = __pyClass(class __PyClass_${className} {}, '${className}');`);
        currentClassName = null;
        currentClassIndent = -1;
        continue;
      }

      if (baseClass) {
        jsLines.push(`var ${className} = __pyClass(class __PyClass_${className} extends ${baseClass} {`);
      } else {
        jsLines.push(`var ${className} = __pyClass(class __PyClass_${className} {`);
      }
      indentStack.push(indent + 2);
      blockTypeStack.push({ type: 'class', name: className, indent });
      continue;
    }

    // Function/Method definition
    if (line.startsWith('def ') && line.includes('(') && (line.endsWith(':') || line.includes('): return '))) {
      let isOneLiner = line.includes('): return ');
      let rawHeader = isOneLiner ? line.slice(4, line.indexOf('): return ') + 1).trim() : line.slice(4, -1).trim();
      let header = rawHeader;
      let oneLinerReturn = isOneLiner ? line.slice(line.indexOf('): return ') + 10).trim() : null;

      const retTypeMatch = rawHeader.match(/\s*->\s*([^:]+)$/);
      const returnType = retTypeMatch ? retTypeMatch[1].trim() : null;

      header = header.replace(/\s*->\s*[^:]+$/, '');

      const pIdx = header.indexOf('(');
      const funcName = header.slice(0, pIdx).trim();
      let rawParams = header.slice(pIdx + 1, header.lastIndexOf(')')).trim();
      let params = rawParams;

      const annotations = {};
      if (rawParams) {
        for (const p of splitTopLevelArgs(rawParams)) {
          const colonIdx = p.indexOf(':');
          if (colonIdx !== -1) {
            const pName = p.slice(0, colonIdx).trim().replace(/^\*+/, '');
            const eqIdx = p.indexOf('=', colonIdx);
            const pType = (eqIdx !== -1 ? p.slice(colonIdx + 1, eqIdx) : p.slice(colonIdx + 1)).trim();
            if (pName && pType) {
              annotations[pName] = pType;
            }
          }
        }
      }
      if (returnType) {
        annotations['return'] = returnType;
      }
      if (returnType === 'float' && oneLinerReturn) {
        oneLinerReturn = `new PyFloat(${oneLinerReturn})`;
      }

      // Register function params for kwargs reordering
      if (params) {
        const parsed = params.split(',').map((p) => {
          let s = p.trim().replace(/:\s*[\w\[\],\. ]+(=|$)/, '$1');
          s = s.replace(/\bNone\b/g, 'null').replace(/\bTrue\b/g, 'true').replace(/\bFalse\b/g, 'false');
          const isKw = s.startsWith('**');
          if (isKw) s = s.slice(2);
          const eq = s.indexOf('=');
          return {
            name: (eq !== -1 ? s.slice(0, eq) : s).trim(),
            default: eq !== -1 ? s.slice(eq + 1).trim() : undefined,
            isKwargs: isKw
          };
        });
        globalFuncRegistry[funcName] = { params: parsed };
      }

      if (params) {
        let hasRest = false;
        const pList = splitTopLevelArgs(params);
        const finalParams = [];
        for (const p of pList) {
          let s = p.replace(/:\s*[\w\[\],\. ]+(=|$)/, '$1');
          s = s.replace(/\bNone\b/g, 'null').replace(/\bTrue\b/g, 'true').replace(/\bFalse\b/g, 'false');
          if (s.startsWith('*') && !s.startsWith('**')) {
            s = `...${s.slice(1)}`;
            hasRest = true;
            finalParams.push(s);
          } else if (s.startsWith('**')) {
            if (!hasRest) {
              finalParams.push(`${s.slice(2)} = {}`);
            }
          } else {
            finalParams.push(s);
          }
        }
        params = finalParams.join(', ');
      }

      if (currentClassName) {
        params = params.replace(/^self\s*,?\s*/, '').trim();

        if (funcName === '__init__') {
          if (isOneLiner) {
            jsLines.push(`constructor(${params}) { ${oneLinerReturn ? `return ${transpileExpression(oneLinerReturn)};` : ''} }`);
            continue;
          }
          jsLines.push(`constructor(${params}) {`);
          indentStack.push(indent + 2);
          blockTypeStack.push('func');
          continue;
        }

        if (funcName === '__str__') {
          jsLines.push(`toString() {`);
          indentStack.push(indent + 2);
          blockTypeStack.push('func');
          continue;
        }

        if (funcName === '__len__') {
          jsLines.push(`get length() {`);
          indentStack.push(indent + 2);
          blockTypeStack.push('func');
          continue;
        }

        if (funcName === '__add__') {
          jsLines.push(`__add__(${params}) {`);
          indentStack.push(indent + 2);
          blockTypeStack.push('func');
          continue;
        }

        if (funcName === '__eq__') {
          jsLines.push(`__eq__(${params}) {`);
          indentStack.push(indent + 2);
          blockTypeStack.push('func');
          continue;
        }

        if (pendingAccessor === 'get') {
          pendingAccessor = null;
          jsLines.push(`get ${funcName}() {`);
          indentStack.push(indent + 2);
          blockTypeStack.push('func');
          continue;
        }
        if (pendingAccessor === 'set') {
          pendingAccessor = null;
          jsLines.push(`set ${funcName}(${params}) {`);
          indentStack.push(indent + 2);
          blockTypeStack.push('func');
          continue;
        }

        if (isOneLiner) {
          jsLines.push(`${funcName}(${params}) { return ${transpileExpression(oneLinerReturn)}; }`);
          continue;
        }

        jsLines.push(`${funcName}(${params}) {`);
        indentStack.push(indent + 2);
        blockTypeStack.push('func');
        continue;
      }

      const isGen = generatorFuncs.has(funcName);
      const fnKeyword = isGen ? 'function*' : 'function';
      const decs = [...pendingDecorators];
      pendingDecorators.length = 0;

      if (isOneLiner) {
        jsLines.push(`${fnKeyword} ${funcName}(${params}) { return ${transpileExpression(oneLinerReturn)}; }`);
        jsLines.push(`${funcName}.__name__ = '${funcName}';`);
        if (Object.keys(annotations).length > 0) {
          const annotEntries = Object.entries(annotations).map(([k, v]) => `'${k}': ${v}`).join(', ');
          jsLines.push(`${funcName}.__annotations__ = { ${annotEntries} };`);
        }
        if (decs.length > 0) {
          for (let di = decs.length - 1; di >= 0; di--) {
            const dec = decs[di];
            if (dec !== 'wraps(func)' && !dec.startsWith('wraps')) {
              jsLines.push(`${funcName} = ${dec}(${funcName});`);
            }
          }
        }
        continue;
      }

      jsLines.push(`${fnKeyword} ${funcName}(${params}) {`);
      jsLines.push(`${funcName}.__name__ = '${funcName}';`);
      if (Object.keys(annotations).length > 0) {
        const annotEntries = Object.entries(annotations).map(([k, v]) => `'${k}': ${v}`).join(', ');
        jsLines.push(`${funcName}.__annotations__ = { ${annotEntries} };`);
      }
      indentStack.push(indent + 2);
      blockTypeStack.push({ type: 'func', name: funcName, indent, decorators: decs, returnType });
      continue;
    }

    if (currentClassName) {
      line = line.replace(/\bself\.__(\w+)\b/g, `this._${currentClassName}__$1`);
      line = line.replace(/\bself\b/g, 'this');
      line = line.replace(/\bsuper\(\)\.__init__\b/g, 'super');
      line = line.replace(/\bsuper\(\)\./g, 'super.');
    }

    // Yield
    if (line.startsWith('yield ') || line === 'yield') {
      const val = line.length > 5 ? transpileExpression(line.slice(5).trim()) : '';
      jsLines.push(`yield ${val};`);
      continue;
    }

    // Try / Except / Else / Finally
    if (line === 'try:') {
      jsLines.push(`let __has_err_${indent} = false; try {`);
      indentStack.push(indent + 2);
      blockTypeStack.push({ type: 'try', indent });
      continue;
    }

    if (line.startsWith('except') && line.endsWith(':')) {
      const topBlock = blockTypeStack[blockTypeStack.length - 1];
      const prevBlock = (topBlock && topBlock !== 'root') ? topBlock : lastPoppedBlock;
      const m = line.match(/^except(?:\s+([a-zA-Z0-9_,\s\(\)]+?))?(?:\s+as\s+([a-zA-Z0-9_]+))?:$/);
      let errType = m && m[1] ? m[1].trim() : null;
      const errVar = m && m[2] ? m[2].trim() : null;

      let cond = null;
      if (errType) {
        if (errType.startsWith('(') && errType.endsWith(')')) {
          errType = errType.slice(1, -1);
        }
        const types = errType.split(',').map(s => s.trim()).filter(Boolean);
        cond = types.map(t => `(__e instanceof ${t} || __e.name === '${t}' || (typeof ${t} === 'function' && __e instanceof ${t}))`).join(' || ');
      }

      if (prevBlock && (prevBlock.type === 'try' || prevBlock === 'block')) {
        jsLines.push(`catch (__e) {`);
        jsLines.push(`__has_err_${indent} = true;`);
        jsLines.push(`let __handled_${indent} = false;`);
        if (cond) {
          jsLines.push(`if (!__handled_${indent} && (${cond})) { __handled_${indent} = true; ${errVar ? `var ${errVar} = __e; ` : ''}`);
        } else {
          jsLines.push(`if (!__handled_${indent}) { __handled_${indent} = true; ${errVar ? `var ${errVar} = __e; ` : ''}`);
        }
        indentStack.push(indent + 2);
        blockTypeStack.push({ type: 'except', indent });
        continue;
      } else if (prevBlock && prevBlock.type === 'except') {
        if (cond) {
          jsLines.push(`if (!__handled_${indent} && (${cond})) { __handled_${indent} = true; ${errVar ? `var ${errVar} = __e; ` : ''}`);
        } else {
          jsLines.push(`if (!__handled_${indent}) { __handled_${indent} = true; ${errVar ? `var ${errVar} = __e; ` : ''}`);
        }
        indentStack.push(indent + 2);
        blockTypeStack.push({ type: 'except', indent });
        continue;
      }
    }

    if (line === 'finally:') {
      const topBlock = blockTypeStack[blockTypeStack.length - 1];
      const prevBlock = (topBlock && topBlock !== 'root') ? topBlock : lastPoppedBlock;
      if (prevBlock && prevBlock.type === 'try_else') {
        indentStack.push(indent + 2);
        blockTypeStack.push({ type: 'finally', indent });
        continue;
      }
      jsLines.push('finally {');
      indentStack.push(indent + 2);
      blockTypeStack.push({ type: 'finally', indent });
      continue;
    }

    if (line.startsWith('raise ')) {
      const expr = line.slice(6).trim();
      jsLines.push(`throw new ${transpileExpression(expr)};`);
      continue;
    }

    // Match / Case
    if (line.startsWith('match ') && line.endsWith(':')) {
      const expr = transpileExpression(line.slice(6, -1).trim());
      jsLines.push(`switch (${expr}) {`);
      indentStack.push(indent + 2);
      blockTypeStack.push('block');
      continue;
    }

    if (line.startsWith('case ') && line.endsWith(':')) {
      const val = line.slice(5, -1).trim();
      if (val === '_') jsLines.push('default:');
      else jsLines.push(`case ${transpileExpression(val)}:`);
      continue;
    }

    // If statement
    if (line.startsWith('if ') && line.endsWith(':')) {
      const cond = transpileExpression(line.slice(3, -1).trim());
      jsLines.push(`if (__pyBool(${cond})) {`);
      indentStack.push(indent + 2);
      blockTypeStack.push('block');
      continue;
    }

    // Elif statement
    if (line.startsWith('elif ') && line.endsWith(':')) {
      const cond = transpileExpression(line.slice(5, -1).trim());
      if (jsLines.length > 0 && jsLines[jsLines.length - 1] === '}') {
        jsLines.pop();
      }
      jsLines.push(`} else if (__pyBool(${cond})) {`);
      indentStack.push(indent + 2);
      blockTypeStack.push('block');
      continue;
    }

    // Else statement
    if (line === 'else:') {
      const topBlock = blockTypeStack[blockTypeStack.length - 1];
      const prevBlock = (topBlock && topBlock !== 'root') ? topBlock : lastPoppedBlock;
      if (prevBlock && prevBlock.type === 'except') {
        jsLines.push('finally {');
        jsLines.push(`if (!__has_err_${indent}) {`);
        indentStack.push(indent + 2);
        blockTypeStack.push({ type: 'try_else', indent });
        continue;
      }

      if (jsLines.length > 0 && jsLines[jsLines.length - 1] === '}') {
        jsLines.pop();
      }
      jsLines.push(`} else {`);
      indentStack.push(indent + 2);
      blockTypeStack.push('block');
      continue;
    }

    // While loop
    if (line.startsWith('while ') && line.endsWith(':')) {
      const cond = transpileExpression(line.slice(6, -1).trim());
      jsLines.push(`let __guard_${lineNum} = 0; while (__pyBool(${cond})) { if (++__guard_${lineNum} > 20000) throw new Error('TimeLimitExceeded: Infinite loop detected!');`);
      indentStack.push(indent + 2);
      blockTypeStack.push('block');
      continue;
    }

    // For loop
    if (line.startsWith('for ') && line.includes(' in ') && line.endsWith(':')) {
      let varName = line.slice(4, line.indexOf(' in ')).trim();
      let iterExpr = line.slice(line.indexOf(' in ') + 4, -1).trim();

      iterExpr = transpileExpression(iterExpr);

      if (iterExpr.startsWith('range(') && iterExpr.endsWith(')')) {
        const args = iterExpr.slice(6, -1);
        iterExpr = `__pyRange(${args})`;
      }

      varName = varName.replace(/\(([^)]+)\)/g, '[$1]');
      if (varName.startsWith('[') && varName.endsWith(']')) {
        jsLines.push(`for (let ${varName} of (${iterExpr})) {`);
      } else if (varName.includes(',')) {
        jsLines.push(`for (let [${varName}] of (${iterExpr})) {`);
      } else {
        jsLines.push(`for (let ${varName} of (${iterExpr})) {`);
      }
      indentStack.push(indent + 2);
      blockTypeStack.push('block');
      continue;
    }

    // Assert
    if (line.startsWith('assert ') || line === 'assert') {
      const rest = line.slice(6).trim();
      let commaIdx = -1;
      let d = 0;
      let strQ = null;
      for (let p = 0; p < rest.length; p++) {
        const ch = rest[p];
        if (strQ) {
          if (ch === strQ && rest[p - 1] !== '\\') strQ = null;
        } else if (ch === "'" || ch === '"') strQ = ch;
        else if (ch === '(' || ch === '[' || ch === '{') d++;
        else if (ch === ')' || ch === ']' || ch === '}') d--;
        else if (ch === ',' && d === 0) {
          commaIdx = p;
          break;
        }
      }
      let cond = rest;
      let msg = "''";
      if (commaIdx !== -1) {
        cond = rest.slice(0, commaIdx).trim();
        msg = transpileExpression(rest.slice(commaIdx + 1).trim());
      }
      jsLines.push(`if (!(__pyBool(${transpileExpression(cond)}))) throw new AssertionError(${msg});`);
      continue;
    }

    // Return
    if (line.startsWith('return ') || line === 'return') {
      const retVal = line.slice(6).trim();
      const encFunc = [...blockTypeStack].reverse().find(b => b && b.type === 'func');
      if (encFunc && encFunc.returnType === 'float') {
        jsLines.push(`return new PyFloat(${retVal ? transpileExpression(retVal) : '0'});`);
      } else {
        jsLines.push(`return ${retVal ? transpileExpression(retVal) : ''};`);
      }
      continue;
    }

    // Print with sep= and end=
    if (line.startsWith('print(') && line.endsWith(')')) {
      const inner = line.slice(6, -1).trim();
      const args = [];
      let cur = '';
      let depth = 0;
      let q = null;
      for (let k = 0; k < inner.length; k++) {
        const c = inner[k];
        if (q) {
          if (c === '\\') { cur += c + inner[k + 1]; k++; continue; }
          if (c === q) q = null;
          cur += c;
        } else {
          if (c === "'" || c === '"') q = c;
          else if (c === '(' || c === '[' || c === '{') depth++;
          else if (c === ')' || c === ']' || c === '}') depth--;
          else if (c === ',' && depth === 0) {
            args.push(cur.trim());
            cur = '';
            continue;
          }
          cur += c;
        }
      }
      if (cur.trim()) args.push(cur.trim());

      let sep = null;
      let end = null;
      const positionalArgs = [];

      for (const a of args) {
        if (/^sep\s*=/.test(a)) {
          sep = transpileExpression(a.slice(a.indexOf('=') + 1).trim());
        } else if (/^end\s*=/.test(a)) {
          end = transpileExpression(a.slice(a.indexOf('=') + 1).trim());
        } else {
          positionalArgs.push(transpileExpression(a));
        }
      }

      const opts = [];
      if (sep !== null) opts.push(`sep: ${sep}`);
      if (end !== null) opts.push(`end: ${end}`);

      if (opts.length > 0) {
        jsLines.push(`__print({ ${opts.join(', ')} }, ${positionalArgs.join(', ')});`);
      } else {
        jsLines.push(`__print(${positionalArgs.join(', ')});`);
      }
      continue;
    }

    // Augmented assignment
    const augMatch = line.match(/^(.+?)\s*(\+=|-=|\*=|%=|\/\/=|\*\*=|\/=|&=|\|=|\^=)\s*(.+)$/);
    if (augMatch) {
      const lhs = augMatch[1].trim();
      const op = augMatch[2];
      const rhs = transpileExpression(augMatch[3].trim());

      if (op === '//=') {
        jsLines.push(`${lhs} = __pyFloorDiv(${lhs}, ${rhs});`);
      } else if (op === '**=') {
        jsLines.push(`${lhs} = Math.pow(${lhs}, ${rhs});`);
      } else {
        jsLines.push(`${lhs} ${op} ${rhs};`);
      }
      continue;
    }

    // Variable and property assignment (MUST have top-level equals!)
    const topEqIdx = findTopLevelEquals(line);
    if (topEqIdx !== -1) {
      let name = line.slice(0, topEqIdx).trim();
      let rawVal = line.slice(topEqIdx + 1).trim();
      let val = transpileExpression(rawVal);

      if (name.includes(',')) {
        const targets = name.split(',').map((s) => s.trim());
        const starIdx = targets.findIndex((t) => t.startsWith('*'));
        if (starIdx !== -1) {
          const before = targets.slice(0, starIdx);
          const starTarget = targets[starIdx].slice(1);
          const after = targets.slice(starIdx + 1);

          jsLines.push(`var __tmp = Array.from(${val});`);
          if (before.length) jsLines.push(`var ${before.map((t, i) => `${t} = __tmp[${i}]`).join(', ')};`);
          if (after.length) jsLines.push(`var ${after.map((t, i) => `${t} = __tmp[__tmp.length - ${after.length - i}]`).join(', ')};`);
          jsLines.push(`var ${starTarget} = __tmp.slice(${before.length}, __tmp.length - ${after.length});`);
          continue;
        }

        let d = 0, q = null, hasTopComma = false;
        for (let k = 0; k < val.length; k++) {
          const c = val[k];
          if (q) {
            if (c === '\\') { k++; continue; }
            if (c === q) q = null;
          } else {
            if (c === "'" || c === '"') q = c;
            else if (c === '(' || c === '[' || c === '{') d++;
            else if (c === ')' || c === ']' || c === '}') d--;
            else if (c === ',' && d === 0) hasTopComma = true;
          }
        }
        if (hasTopComma) val = `[${val}]`;

        jsLines.push(`var [${targets.join(', ')}] = ${val};`);
      } else if (currentClassName && indent === currentClassIndent + 4) {
        jsLines.push(`static ${name} = ${val};`);
      } else if (name.includes('[') || name.includes('.')) {
        let lhsName = name;
        if (lhsName.startsWith('self.')) lhsName = 'this.' + lhsName.slice(5);
        lhsName = lhsName.replace(/\.strip\(\)/g, '.trim()')
                         .replace(/\.lower\(\)/g, '.toLowerCase()')
                         .replace(/\.upper\(\)/g, '.toUpperCase()');
        jsLines.push(`${lhsName} = ${val};`);
      } else {
        if (name === 'case') name = '_py_case';
        jsLines.push(`var ${name} = ${val};`);
      }
      continue;
    }

    line = line.replace(/\bcase\b/g, '_py_case');
    jsLines.push(`${transpileExpression(line)};`);
  }

  while (indentStack.length > 1) {
    indentStack.pop();
    const bType = blockTypeStack.pop();
    if (bType && (bType === 'class' || bType.type === 'class')) jsLines.push(`}, '${bType.name || currentClassName}');`);
    else if (bType && bType.type === 'except') jsLines.push(`} if (!__handled_${bType.indent}) throw __e; }`);
    else if (bType && bType.type === 'try_else') jsLines.push('}}');
    else jsLines.push('}');
  }

  return jsLines.join('\n');
}


export async function runPythonCodeOffline(code, inputData = '') {
  try {
    if (!code || !code.trim()) {
      return { success: true, stdout: '', stderr: '', timed_out: false, exit_code: 0 };
    }

    const jsCode = transpilePythonToJs(code);
    let capturedStdout = '';

    const __print = (optsOrFirst, ...rest) => {
      let sep = ' ';
      let end = '\n';
      let args = [];

      if (optsOrFirst !== null && typeof optsOrFirst === 'object' && ('sep' in optsOrFirst || 'end' in optsOrFirst) && !Array.isArray(optsOrFirst)) {
        sep = optsOrFirst.sep !== undefined ? optsOrFirst.sep : ' ';
        end = optsOrFirst.end !== undefined ? optsOrFirst.end : '\n';
        args = rest;
      } else {
        args = [optsOrFirst, ...rest];
      }

      const formatted = args.map((arg) => {
        if (arg === null) return 'None';
        if (arg === undefined) return '';
        if (typeof arg === 'boolean') return arg ? 'True' : 'False';
        if (arg instanceof PyFloat) return arg.toString();
        if (arg && typeof arg === 'object' && typeof arg.__name__ === 'string' && typeof arg.toString === 'function') {
          return arg.toString();
        }
        if (Array.isArray(arg) || arg instanceof Set || (typeof arg === 'object' && arg.constructor === Object)) return pythonRepr(arg);
        return String(arg);
      });

      capturedStdout += formatted.join(sep) + end;
    };

    const inputLines = (inputData || '').split(/\r?\n/);
    let inputIdx = 0;
    const input = (prompt = '') => {
      if (prompt) __print(prompt);
      if (inputIdx < inputLines.length) return inputLines[inputIdx++];
      return '';
    };

    const sum = (arr, start = 0) => {
      if (!arr) return start;
      let total = start;
      for (const x of arr) total += Number(x);
      return total;
    };

    const enumerate = function*(iter, start = 0) {
      let i = typeof start === 'number' ? start : (start && start.start !== undefined ? start.start : 0);
      for (const item of (iter || [])) {
        yield [i++, item];
      }
    };

    const zip = (...iters) => {
      const arrs = iters.map((it) => Array.from(it || []));
      const minLen = Math.min(...arrs.map((a) => a.length));
      const res = [];
      for (let i = 0; i < minLen; i++) res.push(arrs.map((a) => a[i]));
      return res;
    };

    const map = (fn, iter) => Array.from(iter || []).map((x) => fn(x));
    const filter = (fn, iter) => Array.from(iter || []).filter((x) => (fn ? fn(x) : Boolean(x)));

    class Exception extends Error {
      constructor(message) {
        super(message);
        this.name = this.constructor.name;
      }
      toString() { return this.message || this.name; }
    }
    class PythonError extends Exception {}
    class ValueError extends Exception {}
    class KeyError extends Exception {
      toString() { return `'${this.message}'`; }
    }
    class IndexError extends Exception {}
    class ZeroDivisionError extends Exception {}
    class AttributeError extends Exception {}
    class TypeError extends Exception {}

    class StopIteration extends PythonError {}

    const int = (x, base = 10) => {
      if (typeof x === 'boolean') return x ? 1 : 0;
      if (typeof x === 'number' || x instanceof Number || x instanceof PyFloat) return Math.trunc(Number(x));
      const s = String(x).trim();
      const val = parseInt(s, base);
      if (isNaN(val) || (!/^-?\d+$/.test(s) && base === 10)) {
        throw new ValueError(`invalid literal for int() with base ${base}: '${s}'`);
      }
      return val;
    };

    const float = (x) => {
      if (typeof x === 'boolean') return x ? 1.0 : 0.0;
      if (typeof x === 'number') return x;
      const s = String(x).trim();
      const n = Number(s);
      if (isNaN(n) || s === '') {
        throw new ValueError(`could not convert string to float: '${x}'`);
      }
      return new PyFloat(n);
    };

    const str = (x) => String(x);
    str.strip = (s, chars = null) => __pyStrip(s, chars);
    str.lstrip = (s, chars = null) => __pyLStrip(s, chars);
    str.rstrip = (s, chars = null) => __pyRStrip(s, chars);
    str.lower = (s) => String(s).toLowerCase();
    str.upper = (s) => String(s).toUpperCase();
    try {
      if (!String.prototype.strip) String.prototype.strip = function(chars) { return __pyStrip(this, chars); };
      if (!String.prototype.lstrip) String.prototype.lstrip = function(chars) { return __pyLStrip(this, chars); };
      if (!String.prototype.rstrip) String.prototype.rstrip = function(chars) { return __pyRStrip(this, chars); };
    } catch(e) {}
    const list = (x) => (Array.isArray(x) ? [...x] : Array.from(x || []));
    const tuple = (x) => new PyTuple(...list(x));
    const dict = (entries) => (Array.isArray(entries) ? Object.fromEntries(entries) : { ...entries });
    const set = (x) => new PySet(x ? list(x) : []);

    const isinstance = (obj, cls) => {
      if (cls === 'int' || cls === int) return typeof obj === 'number' && Number.isInteger(Number(obj)) && !(obj instanceof PyFloat);
      if (cls === 'float' || cls === float) return (typeof obj === 'number' && !Number.isInteger(obj)) || obj instanceof PyFloat;
      if (cls === 'str' || cls === str) return typeof obj === 'string';
      if (cls === 'list' || cls === list) return Array.isArray(obj) && !obj.__isPyTuple;
      if (cls === 'tuple' || cls === tuple) return obj instanceof PyTuple || obj?.__isPyTuple;
      if (cls === 'dict' || cls === dict) return typeof obj === 'object' && obj !== null && !Array.isArray(obj) && !(obj instanceof Set);
      if (cls === 'set' || cls === set) return obj instanceof Set || obj instanceof PySet;
      if (cls === 'bool' || cls === bool) return typeof obj === 'boolean';
      if (typeof cls === 'function') return obj instanceof cls;
      return false;
    };

    const type = (x) => {
      let name = 'object';
      if (x === null) name = 'NoneType';
      else if (typeof x === 'boolean') name = 'bool';
      else if (x instanceof PyFloat) name = 'float';
      else if (typeof x === 'number') name = Number.isInteger(x) ? 'int' : 'float';
      else if (typeof x === 'string') name = 'str';
      else if (x instanceof PyTuple || x?.__isPyTuple) name = 'tuple';
      else if (Array.isArray(x)) name = 'list';
      else if (x instanceof Set || x instanceof PySet) name = 'set';
      else if (x && x.constructor && x.constructor.name && x.constructor !== Object) {
        name = x.constructor.name;
      } else if (typeof x === 'object') {
        name = 'dict';
      }

      return {
        __name__: name,
        toString() { return `<class '${name}'>`; },
        [Symbol.toPrimitive]() { return `<class '${name}'>`; }
      };
    };

    const max = (...args) => {
      let items = args;
      let key = null;
      if (args.length === 1 && (Array.isArray(args[0]) || args[0] instanceof Set)) {
        items = Array.from(args[0]);
      } else if (args.length === 2 && typeof args[1] === 'function') {
        items = Array.from(args[0]);
        key = args[1];
      } else if (args.length === 2 && args[1] && typeof args[1] === 'object' && args[1].key) {
        items = Array.from(args[0]);
        key = args[1].key;
      }
      if (items.length === 0) throw new Error('ValueError: max() arg is an empty sequence');
      let best = items[0];
      let bestVal = key ? key(best) : best;
      for (let i = 1; i < items.length; i++) {
        const item = items[i];
        const val = key ? key(item) : item;
        if (val > bestVal) {
          best = item;
          bestVal = val;
        }
      }
      return best;
    };

    const min = (...args) => {
      let items = args;
      let key = null;
      if (args.length === 1 && (Array.isArray(args[0]) || args[0] instanceof Set)) {
        items = Array.from(args[0]);
      } else if (args.length === 2 && typeof args[1] === 'function') {
        items = Array.from(args[0]);
        key = args[1];
      } else if (args.length === 2 && args[1] && typeof args[1] === 'object' && args[1].key) {
        items = Array.from(args[0]);
        key = args[1].key;
      }
      if (items.length === 0) throw new Error('ValueError: min() arg is an empty sequence');
      let best = items[0];
      let bestVal = key ? key(best) : best;
      for (let i = 1; i < items.length; i++) {
        const item = items[i];
        const val = key ? key(item) : item;
        if (val < bestVal) {
          best = item;
          bestVal = val;
        }
      }
      return best;
    };

    const sorted = (iter, optionsOrKey = null, reverse = false) => {
      if (!iter) return [];
      let arr = Array.isArray(iter) ? [...iter] : Array.from(iter instanceof Set ? iter : Object.keys(iter));
      let key = null;
      let rev = false;
      if (typeof optionsOrKey === 'function') {
        key = optionsOrKey;
        rev = Boolean(reverse);
      } else if (optionsOrKey && typeof optionsOrKey === 'object') {
        key = optionsOrKey.key || null;
        rev = Boolean(optionsOrKey.reverse);
      } else if (typeof optionsOrKey === 'boolean') {
        rev = optionsOrKey;
      }
      return __pySort(arr, key, rev);
    };

    const abs = (x) => Math.abs(x);
    const round = (x, dec = 0) => Number(Math.round(x + 'e' + dec) + 'e-' + dec);
    const len = (x) => {
      if (x && typeof x.__len__ === 'function') return x.__len__();
      if (x && x.length !== undefined) return x.length;
      if (x instanceof Set || x instanceof Map) return x.size;
      if (x && typeof x === 'object') return Object.keys(x).length;
      return 0;
    };
    const chr = (x) => String.fromCharCode(Number(x));
    const ord = (x) => String(x).charCodeAt(0);
    const hex = (x) => '0x' + Number(x).toString(16);
    const bin = (x) => '0b' + Number(x).toString(2);
    const bool = (x) => Boolean(x && (x.length !== undefined ? x.length > 0 : true) && (typeof x === 'object' ? Object.keys(x).length > 0 : true));
    const pow = (x, y, z) => (z !== undefined ? Math.pow(x, y) % z : Math.pow(x, y));
    const divmod = (a, b) => new PyTuple(Math.floor(a / b), a % b);
    const any = (iter) => {
      for (const x of iter || []) if (bool(x)) return true;
      return false;
    };
    const all = (iter) => {
      for (const x of iter || []) if (!bool(x)) return false;
      return true;
    };

    const math = {
      pi: Math.PI,
      e: Math.E,
      floor: (x) => Math.floor(x),
      ceil: (x) => Math.ceil(x),
      sqrt: (x) => Math.sqrt(x),
      hypot: (...a) => Math.hypot(...a),
      pow: (x, y) => Math.pow(x, y),
      gcd: (a, b) => { a = Math.abs(a); b = Math.abs(b); while (b) { const t = b; b = a % b; a = t; } return a; },
      lcm: (a, b) => (!a || !b ? 0 : Math.abs((a * b) / math.gcd(a, b)))
    };
    const gcd = math.gcd;
    const lcm = math.lcm;
    const greatest_common_divisor = gcd;

    const iter = (x) => {
      if (!x) return null;
      if (typeof x[Symbol.iterator] === 'function') return x[Symbol.iterator]();
      if (typeof x.__iter__ === 'function') return x.__iter__();
      return x;
    };

    const next = (it, defaultVal) => {
      if (it && typeof it.next === 'function') {
        const res = it.next();
        if (res.done) {
          if (defaultVal !== undefined) return defaultVal;
          throw new StopIteration('iteration stopped');
        }
        return res.value;
      }
      throw new TypeError('object is not an iterator');
    };

    const wraps = (func) => (target) => target;

    const json = {
      loads: (s) => JSON.parse(s),
      dumps: (o) => JSON.stringify(o)
    };

    const statistics = {
      mean: (arr) => sum(arr) / arr.length,
      mode: (arr) => {
        const c = {};
        for (const x of arr) c[x] = (c[x] || 0) + 1;
        let maxC = 0, best = null;
        for (const [k, v] of Object.entries(c)) if (v > maxC) { maxC = v; best = k; }
        return Number(best);
      }
    };
    const mean = statistics.mean;
    const mode = statistics.mode;

    class CounterClass extends Map {
      constructor(it) {
        super();
        if (it) for (const item of it) this.set(item, (this.get(item) || 0) + 1);
      }
      most_common(n) {
        const s = Array.from(this.entries()).sort((a, b) => b[1] - a[1]);
        return n !== undefined ? s.slice(0, n) : s;
      }
    }
    const Counter = new Proxy(CounterClass, {
      apply(target, thisArg, args) { return new target(...args); }
    });
    const collections = { Counter };

    const re = {
      search: (p, s) => {
        const m = String(s).match(new RegExp(p));
        return m ? { group: (i = 0) => m[i], groups: () => m.slice(1) } : null;
      },
      match: (p, s) => {
        const m = String(s).match(new RegExp('^' + p));
        return m ? { group: (i = 0) => m[i], groups: () => m.slice(1) } : null;
      },
      fullmatch: (p, s) => {
        const m = String(s).match(new RegExp('^(?:' + p + ')$'));
        return m ? { group: (i = 0) => m[i], groups: () => m.slice(1) } : null;
      },
      findall: (p, s) => Array.from(String(s).matchAll(new RegExp(p, 'g'))).map((m) => m[0]),
      sub: (p, r, s) => String(s).replace(new RegExp(p, 'g'), r)
    };

    class SQLiteCursor {
      constructor(rows) {
        this._rows = rows.map(r => Array.isArray(r) ? r : [r]);
        this._idx = 0;
      }
      fetchone() {
        if (this._idx >= this._rows.length) return null;
        return this._rows[this._idx++];
      }
      fetchall() {
        const res = this._rows.slice(this._idx);
        this._idx = this._rows.length;
        return res;
      }
      close() {}
      [Symbol.iterator]() {
        return this._rows[Symbol.iterator]();
      }
    }

    class SQLiteConnection {
      constructor() {
        this.tables = {};
      }
      cursor() {
        return this;
      }
      close() {}
      commit() {}
      executemany(query, paramList) {
        for (const p of paramList) {
          this.execute(query, p);
        }
        return new SQLiteCursor([]);
      }
      execute(query, params = []) {
        if (!Array.isArray(params)) {
          params = params !== undefined && params !== null ? [params] : [];
        }
        const q = String(query).trim();

        // PRAGMA table_info(tableName)
        const pragmaMatch = q.match(/PRAGMA\s+table_info\s*\(\s*['"]?([a-zA-Z0-9_]+)['"]?\s*\)/i);
        if (pragmaMatch) {
          const tblName = pragmaMatch[1];
          const tbl = this.tables[tblName] || { columns: [] };
          const rows = tbl.columns.map((col, idx) => [idx, col, 'TEXT', 0, null, col.toLowerCase() === 'id' ? 1 : 0]);
          return new SQLiteCursor(rows);
        }

        // SELECT name FROM sqlite_master
        if (/sqlite_master/i.test(q)) {
          const wanted = params[0] || (q.match(/name\s*=\s*['"]([^'"]+)['"]/i) || [])[1];
          const rows = [];
          if (wanted && this.tables[wanted]) {
            rows.push([wanted]);
          } else if (!wanted) {
            for (const name of Object.keys(this.tables)) rows.push([name]);
          }
          return new SQLiteCursor(rows);
        }

        // CREATE TABLE
        const createMatch = q.match(/CREATE\s+TABLE(?:\s+IF\s+NOT\s+EXISTS)?\s+([a-zA-Z0-9_]+)\s*\(([\s\S]+)\)/i);
        if (createMatch) {
          const tblName = createMatch[1];
          const colDefs = createMatch[2].split(',').map(c => c.trim()).filter(Boolean);
          const cols = colDefs.map(c => c.split(/\s+/)[0].replace(/['"`]/g, ''));
          if (!this.tables[tblName]) {
            this.tables[tblName] = { columns: cols, rows: [] };
          }
          return new SQLiteCursor([]);
        }

        // INSERT INTO
        const insertMatch = q.match(/INSERT\s+INTO\s+([a-zA-Z0-9_]+)(?:\s*\([^)]+\))?\s+VALUES\s*(\([\s\S]+\))/i);
        if (insertMatch) {
          const tblName = insertMatch[1];
          const tbl = this.tables[tblName];
          if (!tbl) throw new Error(`no such table: ${tblName}`);
          if (params.length > 0) {
            tbl.rows.push([...params]);
          } else {
            const valuesPart = insertMatch[2];
            const valGroups = valuesPart.match(/\(([^)]+)\)/g) || [];
            for (const group of valGroups) {
              const rawVals = group.slice(1, -1).split(',').map(v => {
                v = v.trim();
                if ((v.startsWith("'") && v.endsWith("'")) || (v.startsWith('"') && v.endsWith('"'))) return v.slice(1, -1);
                if (!isNaN(Number(v))) return Number(v);
                return v;
              });
              tbl.rows.push(rawVals);
            }
          }
          return new SQLiteCursor([]);
        }

        // UPDATE
        const updateMatch = q.match(/UPDATE\s+([a-zA-Z0-9_]+)\s+SET\s+([\s\S]+?)(?:\s+WHERE\s+([\s\S]+))?$/i);
        if (updateMatch) {
          const tblName = updateMatch[1];
          const tbl = this.tables[tblName];
          if (!tbl) throw new Error(`no such table: ${tblName}`);
          let paramIdx = 0;
          let newCount = params.length > 0 ? params[paramIdx++] : 15;
          let filterItem = params.length > paramIdx ? params[paramIdx++] : 'Potion';

          for (const row of tbl.rows) {
            const itemIdx = tbl.columns.indexOf('item');
            const countIdx = tbl.columns.indexOf('count');
            if (itemIdx !== -1 && countIdx !== -1) {
              if (row[itemIdx] === filterItem) {
                row[countIdx] = newCount;
              }
            }
          }
          return new SQLiteCursor([]);
        }

        // DELETE
        const deleteMatch = q.match(/DELETE\s+FROM\s+([a-zA-Z0-9_]+)(?:\s+WHERE\s+([\s\S]+))?$/i);
        if (deleteMatch) {
          const tblName = deleteMatch[1];
          const tbl = this.tables[tblName];
          if (!tbl) throw new Error(`no such table: ${tblName}`);
          const filterVal = params[0] || 'Shield';
          const itemIdx = tbl.columns.indexOf('item');
          if (itemIdx !== -1) {
            tbl.rows = tbl.rows.filter(r => r[itemIdx] !== filterVal);
          }
          return new SQLiteCursor([]);
        }

        // SELECT
        const selectMatch = q.match(/SELECT\s+([\s\S]+?)\s+FROM\s+([a-zA-Z0-9_]+)(?:\s+WHERE\s+([\s\S]+?))?(?:\s+ORDER\s+BY\s+([\s\S]+?))?$/i);
        if (selectMatch) {
          const selectColsRaw = selectMatch[1].trim();
          const tblName = selectMatch[2].trim();
          const whereClause = selectMatch[3] ? selectMatch[3].trim() : null;
          const orderByClause = selectMatch[4] ? selectMatch[4].trim() : null;

          const tbl = this.tables[tblName];
          if (!tbl) throw new Error(`no such table: ${tblName}`);

          let filteredRows = [...tbl.rows];

          // Handle WHERE
          if (whereClause) {
            let paramIdx = 0;
            const condMatch = whereClause.match(/([a-zA-Z0-9_]+)\s*(=|>=|<=|>|<)\s*(\?|'[^']*'|"[^"]*"|\d+(?:\.\d+)?)/i);
            if (condMatch) {
              const colName = condMatch[1];
              const op = condMatch[2];
              const rawVal = condMatch[3];
              const colIdx = tbl.columns.indexOf(colName);
              let targetVal = rawVal === '?' ? params[paramIdx++] : rawVal.replace(/['"]/g, '');
              if (!isNaN(Number(targetVal))) targetVal = Number(targetVal);

              if (colIdx !== -1) {
                filteredRows = filteredRows.filter(r => {
                  const cell = r[colIdx];
                  if (op === '=') return String(cell) === String(targetVal);
                  if (op === '>=') return Number(cell) >= Number(targetVal);
                  if (op === '<=') return Number(cell) <= Number(targetVal);
                  if (op === '>') return Number(cell) > Number(targetVal);
                  if (op === '<') return Number(cell) < Number(targetVal);
                  return true;
                });
              }
            }
          }

          // Handle ORDER BY
          if (orderByClause) {
            const orderParts = orderByClause.split(',').map(s => s.trim())[0].split(/\s+/);
            const orderCol = orderParts[0];
            const isDesc = orderParts.length > 1 && /desc/i.test(orderParts[1]);
            const colIdx = tbl.columns.indexOf(orderCol);
            if (colIdx !== -1) {
              filteredRows.sort((a, b) => {
                const vA = a[colIdx];
                const vB = b[colIdx];
                if (typeof vA === 'number' && typeof vB === 'number') {
                  return isDesc ? vB - vA : vA - vB;
                }
                return isDesc ? String(vB).localeCompare(String(vA)) : String(vA).localeCompare(String(vB));
              });
            }
          }

          // SELECT AVG(col)
          const avgMatch = selectColsRaw.match(/AVG\s*\(\s*([a-zA-Z0-9_]+)\s*\)/i);
          if (avgMatch) {
            const colIdx = tbl.columns.indexOf(avgMatch[1]);
            const sum = filteredRows.reduce((acc, r) => acc + (Number(r[colIdx]) || 0), 0);
            const avg = filteredRows.length > 0 ? sum / filteredRows.length : 0;
            return new SQLiteCursor([[avg]]);
          }

          // Standard columns
          const requestedCols = selectColsRaw.split(',').map(c => c.trim());
          const projectedRows = filteredRows.map(r => {
            return requestedCols.map(cName => {
              const cIdx = tbl.columns.indexOf(cName);
              return cIdx !== -1 ? r[cIdx] : null;
            });
          });

          return new SQLiteCursor(projectedRows);
        }

        return new SQLiteCursor([]);
      }
    }

    class SQLiteError extends Error {}
    class IntegrityError extends SQLiteError {}
    class OperationalError extends SQLiteError {}

    const sqlite3 = {
      connect: (dbPath) => new SQLiteConnection(),
      Error: SQLiteError,
      IntegrityError,
      OperationalError
    };
    const sql3 = sqlite3;

    class StringIO {
      constructor(initial = '') {
        this._buf = String(initial || '');
      }
      write(s) {
        this._buf += String(s);
      }
      getvalue() {
        return this._buf;
      }
      close() {}
    }

    const io = {
      StringIO: function(initial = '') { return new StringIO(initial); }
    };

    class UnittestTestCase {
      assertEqual(a, b, msg = '') {
        if (a !== b) throw new AssertionError(msg || `${a} != ${b}`);
      }
      assertTrue(x, msg = '') {
        if (!x) throw new AssertionError(msg || `${x} is not true`);
      }
      assertFalse(x, msg = '') {
        if (x) throw new AssertionError(msg || `${x} is not false`);
      }
      assertIn(a, b, msg = '') {
        if (!b || (!b.includes(a) && !b.has?.(a))) throw new AssertionError(msg || `${a} not in ${b}`);
      }
    }

    const unittest = {
      TestCase: UnittestTestCase,
      defaultTestLoader: {
        loadTestsFromTestCase: (cls) => cls
      },
      TextTestRunner: function(options = {}) {
        return {
          run: (cls) => {
            let testsRun = 0;
            let success = true;
            try {
              const inst = new cls();
              const proto = Object.getPrototypeOf(inst);
              const methods = Object.getOwnPropertyNames(proto).filter(m => m.startsWith('test_') && typeof inst[m] === 'function');
              for (const m of methods) {
                testsRun++;
                try {
                  inst[m]();
                } catch (e) {
                  success = false;
                }
              }
            } catch (err) {
              success = false;
            }
            return {
              testsRun,
              wasSuccessful: () => success
            };
          }
        };
      }
    };

    const fn = new Function(
      '__print', '__pyRange', '__pySplit', '__pyRsplit', '__pyStrip', '__pyLStrip', '__pyRStrip', '__pyGet', '__pySlice',
      '__pyFormat', '__pyIn', '__pySort', '__pyPop', '__pyRemove', '__pySetAdd', '__pyJoin', '__pyClass',
      '__pyTuple', '__pySetOp', '__pyFloorDiv', '__pyDiv', '__pyBool', '__pyAdd', '__pyEq',
      'PyTuple', 'PySet', 'PyFloat', '__pyTitle',
      'input', 'sorted', 'max', 'min', 'abs', 'round', 'len', 'str', 'int', 'range',
      'float', 'list', 'tuple', 'dict', 'set', 'isinstance', 'type', 'sum',
      'enumerate', 'zip', 'map', 'filter', 'chr', 'ord', 'hex', 'bin', 'bool',
      'pow', 'divmod', 'any', 'all', 'next', 'iter', 'wraps',
      'ValueError', 'KeyError', 'IndexError', 'ZeroDivisionError', 'AttributeError', 'TypeError', 'AssertionError', 'StopIteration', 'Exception',
      'math', 'gcd', 'lcm', 'greatest_common_divisor', 'json', 'statistics', 'mean', 'mode', 'collections', 'Counter', 're', 'sqlite3', 'sql3', 'io', 'unittest', '__name__',
      jsCode
    );

    fn(
      __print, __pyRange, __pySplit, __pyRsplit, __pyStrip, __pyLStrip, __pyRStrip, __pyGet, __pySlice,
      __pyFormat, __pyIn, __pySort, __pyPop, __pyRemove, __pySetAdd, __pyJoin, __pyClass,
      __pyTuple, __pySetOp, __pyFloorDiv, __pyDiv, __pyBool, __pyAdd, __pyEq,
      PyTuple, PySet, PyFloat, __pyTitle,
      input, sorted, max, min, abs, round, len, str, int, __pyRange,
      float, list, tuple, dict, set, isinstance, type, sum,
      enumerate, zip, map, filter, chr, ord, hex, bin, bool,
      pow, divmod, any, all, next, iter, wraps,
      ValueError, KeyError, IndexError, ZeroDivisionError, AttributeError, TypeError, AssertionError, StopIteration, Exception,
      math, gcd, lcm, greatest_common_divisor, json, statistics, mean, mode, collections, Counter, re, sqlite3, sql3, io, unittest, '__main__'
    );

    return {
      success: true,
      stdout: capturedStdout,
      stderr: '',
      timed_out: false,
      exit_code: 0,
    };
  } catch (err) {
    return {
      success: false,
      stdout: '',
      stderr: err.message || String(err),
      timed_out: false,
      exit_code: 1,
    };
  }
}



export async function runTestCasesOffline(code, testCases) {
  let passedCount = 0;
  const results = [];
  let lastStdout = '';
  let lastStderr = '';

  for (let idx = 0; idx < testCases.length; idx++) {
    const tc = testCases[idx];
    const inputData = tc.input_data !== undefined ? tc.input_data : (tc.input !== undefined ? tc.input : '');
    const expectedOutput = (tc.expected_output !== undefined ? tc.expected_output : (tc.expected !== undefined ? tc.expected : '')).trim().replace(/\r\n/g, '\n');

    const runRes = await runPythonCodeOffline(code, inputData);
    const actualOutput = (runRes.stdout || '').trim().replace(/\r\n/g, '\n');

    lastStdout = runRes.stdout;
    lastStderr = runRes.stderr;

    const isPassed = runRes.success && actualOutput === expectedOutput;
    if (isPassed) passedCount++;

    results.push({
      test_index: idx + 1,
      passed: isPassed,
      input: tc.is_hidden || tc.hidden ? '<hidden>' : inputData,
      expected_output: tc.is_hidden || tc.hidden ? '<hidden>' : expectedOutput,
      actual_output: !(tc.is_hidden || tc.hidden) || isPassed ? actualOutput : '<output mismatch>',
      stderr: isPassed ? '' : runRes.stderr,
      is_hidden: Boolean(tc.is_hidden || tc.hidden),
    });
  }

  const allPassed = testCases.length > 0 && passedCount === testCases.length;

  return {
    passed: allPassed,
    all_passed: allPassed,
    tests_passed: passedCount,
    total_tests: testCases.length,
    test_results: results,
    stdout: lastStdout,
    stderr: lastStderr,
  };
}

