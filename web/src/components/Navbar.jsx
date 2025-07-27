import { Link, useLocation } from 'react-router-dom'
import { Button } from '@/components/ui/button'
import { Stamp, FileText, Settings, LogOut } from 'lucide-react'

const Navbar = ({ user, onLogout }) => {
  const location = useLocation()

  const navItems = [
    { path: '/stamp', label: '加盖签章', icon: Stamp },
    { path: '/contracts', label: '合同管理', icon: FileText },
    { path: '/seals', label: '印章管理', icon: Settings },
  ]

  return (
    <nav className="bg-white shadow-sm border-b">
      <div className="container mx-auto px-4">
        <div className="flex items-center justify-between h-16">
          <div className="flex items-center space-x-8">
            <div className="flex items-center space-x-2">
              <Stamp className="h-8 w-8 text-blue-600" />
              <span className="text-xl font-bold text-gray-900">电子签章系统</span>
            </div>
            
            <div className="flex space-x-4">
              {navItems.map((item) => {
                const Icon = item.icon
                const isActive = location.pathname === item.path
                
                return (
                  <Link
                    key={item.path}
                    to={item.path}
                    className={`flex items-center space-x-2 px-3 py-2 rounded-md text-sm font-medium transition-colors ${
                      isActive
                        ? 'bg-blue-100 text-blue-700'
                        : 'text-gray-600 hover:text-gray-900 hover:bg-gray-100'
                    }`}
                  >
                    <Icon className="h-4 w-4" />
                    <span>{item.label}</span>
                  </Link>
                )
              })}
            </div>
          </div>

          <div className="flex items-center space-x-4">
            <span className="text-sm text-gray-600">欢迎，{user.username}</span>
            <Button
              variant="ghost"
              size="sm"
              onClick={onLogout}
              className="flex items-center space-x-2"
            >
              <LogOut className="h-4 w-4" />
              <span>退出</span>
            </Button>
          </div>
        </div>
      </div>
    </nav>
  )
}

export default Navbar

