import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'
import path from 'path'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react(),tailwindcss()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "./src"),
    },
  },
  server:{
    host: '0.0.0.0',
    port: 5678, // 前端端口
    allowedHosts: [
      '2f2fa3c1.r6.cpolar.cn',
      'localhost',
      '127.0.0.1',
      '172.29.80.64'
    ],
    proxy:{
      '/api': {
        target: 'http://localhost:5050', // 后端实际端口
        // target: 'http://47.93.189.200:5050', // 直接使用公网IP
        changeOrigin: true,
        // 添加安全配置
        secure: false,
        ws: true,
      },
    },
  },
})
