import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import compression from 'vite-plugin-compression'

export default defineConfig({
    plugins: [
        react(),
        compression({
            algorithm: 'brotliCompress',
            ext: '.br',
            threshold: 1024,
            deleteOriginFile: false,
        }),
        compression({
            algorithm: 'gzip',
            ext: '.gz',
            threshold: 1024,
            deleteOriginFile: false,
        })
    ],
    server: {
        host: 'localhost',
        port: 5000,
        // headers: {
        //     'Content-Security-Policy': "default-src 'self' https://raw.githubusercontent.com;" +
        //         " script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data: https: blob:;"
        // }
    },
    build: {
        target: 'esnext',
        minify: 'esbuild',
        cssMinify: true,
        sourcemap: false,
        rollupOptions: {
            output: {
                manualChunks: {
                    react: ['react', 'react-dom'],
                    motion: ['framer-motion'],
                    markdown: ['react-markdown', 'remark-gfm']
                }
            }
        }
    }
})
