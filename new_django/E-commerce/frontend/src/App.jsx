import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

import Router from './routes/Router';
import Header from './layout/Header';
import Footer from './layout/Footer';





function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <Header />
      <Router />
      <Footer />
    </>
  )
}

export default App
