import React, { useState, useEffect, useRef } from 'react'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { useToast } from '@/hooks/use-toast'
import { Eye, ArrowLeft, ArrowRight, Move } from 'lucide-react'
import Draggable from 'react-draggable'
import '@/assets/pdf_viewer.css'
import * as pdfjsLib from '../../../node_modules/pdfjs-dist/build/pdf'
import '../../../node_modules/pdfjs-dist/build/pdf.worker.mjs'

const PdfCanvas = React.memo(
  function PdfCanvas({ pdfDoc, currentPage, pageSize, canvasRef }) {
    useEffect(() => {
      let renderTask = null
      let cancelled = false
      const renderPage = async () => {
        if (!pdfDoc || !canvasRef.current || !pageSize.width) return
        try {
          const page = await pdfDoc.getPage(currentPage)
          const viewport = page.getViewport({ scale: 1 })
          const canvas = canvasRef.current
          const context = canvas.getContext('2d')
          canvas.width = viewport.width
          canvas.height = viewport.height
          renderTask = page.render({ canvasContext: context, viewport })
          await renderTask.promise
        } catch (e) {
          if (!cancelled) {
            // 这里不处理 toast，错误交给父组件
            window.dispatchEvent(new CustomEvent('pdf-render-error', { detail: e }))
          }
        }
      }
      renderPage()
      return () => {
        cancelled = true
        if (renderTask && renderTask.cancel) renderTask.cancel()
      }
    }, [pdfDoc, currentPage, pageSize.width])

    return (
      <canvas
        ref={canvasRef}
        width={pageSize.width}
        height={pageSize.height}
        style={{
          width: `${pageSize.width}px`,
          height: `${pageSize.height}px`,
          display: 'block',
          borderRadius: 8,
          background: '#fff',
          position: 'absolute',
          left: 0,
          top: 0,
          zIndex: 1
        }}
      />
    )
  },
  (prevProps, nextProps) =>
    prevProps.pdfDoc === nextProps.pdfDoc &&
    prevProps.currentPage === nextProps.currentPage &&
    prevProps.pageSize.width === nextProps.pageSize.width &&
    prevProps.pageSize.height === nextProps.pageSize.height
)

