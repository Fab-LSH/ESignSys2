import { useState, useEffect } from 'react'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Badge } from '@/components/ui/badge'
import { useToast } from '@/hooks/use-toast'
import { FileText, Download, CheckCircle, XCircle, Clock, Eye, Trash2 } from 'lucide-react'

const ContractList = ({ userId }) => {
  const [contracts, setContracts] = useState([])
  const [loading, setLoading] = useState(false)
  const { toast } = useToast()

  useEffect(() => {
    fetchContracts()
  }, [userId])

  const fetchContracts = async () => {
    setLoading(true)
    try {
      const response = await fetch(`/api/contract/list?user_id=${userId}`)
      const data = await response.json()
      setContracts(data.contracts || [])
    } catch (error) {
      toast({
        title: "获取合同列表失败",
        description: error.message,
        variant: "destructive"
      })
    } finally {
      setLoading(false)
    }
  }

  const handleConfirm = async (contractId, action) => {
    try {
      const response = await fetch(`/api/contract/confirm/${contractId}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          action: action, // 'approve' 或 'reject'
          comment: ''
        })
      })

      if (response.ok) {
        toast({
          title: action === 'approve' ? "合同已通过" : "合同已拒绝",
          description: "状态更新成功"
        })
        fetchContracts()
      } else {
        throw new Error('操作失败')
      }
    } catch (error) {
      toast({
        title: "操作失败",
        description: error.message,
        variant: "destructive"
      })
    }
  }

  const handleDownload = (contractId) => {
    window.open(`/api/contract/download/${contractId}`, '_blank')
  }

  // const handlePreview = (contractId) => {
  //   window.open(`/api/contract/preview/${contractId}`, '_blank')
  // }

  const handlePreview = (contract) => {
    // 预览已盖章合同（根据合同编号、签约对方简称、合同名查找）
    const params = new URLSearchParams({
      contract_number: contract.contract_number,
      counterparty_abbr: contract.counterparty_abbr,
      contract_name: contract.contract_name
    }).toString()
    window.open(`/api/contract/preview_final?${params}`, '_blank')
  }


  const getStatusBadge = (status) => {
    const statusConfig = {
      'uploaded': { label: '已上传', variant: 'secondary', icon: Clock },
      'analyzed': { label: 'AI分析完成', variant: 'default', icon: Eye },
      'stamped': { label: '已盖章', variant: 'default', icon: CheckCircle },
      'confirmed': { label: '已确认', variant: 'default', icon: CheckCircle },
      'rejected': { label: '已拒绝', variant: 'destructive', icon: XCircle }
    }

    const config = statusConfig[status] || { label: status, variant: 'secondary', icon: Clock }
    const Icon = config.icon

    return (
      <Badge variant={config.variant} className="flex items-center space-x-1">
        <Icon className="h-3 w-3" />
        <span>{config.label}</span>
      </Badge>
    )
  }

  const formatDate = (dateString) => {
    if (!dateString) return '-'
    return new Date(dateString).toLocaleString('zh-CN')
  }

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="text-center">
          <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600 mx-auto"></div>
          <p className="mt-2 text-gray-600">加载中...</p>
        </div>
      </div>
    )
  }

  return (
    <div className="max-w-6xl mx-auto space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-3xl font-bold text-gray-900">合同管理</h1>
          <p className="mt-2 text-gray-600">查看和管理所有合同的签章状态</p>
        </div>
        
        <Button onClick={fetchContracts} variant="outline">
          刷新列表
        </Button>
      </div>

      {contracts.length === 0 ? (
        <Card>
          <CardContent className="text-center py-12">
            <FileText className="h-12 w-12 text-gray-400 mx-auto mb-4" />
            <h3 className="text-lg font-medium text-gray-900 mb-2">暂无合同</h3>
            <p className="text-gray-600">还没有上传任何合同，请前往签章流程上传合同。</p>
          </CardContent>
        </Card>
      ) : (
        <div className="grid grid-cols-1 gap-6">
          {contracts.map((contract) => (
            <Card key={contract.id}>
              <CardHeader>
                <div className="flex items-center justify-between">
                  <div>
                    <CardTitle className="text-lg">{contract.contract_name}</CardTitle>
                    <div className="flex flex-wrap items-center gap-4 mt-1">
                      <span className="text-lg font-bold text-blue-700">
                        合同编号: {contract.contract_number}
                      </span>
                      <span className="text-base font-semibold text-indigo-700">
                        签约对方: {contract.counterparty_abbr}
                      </span>
                    </div>
                  </div>
                  {getStatusBadge(contract.status)}
                </div>
              </CardHeader>
              <CardContent>
                <div className="space-y-2">
                  <div className="flex flex-wrap items-center gap-6">
                    <div className="flex items-center space-x-2">
                      <span className="text-gray-500 font-medium">印章位置：</span>
                      <Badge variant="outline" className="bg-green-50 text-green-700 border-green-200 px-3 py-1 rounded-full">
                        {contract.final_stamp_positions?.length || 0} 个
                      </Badge>
                    </div>
                    {contract.ai_suggested_positions && contract.ai_suggested_positions.length > 0 && (
                      <div className="flex items-center space-x-2">
                        <span className="text-gray-500 font-medium">AI建议位置：</span>
                        <div className="flex flex-wrap gap-2">
                          {contract.ai_suggested_positions.slice(0, 3).map((position, index) => (
                            <Badge
                              key={index}
                              variant="outline"
                              className="bg-blue-50 text-blue-700 border-blue-200 px-3 py-1 rounded-full"
                            >
                              第{(position.page || 0) + 1}页 ({Math.round(position.x)}, {Math.round(position.y)})
                            </Badge>
                          ))}
                          {contract.ai_suggested_positions.length > 3 && (
                            <Badge variant="outline" className="bg-blue-50 text-blue-700 border-blue-200 px-3 py-1 rounded-full">
                              +{contract.ai_suggested_positions.length - 3} 个
                            </Badge>
                          )}
                        </div>
                      </div>
                    )}
                  </div>

                  {/* 操作按钮 */}
                  <div className="flex items-center justify-between pt-4 border-t">
                    <div className="flex space-x-2">
                      <Button
                        size="sm"
                        variant="outline"
                        onClick={() => handlePreview(contract)}
                        className="flex items-center space-x-1"
                      >
                        <Eye className="h-4 w-4" />
                        <span>预览</span>
                      </Button>
                      
                      {contract.stamped_pdf_path && (
                        <Button
                          size="sm"
                          variant="outline"
                          onClick={() => handleDownload(contract.id)}
                          className="flex items-center space-x-1"
                        >
                          <Download className="h-4 w-4" />
                          <span>下载</span>
                        </Button>
                      )}


                    </div>

                    {/* 法务确认按钮 */}
                    {contract.status === 'stamped' && (
                      <div className="flex space-x-2">
                        <Button
                          size="sm"
                          variant="outline"
                          onClick={() => handleConfirm(contract.id, 'reject')}
                          className="text-red-600 hover:text-red-700"
                        >
                          拒绝
                        </Button>
                        <Button
                          size="sm"
                          onClick={() => handleConfirm(contract.id, 'approve')}
                          className="bg-green-600 hover:bg-green-700"
                        >
                          通过
                        </Button>
                      </div>
                    )}
                  </div>
                </div>
              </CardContent>
            </Card>
          ))}
        </div>
      )}
    </div>
  )
}

export default ContractList

