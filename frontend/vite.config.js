import { defineConfig } from 'vite'

export default defineConfig({
  server: {
    host: '0.0.0.0',  
    port: 5173,        
    hmr: {
      clientPort: 5173,
    }, 
    watch: {
    usePolling: true,
    }
  },
  optimizeDeps: {
    include: [
      'react',        
      'react-dom'
    ]
  },
  base: '/',
});

