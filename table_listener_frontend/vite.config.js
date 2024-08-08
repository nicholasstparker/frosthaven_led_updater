import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import path from 'path';
import cleanPlugin from "vite-plugin-clean";

// https://vitejs.dev/config/
export default defineConfig({
  root: path.resolve(__dirname, 'src'),
    build: {
    outDir: '../dist'
  },

  resolve: {
    alias: {
      '~bootstrap': path.resolve(__dirname, 'node_modules/bootstrap'),
    }
  },
  server: {
    port: 8080,
    hot: true
  },
  plugins: [react(),
    cleanPlugin({
      targets: ['../dist'],
    })
  ]
});
