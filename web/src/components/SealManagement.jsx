import { useState, useEffect } from 'react'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle, DialogTrigger } from '@/components/ui/dialog'
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select'
import { useToast } from '@/hooks/use-toast'
import { Plus, Edit, Trash2, Upload, Image } from 'lucide-react'

const SealManagement = ({ userId }) => {
  const [seals, setSeals] = useState([])
  const [loading, setLoading] = useState(false)
  const [dialogOpen, setDialogOpen] = useState(false)
  const [editingSeal, setEditingSeal] = useState(null)
  const [formData, setFormData] = useState({
    name: '',
    seal_type: 'official'
  })
  const [selectedFile, setSelectedFile] = useState(null)
  const { toast } = useToast()

  useEffect(() => {
    fetchSeals()
  }, [userId])

  const fetchSeals = async () => {
    try {
      const response = await fetch(`/api/seal/list?user_id=${userId}`)
      const data = await response.json()
      setSeals(data.seals || [])
    } catch (error) {
      toast({
        title: "获取印章列表失败",
        description: error.message,
        variant: "destructive"
      })
    }
  }

  const handleFileChange = (e) => {
    const file = e.target.files[0]
    if (file && (file.type === 'image/png' || file.type === 'image/jpeg')) {
      setSelectedFile(file)
    } else {
      toast({
        title: "文件格式错误",
        description: "请选择PNG或JPG格式的图片",
        variant: "destructive"
      })
    }
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    
    if (!formData.name) {
      toast({
        title: "请输入印章名称",
        variant: "destructive"
      })
      return
    }

    if (!editingSeal && !selectedFile) {
      toast({
        title: "请选择印章图片",
        variant: "destructive"
      })
      return
    }

    setLoading(true)

    try {
      if (editingSeal) {
        // 更新印章信息
        const response = await fetch(`/api/seal/${editingSeal.id}`, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(formData)
        })

        if (response.ok) {
          toast({
            title: "印章信息更新成功"
          })
          fetchSeals()
        } else {
          throw new Error('更新失败')
        }
      } else {
        // 新增印章
        const uploadFormData = new FormData()
        uploadFormData.append('seal_image', selectedFile)
        uploadFormData.append('seal_name', formData.name)
        uploadFormData.append('seal_type', formData.seal_type)
        uploadFormData.append('user_id', userId)

        const response = await fetch('/api/seal/upload', {
          method: 'POST',
          body: uploadFormData
        })

        if (response.ok) {
          toast({
            title: "印章上传成功"
          })
          fetchSeals()
        } else {
          throw new Error('上传失败')
        }
      }

      setDialogOpen(false)
      resetForm()
    } catch (error) {
      toast({
        title: editingSeal ? "更新失败" : "上传失败",
        description: error.message,
        variant: "destructive"
      })
    } finally {
      setLoading(false)
    }
  }

  const handleEdit = (seal) => {
    setEditingSeal(seal)
    setFormData({
      name: seal.name,
      seal_type: seal.seal_type
    })
    setDialogOpen(true)
  }

  const handleDelete = async (sealId) => {
    if (!confirm('确定要删除这个印章吗？')) {
      return
    }

    try {
      const response = await fetch(`/api/seal/${sealId}`, {
        method: 'DELETE'
      })

      if (response.ok) {
        toast({
          title: "印章删除成功"
        })
        fetchSeals()
      } else {
        throw new Error('删除失败')
      }
    } catch (error) {
      toast({
        title: "删除失败",
        description: error.message,
        variant: "destructive"
      })
    }
  }

  const resetForm = () => {
    setFormData({
      name: '',
      seal_type: 'official'
    })
    setSelectedFile(null)
    setEditingSeal(null)
  }

  const handleDialogClose = () => {
    setDialogOpen(false)
    resetForm()
  }

  return (
    <div className="max-w-6xl mx-auto space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold text-gray-900">印章管理</h1>
          <p className="mt-2 text-gray-600">管理您的电子印章，支持增加、编辑和删除操作</p>
        </div>
        
        <Dialog open={dialogOpen} onOpenChange={setDialogOpen}>
          <DialogTrigger asChild>
            <Button className="flex items-center space-x-2">
              <Plus className="h-4 w-4" />
              <span>添加印章</span>
            </Button>
          </DialogTrigger>
          <DialogContent>
            <DialogHeader>
              <DialogTitle>{editingSeal ? '编辑印章' : '添加新印章'}</DialogTitle>
              <DialogDescription>
                {editingSeal ? '修改印章信息' : '上传新的印章图片并填写相关信息'}
              </DialogDescription>
            </DialogHeader>
            
            <form onSubmit={handleSubmit} className="space-y-4">
              <div className="space-y-2">
                <Label htmlFor="sealName">印章名称 *</Label>
                <Input
                  id="sealName"
                  value={formData.name}
                  onChange={(e) => setFormData(prev => ({ ...prev, name: e.target.value }))}
                  placeholder="请输入印章名称"
                  required
                />
              </div>
              
              <div className="space-y-2">
                <Label htmlFor="sealType">印章类型</Label>
                <Select value={formData.seal_type} onValueChange={(value) => setFormData(prev => ({ ...prev, seal_type: value }))}>
                  <SelectTrigger>
                    <SelectValue placeholder="选择印章类型" />
                  </SelectTrigger>
                  <SelectContent>
                    <SelectItem value="official">公章</SelectItem>
                    <SelectItem value="personal">私章</SelectItem>
                    <SelectItem value="contract">合同章</SelectItem>
                    <SelectItem value="financial">财务章</SelectItem>
                  </SelectContent>
                </Select>
              </div>
              
              {!editingSeal && (
                <div className="space-y-2">
                  <Label htmlFor="sealImage">印章图片 *</Label>
                  <div className="border-2 border-dashed border-gray-300 rounded-lg p-6">
                    <div className="text-center">
                      <Image className="mx-auto h-12 w-12 text-gray-400" />
                      <div className="mt-4">
                        <label htmlFor="sealImage" className="cursor-pointer">
                          <span className="mt-2 block text-sm font-medium text-gray-900">
                            {selectedFile ? selectedFile.name : '点击选择印章图片'}
                          </span>
                        </label>
                        <input
                          id="sealImage"
                          type="file"
                          accept="image/png,image/jpeg"
                          onChange={handleFileChange}
                          className="hidden"
                          required
                        />
                      </div>
                      <p className="mt-2 text-xs text-gray-500">
                        支持PNG、JPG格式，建议尺寸100x100像素
                      </p>
                    </div>
                  </div>
                </div>
              )}
              
              <div className="flex justify-end space-x-2">
                <Button type="button" variant="outline" onClick={handleDialogClose}>
                  取消
                </Button>
                <Button type="submit" disabled={loading}>
                  {loading ? '处理中...' : (editingSeal ? '更新' : '上传')}
                </Button>
              </div>
            </form>
          </DialogContent>
        </Dialog>
      </div>

      {/* 印章列表 */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {seals.map((seal) => (
          <Card key={seal.id}>
            <CardHeader>
              <div className="flex items-center justify-between">
                <CardTitle className="text-lg">{seal.name}</CardTitle>
                <div className="flex space-x-1">
                  <Button size="sm" variant="ghost" onClick={() => handleEdit(seal)}>
                    <Edit className="h-4 w-4" />
                  </Button>
                  <Button size="sm" variant="ghost" onClick={() => handleDelete(seal.id)}>
                    <Trash2 className="h-4 w-4" />
                  </Button>
                </div>
              </div>
              <CardDescription>
                类型: {seal.seal_type === 'official' ? '公章' : 
                      seal.seal_type === 'personal' ? '私章' : 
                      seal.seal_type === 'contract' ? '合同章' : 
                      seal.seal_type === 'financial' ? '财务章' : seal.seal_type}
              </CardDescription>
            </CardHeader>
            <CardContent>
              <div className="space-y-4">
                {/* 印章图片预览 */}
                <div className="flex justify-center">
                  <img
                    src={`/api/seal/${seal.id}/image`}
                    alt={seal.name}
                    className="w-20 h-20 object-contain border rounded"
                    onError={(e) => {
                      e.target.src = '/placeholder-seal.png'
                    }}
                  />
                </div>
                
                <div className="text-sm text-gray-600 text-center">
                  创建时间: {new Date(seal.created_at).toLocaleDateString('zh-CN')}
                </div>
              </div>
            </CardContent>
          </Card>
        ))}
      </div>

      {seals.length === 0 && (
        <Card>
          <CardContent className="text-center py-12">
            <Upload className="h-12 w-12 text-gray-400 mx-auto mb-4" />
            <h3 className="text-lg font-medium text-gray-900 mb-2">暂无印章</h3>
            <p className="text-gray-600">还没有上传任何印章，请点击上方按钮添加印章。</p>
          </CardContent>
        </Card>
      )}
    </div>
  )
}

export default SealManagement

