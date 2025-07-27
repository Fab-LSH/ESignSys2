import { useState } from 'react'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { useToast } from '@/hooks/use-toast'
import { CheckCircle, Download, ArrowLeft, RotateCcw, Loader2 } from 'lucide-react'

const StepFour = ({ contractData, onComplete, onPrev, onReset }) => {
  const [loading, setLoading] = useState(false)
  const [stamping, setStamping] = useState(false)
  const [completed, setCompleted] = useState(false)
  const [downloadUrl, setDownloadUrl] = useState('')
  const { toast } = useToast()

  const handleStamp = async () => {
    setStamping(true)
    
    try {
      const response = await fetch(`/api/contract/stamp/${contractData.contractId}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          stamp_positions: contractData.finalStampPositions,
          seal_id: contractData.selectedSealId
        })
      })

      const data = await response.json()

      if (response.ok) {
        setCompleted(true)
        setDownloadUrl(`/api/contract/download/${contractData.contractId}`)
        toast({
          title: "印章加盖成功",
          description: "合同已成功加盖电子印章，可以下载了"
        })
        onComplete({ completed: true })
      } else {
        throw new Error(data.error || '加盖印章失败')
      }
    } catch (error) {
      toast({
        title: "加盖印章失败",
        description: error.message,
        variant: "destructive"
      })
    } finally {
      setStamping(false)
    }
  }

  const handleDownload = () => {
    if (downloadUrl) {
      window.open(downloadUrl, '_blank')
    }
  }

  const generateFileName = () => {
    return `${contractData.contractNumber}${contractData.counterpartyAbbr}${contractData.contractName}.pdf`
  }

  return (
    <Card>
      <CardHeader>
        <CardTitle className="flex items-center space-x-2">
          <CheckCircle className="h-5 w-5" />
          <span>步骤四：确认加盖印章并下载</span>
        </CardTitle>
        <CardDescription>
          确认所有信息无误后，点击加盖印章按钮完成签章流程
        </CardDescription>
      </CardHeader>
      <CardContent className="space-y-6">
        {/* 合同信息确认 */}
        <div className="bg-gray-50 p-4 rounded-lg">
          <h3 className="font-medium text-gray-900 mb-4">合同信息确认</h3>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm">
            <div>
              <span className="text-gray-600">合同编号：</span>
              <span className="font-medium">{contractData?.contractNumber}</span>
            </div>
            <div>
              <span className="text-gray-600">签约对方：</span>
              <span className="font-medium">{contractData?.counterpartyAbbr}</span>
            </div>
            <div>
              <span className="text-gray-600">合同名称：</span>
              <span className="font-medium">{contractData?.contractName}</span>
            </div>
            <div>
              <span className="text-gray-600">印章位置：</span>
              <span className="font-medium">{contractData?.finalStampPositions?.length || 0} 个</span>
            </div>
          </div>
        </div>

        {/* 印章位置汇总 */}
        {contractData?.finalStampPositions && contractData.finalStampPositions.length > 0 && (
          <div className="space-y-2">
            <h3 className="font-medium text-gray-900">印章位置汇总：</h3>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-2">
              {contractData.finalStampPositions.map((position, index) => (
                <div key={index} className="flex items-center space-x-3 p-3 bg-blue-50 rounded-lg">
                  <div className="w-6 h-6 bg-blue-100 rounded-full flex items-center justify-center text-xs font-medium text-blue-600">
                    {index + 1}
                  </div>
                  <div className="text-sm">
                    <div>第 {(position.page || 0) + 1} 页</div>
                    <div className="text-gray-600">
                      位置: ({Math.round(position.x)}, {Math.round(position.y)})
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* 文件名预览 */}
        <div className="bg-green-50 p-4 rounded-lg">
          <h3 className="font-medium text-green-900 mb-2">生成的文件名：</h3>
          <div className="text-sm text-green-800 font-mono bg-white p-2 rounded border">
            {generateFileName()}
          </div>
        </div>

        {/* 加盖印章状态 */}
        <div className="text-center py-8">
          {!completed && !stamping && (
            <div className="space-y-4">
              <div className="w-16 h-16 bg-blue-100 rounded-full flex items-center justify-center mx-auto">
                <CheckCircle className="h-8 w-8 text-blue-600" />
              </div>
              <div>
                <h3 className="text-lg font-medium text-gray-900">准备加盖印章</h3>
                <p className="text-gray-600 mt-2">
                  请确认以上信息无误，点击下方按钮开始加盖电子印章
                </p>
              </div>
            </div>
          )}

          {stamping && (
            <div className="space-y-4">
              <Loader2 className="h-16 w-16 animate-spin mx-auto text-blue-600" />
              <div>
                <h3 className="text-lg font-medium text-gray-900">正在加盖印章...</h3>
                <p className="text-gray-600 mt-2">
                  系统正在为合同加盖电子印章，请稍候
                </p>
              </div>
              <div className="bg-blue-50 p-4 rounded-lg text-left max-w-md mx-auto">
                <h4 className="font-medium text-blue-900 mb-2">处理过程：</h4>
                <ul className="text-sm text-blue-800 space-y-1">
                  <li>• 在PDF上添加合同编号和日期</li>
                  <li>• 在指定位置加盖电子印章</li>
                  <li>• 添加骑缝章</li>
                  <li>• 生成最终文件</li>
                </ul>
              </div>
            </div>
          )}

          {completed && (
            <div className="space-y-4">
              <div className="w-16 h-16 bg-green-100 rounded-full flex items-center justify-center mx-auto">
                <CheckCircle className="h-8 w-8 text-green-600" />
              </div>
              <div>
                <h3 className="text-lg font-medium text-gray-900">印章加盖完成</h3>
                <p className="text-gray-600 mt-2">
                  电子印章已成功加盖，您可以下载最终的合同文件
                </p>
              </div>
            </div>
          )}
        </div>

        {/* 操作按钮 */}
        <div className="flex justify-between pt-4">
          <div className="flex space-x-2">
            {!completed && (
              <Button variant="outline" onClick={onPrev} disabled={stamping} className="flex items-center space-x-2">
                <ArrowLeft className="h-4 w-4" />
                <span>上一步</span>
              </Button>
            )}
            
            <Button variant="outline" onClick={onReset} className="flex items-center space-x-2">
              <RotateCcw className="h-4 w-4" />
              <span>重新开始</span>
            </Button>
          </div>
          
          <div className="flex space-x-2">
            {!completed && (
              <Button 
                onClick={handleStamp} 
                disabled={stamping}
                className="flex items-center space-x-2"
              >
                {stamping ? (
                  <>
                    <Loader2 className="h-4 w-4 animate-spin" />
                    <span>加盖中...</span>
                  </>
                ) : (
                  <>
                    <CheckCircle className="h-4 w-4" />
                    <span>确认加盖印章</span>
                  </>
                )}
              </Button>
            )}
            
            {completed && (
              <Button 
                onClick={handleDownload}
                className="flex items-center space-x-2"
              >
                <Download className="h-4 w-4" />
                <span>下载合同</span>
              </Button>
            )}
          </div>
        </div>
      </CardContent>
    </Card>
  )
}

export default StepFour

