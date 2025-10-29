import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { SpeedInsights } from "@vercel/speed-insights/react";
import App from './App.jsx'

createRoot(document.getElementById('root')).render(
    <StrictMode>
        <App />
        {import.meta.env.MODE === "production" && <SpeedInsights />}
    </StrictMode>,
)
