import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import Category from './components/categoryCards.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
    {/* <Category/> */}
    
  </StrictMode>,
)
