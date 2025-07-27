import { useState, useEffect } from 'react'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Progress } from '@/components/ui/progress'
import { useToast } from '@/hooks/use-toast'
import StepOne from './stamp-steps/StepOne'
import StepTwo from './stamp-steps/StepTwo'
import StepThree from './stamp-steps/StepThree'
import StepFour from './stamp-steps/StepFour'

const StampProcess = ({ userId }) => {
  const [currentStep, setCurrentStep] = useState(1)
  const [contractData, setContractData] = useState(null)
  const [seals, setSeals] = useState([])
  const { toast } = useToast()

  const steps = [
    { id: 1, title: '上传文件', description: '上传主合同、附件和合同信息' },
    { id: 2, title: 'AI识别', description: '系统自动识别建议的盖章位置' },
    { id: 3, title: '预览调整', description: '预览合同并调整印章位置' },
    { id: 4, title: '确认下载', description: '确认加盖印章并下载文件' },
  ]

  useEffect(() => {
    // 获取印章列表
    fetchSeals()
  }, [userId])

  const fetchSeals = async () => {
    try {
      const response = await fetch(`/api/seal/list?user_id=${userId}`)
      const data = await response.json()
      setSeals(data.seals || [])
    } catch (error) {
      console.error('获取印章列表失败:', error)
    }
  }

  const handleStepComplete = (data) => {
    setContractData(prev => ({ ...prev, ...data }))
    if (currentStep < 4) {
      setCurrentStep(currentStep + 1)
    }
  }

  const handlePrevStep = () => {
    if (currentStep > 1) {
      setCurrentStep(currentStep - 1)
    }
  }

  const handleReset = () => {
    setCurrentStep(1)
    setContractData(null)
    toast({
      title: "流程重置",
      description: "签章流程已重置，可以开始新的操作。",
    })
  }

  const renderStep = () => {
    switch (currentStep) {
      case 1:
        return (
          <StepOne
            userId={userId}
            seals={seals}
            onComplete={handleStepComplete}
          />
        )
      case 2:
        return (
          <StepTwo
            contractData={contractData}
            onComplete={handleStepComplete}
            onPrev={handlePrevStep}
          />
        )
      case 3:
        return (
          <StepThree
            contractData={contractData}
            onComplete={handleStepComplete}
            onPrev={handlePrevStep}
          />
        )
      case 4:
        return (
          <StepFour
            contractData={contractData}
            onComplete={handleStepComplete}
            onPrev={handlePrevStep}
            onReset={handleReset}
          />
        )
      default:
        return null
    }
  }

  return (
    <div className="max-w-4xl mx-auto space-y-6">
      <div className="text-center">
        <h1 className="text-3xl font-bold text-gray-900">加盖签章</h1>
        <p className="mt-2 text-gray-600">按照以下步骤完成电子签章流程</p>
      </div>

      {/* 步骤指示器 */}
      <Card>
        <CardHeader>
          <CardTitle>流程进度</CardTitle>
          <CardDescription>
            当前步骤: {currentStep}/4 - {steps[currentStep - 1]?.title}
          </CardDescription>
        </CardHeader>
        <CardContent>
          <div className="space-y-4">
            <Progress value={(currentStep / 4) * 100} className="w-full" />
            
            <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
              {steps.map((step) => (
                <div
                  key={step.id}
                  className={`p-4 rounded-lg border-2 transition-colors ${
                    step.id === currentStep
                      ? 'border-blue-500 bg-blue-50'
                      : step.id < currentStep
                      ? 'border-green-500 bg-green-50'
                      : 'border-gray-200 bg-gray-50'
                  }`}
                >
                  <div className="flex items-center space-x-2">
                    <div
                      className={`w-6 h-6 rounded-full flex items-center justify-center text-sm font-medium ${
                        step.id === currentStep
                          ? 'bg-blue-500 text-white'
                          : step.id < currentStep
                          ? 'bg-green-500 text-white'
                          : 'bg-gray-300 text-gray-600'
                      }`}
                    >
                      {step.id}
                    </div>
                    <span className="font-medium">{step.title}</span>
                  </div>
                  <p className="mt-2 text-sm text-gray-600">{step.description}</p>
                </div>
              ))}
            </div>
          </div>
        </CardContent>
      </Card>

      {/* 当前步骤内容 */}
      {renderStep()}
    </div>
  )
}

export default StampProcess

