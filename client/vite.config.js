import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    proxy: {
      //All API cals to /api will proxy to Flask on port 5000
      '/api' : {
          target: 'https://localhost:5000',
          changeOrigin: true,
      },
    },
  },
})
