import { useState, useEffect } from 'react'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { useToast } from '@/hooks/use-toast'
import { Brain, ArrowLeft, ArrowRight, Loader2 } from 'lucide-react'

const StepTwo = ({ contractData, onComplete, onPrev }) => {
  const [loading, setLoading] = useState(false)
  const [analyzing, setAnalyzing] = useState(false)
  const [suggestedPositions, setSuggestedPositions] = useState([])
  const { toast } = useToast()

  useEffect(() => {
    if (contractData?.contractId) {
      startAnalysis()
    }
  }, [contractData])

  const startAnalysis = async () => {
    setAnalyzing(true)
    
    try {
      const response = await fetch(`/api/contract/analyze/${contractData.contractId}`, {
        method: 'POST'
      })

      const data = await response.json()

      if (response.ok) {
        setSuggestedPositions(data.suggested_positions || [])
        toast({
          title: "AI分析完成",
          description: `识别到 ${data.suggested_positions?.length || 0} 个建议的盖章位置`
        })
      } else {
        throw new Error(data.error || 'AI分析失败')
      }
    } catch (error) {
      toast({
        title: "AI分析失败",
        description: error.message,
        variant: "destructive"
      })
      // 提供默认位置
      setSuggestedPositions([
        {
          x: 400,
          y: 600,
          width: 120,
          height: 120,
          page: 0,
          score: 1.0,
          reason: '默认位置：右下角'
        }
      ])
    } finally {
      setAnalyzing(false)
    }
  }

  const handleNext = () => {
    setLoading(true)
    
    // 模拟处理时间
    setTimeout(() => {
      onComplete({
        suggestedPositions
      })
      setLoading(false)
    }, 500)
  }

  return (
    <Card>
      <CardHeader>
        <CardTitle className="flex items-center space-x-2">
          <Brain className="h-5 w-5" />
          <span>步骤二：AI识别盖章位置</span>
        </CardTitle>
        <CardDescription>
          系统正在使用AI技术分析合同内容，识别最佳的盖章位置
        </CardDescription>
      </CardHeader>
      <CardContent className="space-y-6">
        {/* 合同信息展示 */}
        <div className="bg-gray-50 p-4 rounded-lg">
          <h3 className="font-medium text-gray-900 mb-2">合同信息</h3>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4 text-sm">
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
          </div>
        </div>

        {/* AI分析状态 */}
        <div className="text-center py-8">
          {analyzing ? (
            <div className="space-y-4">
              <Loader2 className="h-12 w-12 animate-spin mx-auto text-blue-600" />
              <div>
                <h3 className="text-lg font-medium text-gray-900">AI正在分析合同...</h3>
                <p className="text-gray-600 mt-2">
                  系统正在识别合同中的关键区域和最佳盖章位置，请稍候
                </p>
              </div>
              <div className="bg-blue-50 p-4 rounded-lg text-left">
                <h4 className="font-medium text-blue-900 mb-2">分析过程：</h4>
                <ul className="text-sm text-blue-800 space-y-1">
                  <li>• 提取PDF文本内容和布局信息</li>
                  <li>• 识别签名、盖章等关键词位置</li>
                  <li>• 分析页面布局和空白区域</li>
                  <li>• 计算最佳盖章位置建议</li>
                </ul>
              </div>
            </div>
          ) : (
            <div className="space-y-4">
              <div className="w-12 h-12 bg-green-100 rounded-full flex items-center justify-center mx-auto">
                <Brain className="h-6 w-6 text-green-600" />
              </div>
              <div>
                <h3 className="text-lg font-medium text-gray-900">AI分析完成</h3>
                <p className="text-gray-600 mt-2">
                  系统已识别到 {suggestedPositions.length} 个建议的盖章位置
                </p>
              </div>
            </div>
          )}
        </div>

        {/* 建议位置列表 */}
        {!analyzing && suggestedPositions.length > 0 && (
          <div className="space-y-4">
            <h3 className="font-medium text-gray-900">AI建议的盖章位置：</h3>
            <div className="space-y-2">
              {suggestedPositions.map((position, index) => (
                <div key={index} className="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
                  <div className="flex items-center space-x-3">
                    <div className="w-8 h-8 bg-blue-100 rounded-full flex items-center justify-center text-sm font-medium text-blue-600">
                      {index + 1}
                    </div>
                    <div>
                      <div className="font-medium">
                        第 {(position.page || 0) + 1} 页 - 位置 ({Math.round(position.x)}, {Math.round(position.y)})
                      </div>
                      <div className="text-sm text-gray-600">{position.reason}</div>
                    </div>
                  </div>
                  <div className="text-sm text-gray-500">
                    置信度: {Math.round((position.score || 0) * 100)}%
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* 操作按钮 */}
        <div className="flex justify-between pt-4">
          <Button variant="outline" onClick={onPrev} className="flex items-center space-x-2">
            <ArrowLeft className="h-4 w-4" />
            <span>上一步</span>
          </Button>
          
          <Button 
            onClick={handleNext} 
            disabled={analyzing || loading}
            className="flex items-center space-x-2"
          >
            <span>{loading ? '处理中...' : '下一步'}</span>
            <ArrowRight className="h-4 w-4" />
          </Button>
        </div>
      </CardContent>
    </Card>
  )
}

export default StepTwo

