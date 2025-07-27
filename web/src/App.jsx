import { useState } from 'react'
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom'
import { Toaster } from '@/components/ui/sonner'
import Navbar from './components/Navbar'
import Login from './components/Login'
import StampProcess from './components/StampProcess'
import SealManagement from './components/SealManagement'
import ContractList from './components/ContractList'
import './App.css'

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(true) // 简化认证，默认已登录
  const [currentUser, setCurrentUser] = useState({ id: 1, username: '管理员' })

  if (!isAuthenticated) {
    return <Login onLogin={setIsAuthenticated} />
  }

  return (
    <Router>
      <div className="min-h-screen bg-gray-50">
        <Navbar user={currentUser} onLogout={() => setIsAuthenticated(false)} />
        <main className="container mx-auto px-4 py-8">
          <Routes>
            <Route path="/" element={<Navigate to="/stamp" replace />} />
            <Route path="/stamp" element={<StampProcess userId={currentUser.id} />} />
            <Route path="/seals" element={<SealManagement userId={currentUser.id} />} />
            <Route path="/contracts" element={<ContractList userId={currentUser.id} />} />
          </Routes>
        </main>
        <Toaster />
      </div>
    </Router>
  )
}

export default App