const StepThree = ({ contractData, onComplete, onPrev }) => {
  const [loading, setLoading] = useState(false)
  const [stampPositions, setStampPositions] = useState([])
  const [pdfUrl, setPdfUrl] = useState('')
  const [numPages, setNumPages] = useState(1)
  const [currentPage, setCurrentPage] = useState(1)
  const [pageSize, setPageSize] = useState({ width: 595, height: 842 }) // 默认A4
  const [pdfDoc, setPdfDoc] = useState(null)
  const canvasRef = useRef()
  const viewerRef = useRef()
  const { toast } = useToast()

  // 初始化PDF和印章（支持AI识别结果）
  useEffect(() => {
    if (contractData?.contractId) {
      setPdfUrl(`/api/contract/preview/${contractData.contractId}`)
      // 兼容AI识别结果
      if (contractData.suggestedPositions) {
        setStampPositions(
          contractData.suggestedPositions.map((pos, index) => ({
            ...pos,
            id: index,
            isDragging: false
          }))
        )
      }
    }
  }, [contractData])

  // 加载PDF.js并渲染第一页
  useEffect(() => {
    if (!pdfUrl) return
    const loadPdf = async () => {
      try {
        const loadingTask = pdfjsLib.getDocument(pdfUrl)
        const pdf = await loadingTask.promise
        setPdfDoc(pdf)
        setNumPages(pdf.numPages)
        setCurrentPage(1)
      } catch (e) {
        toast({ title: 'PDF加载失败', description: e.message, variant: 'destructive' })
      }
    }
    loadPdf()
  }, [pdfUrl])

  // 1. 获取页面尺寸
  useEffect(() => {
    if (!pdfDoc) return
    const getPageSize = async () => {
      const page = await pdfDoc.getPage(currentPage)
      const viewport = page.getViewport({ scale: 1 })
      setPageSize({ width: viewport.width, height: viewport.height })
    }
    getPageSize()
  }, [pdfDoc, currentPage])

  // 拖拽事件
  const handleDrag = (id, e, data) => {

    setStampPositions(prev => prev.map(pos =>
      pos.id === id
        ? { ...pos, x: data.x, y: data.y }
        : pos
    ))
  }

  // 添加印章
  const addStampPosition = () => {
    const newPosition = {
      id: stampPositions.length,
      page: currentPage - 1,
      x: 300,
      y: 400,
      width: 120,
      height: 120,
      score: 1.0,
      reason: '手动添加',
      isDragging: false
    }
    setStampPositions(prev => [...prev, newPosition])
  }

  // 删除印章
  const removeStampPosition = (id) => {
    setStampPositions(prev => prev.filter(pos => pos.id !== id))
  }

  // 跳转页
  const jumpToPage = (page) => {
    setCurrentPage(page + 1)
    viewerRef.current?.scrollIntoView({ behavior: 'smooth' })
  }

  // 下一步，传递所有印章位置
  const handleNext = () => {
    setLoading(true)
    // 只传递必要字段
    const finalPositions = stampPositions.map(pos => ({
      page: pos.page || 0,
      x: pos.x,
      y: pos.y,
      width: pos.width || 120,
      height: pos.height || 120,
      reason: pos.reason,
      score: pos.score
    }))
    setTimeout(() => {
      onComplete({ finalStampPositions: finalPositions })
      setLoading(false)
    }, 500)
  }

  const handlePrevPage = () => setCurrentPage(p => Math.max(1, p - 1))
  const handleNextPageBtn = () => setCurrentPage(p => Math.min(numPages, p + 1))

  // StepThree 组件内监听错误并弹 toast
  useEffect(() => {
    const handler = (e) => {
      toast({ title: 'PDF渲染失败', description: e.detail.message, variant: 'destructive' })
    }
    window.addEventListener('pdf-render-error', handler)
    return () => window.removeEventListener('pdf-render-error', handler)
  }, [toast])

  return (
    <Card>
      <CardHeader>
        <CardTitle className="flex items-center space-x-2">
          <Eye className="h-5 w-5" />
          <span>步骤三：预览合同并调整印章位置</span>
        </CardTitle>
        <CardDescription>
          预览合同内容，可以拖拽调整印章位置，确保盖章位置准确
        </CardDescription>
      </CardHeader>
      <CardContent className="space-y-6">
        {/* 操作提示 */}
        <div className="bg-blue-50 p-4 rounded-lg">
          <h3 className="font-medium text-blue-900 mb-2">操作说明：</h3>
          <ul className="text-sm text-blue-800 space-y-1">
            <li>• 红色方框表示AI建议的盖章位置</li>
            <li>• 可以拖拽方框调整印章位置</li>
            <li>• 可以添加或删除印章位置</li>
            <li>• 系统会自动在页面边缘添加骑缝章</li>
          </ul>
        </div>

        {/* 印章位置控制 */}
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-4">
            <span className="text-sm font-medium">印章位置管理：</span>
            <Button size="sm" onClick={addStampPosition}>
              添加印章位置
            </Button>
          </div>
          <div className="text-sm text-gray-600">
            当前共 {stampPositions.length} 个印章位置
          </div>
        </div>


        {/* PDF预览区域（canvas） */}
        <div className="border rounded-lg bg-white" style={{ overflow: 'auto' }}>
          <div
            ref={viewerRef}
            className="relative mx-auto"
            style={{
              width: `${pageSize.width}px`,
              height: `${pageSize.height}px`,
              background: '#f3f4f6'
            }}
          >
            <PdfCanvas
              pdfDoc={pdfDoc}
              currentPage={currentPage}
              pageSize={pageSize}
              canvasRef={canvasRef}
            />
            {/* 印章层保持原样 */}
            <div
              style={{
                position: 'absolute',
                left: 0,
                top: 0,
                width: `${pageSize.width}px`,
                height: `${pageSize.height}px`,
                zIndex: 2,
                pointerEvents: 'none'
              }}
            >
              {stampPositions.filter(pos => (pos.page || 0) === (currentPage - 1)).map((position) => (
                <Draggable
                  key={position.id}
                  position={{ x: position.x, y: position.y }}
                  onDrag={(e, data) => handleDrag(position.id, e, data)}
                  bounds="parent"
                >
                  <div
                    className="absolute border-2 border-red-500 bg-red-100 bg-opacity-50 cursor-move flex items-center justify-center group"
                    style={{
                      width: position.width || 120,
                      height: position.height || 120,
                      zIndex: 10,
                      pointerEvents: 'auto'
                    }}
                  >
                    <div className="text-xs text-red-700 text-center">
                      <Move className="h-4 w-4 mx-auto mb-1" />
                      <div>印章{position.id + 1}</div>
                    </div>
                    <button
                      onClick={() => removeStampPosition(position.id)}
                      className="absolute -top-2 -right-2 w-6 h-6 bg-red-500 text-white rounded-full text-xs opacity-0 group-hover:opacity-100 transition-opacity"
                    >
                      ×
                    </button>
                  </div>
                </Draggable>
              ))}
            </div>
          </div>
          {/* 翻页与跳页控件，放在PDF预览区下方 */}
          <div className="flex items-center justify-center space-x-2 bg-white bg-opacity-80 rounded px-3 py-2 shadow mt-4">
            <Button
              size="sm"
              variant="outline"
              disabled={currentPage <= 1}
              onClick={handlePrevPage}
            >
              上一页
            </Button>
            <span className="text-sm mx-2">
              第 {currentPage} 页 / 共 {numPages} 页
            </span>
            <Button
              size="sm"
              variant="outline"
              disabled={currentPage >= numPages}
              onClick={handleNextPageBtn}
            >
              下一页
            </Button>
            <span className="ml-4 text-sm">跳转到：</span>
            <input
              type="number"
              min={1}
              max={numPages}
              value={currentPage}
              onChange={e => {
                let val = Number(e.target.value)
                if (val >= 1 && val <= numPages) setCurrentPage(val)
              }}
              className="w-16 px-2 py-1 border rounded text-center"
            />
          </div>
        </div>

        {/* 印章位置列表 */}
        {stampPositions.length > 0 && (
          <div className="space-y-2">
            <h3 className="font-medium text-gray-900">当前印章位置：</h3>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-2">
              {stampPositions.map((position) => (
                <div
                  key={position.id}
                  className="flex items-center justify-between p-3 bg-gray-50 rounded-lg cursor-pointer hover:bg-blue-50 transition"
                  onClick={() => jumpToPage(position.page || 0)}
                >
                  <div className="flex items-center space-x-3">
                    <div className="w-6 h-6 bg-red-100 rounded-full flex items-center justify-center text-xs font-medium text-red-600">
                      {position.id + 1}
                    </div>
                    <div className="text-sm">
                      <div>第 {(position.page || 0) + 1} 页</div>
                      <div className="text-gray-600">
                        ({Math.round(position.x)}, {Math.round(position.y)})
                      </div>
                      <div className="text-gray-500 text-xs">{position.reason}</div>
                    </div>
                  </div>
                  <Button
                    size="sm"
                    variant="ghost"
                    onClick={e => {
                      e.stopPropagation()
                      removeStampPosition(position.id)
                    }}
                    className="text-red-600 hover:text-red-700"
                  >
                    删除
                  </Button>
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
            disabled={loading || stampPositions.length === 0}
            className="flex items-center space-x-2"
          >
            <span>{loading ? '处理中...' : '确认位置'}</span>
            <ArrowRight className="h-4 w-4" />
          </Button>
        </div>
      </CardContent>
    </Card>
  )
}

export default StepThree