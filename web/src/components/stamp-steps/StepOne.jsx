import { useState } from 'react'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Label } from '@/components/ui/label'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select'
import { useToast } from '@/hooks/use-toast'
import { Upload, FileText, Paperclip } from 'lucide-react'

const StepOne = ({ userId, seals, onComplete }) => {
  const [formData, setFormData] = useState({
    contractNumber: '',
    counterpartyAbbr: '',
    contractName: '',
    selectedSealId: ''
  })
  const [files, setFiles] = useState({
    mainContract: null,
    attachments: []
  })
  const [loading, setLoading] = useState(false)
  const { toast } = useToast()

  const handleInputChange = (field, value) => {
    setFormData(prev => ({ ...prev, [field]: value }))
  }

  const handleMainContractChange = (e) => {
    const file = e.target.files[0]
    if (file && file.type === 'application/pdf') {
      setFiles(prev => ({ ...prev, mainContract: file }))
    } else {
      toast({
        title: "文件格式错误",
        description: "请选择PDF格式的文件",
        variant: "destructive"
      })
    }
  }

  const handleAttachmentsChange = (e) => {
    const selectedFiles = Array.from(e.target.files).filter(file => file.type === 'application/pdf')
    setFiles(prev => ({ ...prev, attachments: selectedFiles }))
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    
    if (!files.mainContract) {
      toast({
        title: "请选择主合同文件",
        variant: "destructive"
      })
      return
    }

    if (!formData.contractNumber || !formData.counterpartyAbbr || !formData.contractName) {
      toast({
        title: "请填写完整的合同信息",
        variant: "destructive"
      })
      return
    }

    setLoading(true)

    try {
      const uploadFormData = new FormData()
      uploadFormData.append('main_contract', files.mainContract)
      uploadFormData.append('contract_number', formData.contractNumber)
      uploadFormData.append('counterparty_abbr', formData.counterpartyAbbr)
      uploadFormData.append('contract_name', formData.contractName)
      uploadFormData.append('user_id', userId)

      // 添加附件
      files.attachments.forEach(file => {
        uploadFormData.append('attachments', file)
      })

      const response = await fetch('/api/contract/upload', {
        method: 'POST',
        body: uploadFormData
      })

      const data = await response.json()

      if (response.ok) {
        toast({
          title: "文件上传成功",
          description: "正在进行下一步..."
        })
        
        onComplete({
          contractId: data.contract_id,
          contract: data.contract,
          selectedSealId: formData.selectedSealId,
          ...formData
        })
      } else {
        throw new Error(data.error || '上传失败')
      }
    } catch (error) {
      toast({
        title: "上传失败",
        description: error.message,
        variant: "destructive"
      })
    } finally {
      setLoading(false)
    }
  }

  return (
    <Card>
      <CardHeader>
        <CardTitle className="flex items-center space-x-2">
          <Upload className="h-5 w-5" />
          <span>步骤一：上传文件和合同信息</span>
        </CardTitle>
        <CardDescription>
          请上传主合同文件、附件（可选），并填写合同相关信息
        </CardDescription>
      </CardHeader>
      <CardContent>
        <form onSubmit={handleSubmit} className="space-y-6">
          {/* 合同信息 */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div className="space-y-2">
              <Label htmlFor="contractNumber">合同编号 *</Label>
              <Input
                id="contractNumber"
                value={formData.contractNumber}
                onChange={(e) => handleInputChange('contractNumber', e.target.value)}
                placeholder="如：ZS-202504PO-213"
                required
              />
            </div>
            
            <div className="space-y-2">
              <Label htmlFor="counterpartyAbbr">签约对方简称 *</Label>
              <Input
                id="counterpartyAbbr"
                value={formData.counterpartyAbbr}
                onChange={(e) => handleInputChange('counterpartyAbbr', e.target.value)}
                placeholder="如：上海集采汇"
                required
              />
            </div>
            
            <div className="space-y-2">
              <Label htmlFor="contractName">合同名称 *</Label>
              <Input
                id="contractName"
                value={formData.contractName}
                onChange={(e) => handleInputChange('contractName', e.target.value)}
                placeholder="如：采购合同"
                required
              />
            </div>
          </div>

          {/* 印章选择 */}
          <div className="space-y-2">
            <Label htmlFor="sealSelect">选择印章</Label>
            <Select value={formData.selectedSealId} onValueChange={(value) => handleInputChange('selectedSealId', value)}>
              <SelectTrigger>
                <SelectValue placeholder="请选择要使用的印章" />
              </SelectTrigger>
              <SelectContent>
                {seals.map(seal => (
                  <SelectItem key={seal.id} value={seal.id.toString()}>
                    {seal.name} ({seal.seal_type})
                  </SelectItem>
                ))}
              </SelectContent>
            </Select>
          </div>

          {/* 主合同上传 */}
          <div className="space-y-2">
            <Label htmlFor="mainContract">主合同文件 *</Label>
            <div className="border-2 border-dashed border-gray-300 rounded-lg p-6">
              <div className="text-center">
                <FileText className="mx-auto h-12 w-12 text-gray-400" />
                <div className="mt-4">
                  <label htmlFor="mainContract" className="cursor-pointer">
                    <span className="mt-2 block text-sm font-medium text-gray-900">
                      {files.mainContract ? files.mainContract.name : '点击选择主合同PDF文件'}
                    </span>
                  </label>
                  <input
                    id="mainContract"
                    type="file"
                    accept=".pdf"
                    onChange={handleMainContractChange}
                    className="hidden"
                    required
                  />
                </div>
                <p className="mt-2 text-xs text-gray-500">
                  仅支持PDF格式，最大50MB
                </p>
              </div>
            </div>
          </div>

          {/* 附件上传 */}
          <div className="space-y-2">
            <Label htmlFor="attachments">附件文件（可选）</Label>
            <div className="border-2 border-dashed border-gray-300 rounded-lg p-6">
              <div className="text-center">
                <Paperclip className="mx-auto h-12 w-12 text-gray-400" />
                <div className="mt-4">
                  <label htmlFor="attachments" className="cursor-pointer">
                    <span className="mt-2 block text-sm font-medium text-gray-900">
                      {files.attachments.length > 0 
                        ? `已选择 ${files.attachments.length} 个附件` 
                        : '点击选择附件PDF文件'}
                    </span>
                  </label>
                  <input
                    id="attachments"
                    type="file"
                    accept=".pdf"
                    multiple
                    onChange={handleAttachmentsChange}
                    className="hidden"
                  />
                </div>
                <p className="mt-2 text-xs text-gray-500">
                  可选择多个PDF文件作为附件
                </p>
              </div>
            </div>
          </div>

          {/* 已选择的附件列表 */}
          {files.attachments.length > 0 && (
            <div className="space-y-2">
              <Label>已选择的附件：</Label>
              <div className="space-y-1">
                {files.attachments.map((file, index) => (
                  <div key={index} className="flex items-center space-x-2 text-sm text-gray-600">
                    <Paperclip className="h-4 w-4" />
                    <span>{file.name}</span>
                  </div>
                ))}
              </div>
            </div>
          )}

          <div className="flex justify-end">
            <Button type="submit" disabled={loading} className="px-8">
              {loading ? '上传中...' : '下一步'}
            </Button>
          </div>
        </form>
      </CardContent>
    </Card>
  )
}

export default StepOne

