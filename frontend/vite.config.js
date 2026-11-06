import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { spawn } from 'node:child_process'
import { fileURLToPath } from 'node:url'
import { resolve } from 'node:path'

const previewRunner = resolve(fileURLToPath(new URL('.', import.meta.url)), '../backend/live_preview_runner.py')

function localPythonExecutionPlugin() {
  const handleCodeRequest = (req, res, next) => {
    const pathname = (req.url || '').split('?')[0]
    const action = pathname === '/api/code/execute'
      ? 'execute'
      : pathname === '/api/code/submit'
        ? 'submit'
        : null

    if (!action) return next()
    if (req.method !== 'POST') {
      res.statusCode = 405
      res.setHeader('Allow', 'POST')
      res.end(JSON.stringify({ error: 'POST is required for code actions.' }))
      return
    }

    // The live preview is available to localhost only; do not expose this
    // development execution adapter to other devices on the LAN.
    const host = String(req.headers.host || '').split(':')[0].toLowerCase()
    if (host !== 'localhost' && host !== '127.0.0.1') {
      res.statusCode = 403
      res.end(JSON.stringify({ error: 'Code execution is available from this computer only.' }))
      return
    }

    let body = ''
    req.setEncoding('utf8')
    req.on('data', (chunk) => {
      body += chunk
      if (body.length > 1_000_000) req.destroy()
    })
    req.on('end', () => {
      let data
      try {
        data = JSON.parse(body || '{}')
      } catch {
        res.statusCode = 400
        res.setHeader('Content-Type', 'application/json')
        res.end(JSON.stringify({ error: 'Request body must be valid JSON.' }))
        return
      }

      const runner = spawn(process.env.PYTHON_EXECUTABLE || 'python', [previewRunner], {
        windowsHide: true,
        stdio: ['pipe', 'pipe', 'pipe'],
      })
      let stdout = ''
      let stderr = ''
      let finished = false
      const finish = (status, payload) => {
        if (finished) return
        finished = true
        clearTimeout(timer)
        res.statusCode = status
        res.setHeader('Content-Type', 'application/json; charset=utf-8')
        res.setHeader('Cache-Control', 'no-store')
        res.end(JSON.stringify(payload))
      }
      const timer = setTimeout(() => {
        runner.kill()
        finish(504, { error: 'The local Python execution service timed out.' })
      }, 20_000)

      runner.stdout.setEncoding('utf8')
      runner.stderr.setEncoding('utf8')
      runner.stdout.on('data', (chunk) => { stdout += chunk })
      runner.stderr.on('data', (chunk) => { stderr += chunk })
      runner.on('error', (error) => {
        finish(503, { error: `Could not start Python: ${error.message}` })
      })
      runner.on('close', (exitCode) => {
        if (finished) return
        try {
          const result = JSON.parse(stdout)
          finish(result.status || 200, result.body || {})
        } catch {
          finish(500, { error: stderr.trim() || `Python runner exited with code ${exitCode}.` })
        }
      })
      runner.stdin.end(JSON.stringify({ action, data }))
    })
  }

  return {
    name: 'python-quest-local-execution',
    configureServer(server) {
      server.middlewares.use(handleCodeRequest)
    },
    configurePreviewServer(server) {
      server.middlewares.use(handleCodeRequest)
    },
  }
}

// https://vite.dev/config/
export default defineConfig({
  plugins: [react(), localPythonExecutionPlugin()],
  server: {
    host: '0.0.0.0',
    port: 5173,
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:5000',
        changeOrigin: true,
      }
    }
  },
  preview: {
    host: '0.0.0.0',
    port: 4173,
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:5000',
        changeOrigin: true,
      }
    }
  }
})
