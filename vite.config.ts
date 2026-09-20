import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import tailwindcss from '@tailwindcss/vite';
export default defineConfig(({ mode }) => ({
  base: mode === 'github-pages' ? '/Portfolio-Nikky/' : '/',
  plugins: [react(), tailwindcss()],
  build: { rollupOptions: { output: { manualChunks: { three: ['three'], motion: ['framer-motion'] } } } },
}));
