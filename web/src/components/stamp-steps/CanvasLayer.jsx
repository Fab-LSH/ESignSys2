import React from 'react'

const CanvasLayer = React.memo(({ canvasRef, width, height }) => (
  <canvas
    ref={canvasRef}
    width={width}
    height={height}
    style={{
      width: `${width}px`,
      height: `${height}px`,
      display: 'block',
      borderRadius: 8,
      background: '#fff'
    }}
  />
))

export default CanvasLayer