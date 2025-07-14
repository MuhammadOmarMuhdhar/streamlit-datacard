import {
  Streamlit,
  withStreamlitConnection,
  ComponentProps,
} from "streamlit-component-lib"
import React, { useEffect, ReactElement } from "react"

interface CardData {
  [key: string]: any
}

interface DataCardProps extends ComponentProps {
  args: {
    data: CardData[]
    title_field?: string
    image_field?: string
    field_types?: { [key: string]: string }
    card_width: number
    max_height: number
    clickable: boolean
  }
}

function MyComponent({ args, theme }: DataCardProps): ReactElement {
  const { 
    data = [], 
    title_field, 
    image_field, 
    field_types = {}, 
    card_width = 280, 
    max_height = 400,
    clickable = false
  } = args

  useEffect(() => {
    // Simple timeout to let content render, then set height
    const timer = setTimeout(() => {
      Streamlit.setFrameHeight()
    }, 50)
    
    return () => clearTimeout(timer)
  }, [data])

  const containerStyle: React.CSSProperties = {
    display: 'grid',
    gridTemplateColumns: `repeat(auto-fit, minmax(${card_width}px, 1fr))`,
    gap: '16px',
    padding: '16px',
    fontFamily: theme?.font || 'sans-serif',
  }

  const getCardStyle = (isClickable: boolean): React.CSSProperties => ({
    border: '1px solid #e5e7eb',
    borderRadius: '12px',
    padding: '20px',
    backgroundColor: theme?.backgroundColor || '#ffffff',
    maxHeight: `${max_height}px`,
    overflow: 'auto',
    cursor: isClickable ? 'pointer' : 'default',
    transition: isClickable ? 'box-shadow 0.2s ease' : 'none',
  })

  const imageStyle: React.CSSProperties = {
    width: '100%',
    height: '140px',
    objectFit: 'cover',
    borderRadius: '8px',
    marginBottom: '12px',
  }

  const titleStyle: React.CSSProperties = {
    fontSize: '18px',
    fontWeight: 'bold',
    marginBottom: '8px',
    color: theme?.textColor || '#000000',
  }

  const fieldStyle: React.CSSProperties = {
    fontSize: '14px',
    marginBottom: '4px',
    color: theme?.textColor || '#666666',
  }

  const getBadgeColor = (value: string): string => {
    let hash = 0
    for (let i = 0; i < value.length; i++) {
      const char = value.charCodeAt(i)
      hash = ((hash << 5) - hash) + char
      hash = hash & hash
    }
    
    const mutedColors = [
      '#6b7280', '#6366f1', '#059669', '#dc2626', '#7c3aed', '#0891b2',
      '#65a30d', '#ea580c', '#be185d', '#4338ca', '#0d9488', '#ca8a04',
      '#7f1d1d', '#1e3a8a', '#064e3b', '#78350f', '#581c87', '#164e63'
    ]
    
    const index = Math.abs(hash) % mutedColors.length
    return mutedColors[index]
  }

  const getBadgeStyle = (value: string): React.CSSProperties => ({
    display: 'inline-block',
    backgroundColor: getBadgeColor(value),
    color: '#ffffff',
    fontSize: '12px',
    padding: '0px 4px',
    borderRadius: '12px',
    marginRight: '4px',
  })

  const getTitle = (item: CardData): string => {
    if (title_field && item[title_field]) {
      return item[title_field]
    }
    const firstKey = Object.keys(item)[0]
    return item[firstKey] || 'Untitled'
  }


  const renderField = (key: string, value: any) => {
    if (key === title_field || key === image_field) return null
    
    const fieldType = field_types[key] || 'text'
    
    if (fieldType === 'badge') {
      const badges = String(value).split(',').map(b => b.trim())
      return (
        <div key={key} style={fieldStyle}>
          <strong>{key}:</strong>{' '}
          {badges.map((badge, i) => (
            <span key={i} style={getBadgeStyle(badge)}>{badge}</span>
          ))}
        </div>
      )
    }
    
    return (
      <div key={key} style={fieldStyle}>
        <strong>{key}:</strong> {value}
      </div>
    )
  }

  return (
    <div style={containerStyle}>
      {data.map((item, index) => (
        <div 
          key={index} 
          style={getCardStyle(clickable)}
          onMouseEnter={(e) => {
            if (clickable) {
              e.currentTarget.style.boxShadow = '0 4px 12px rgba(0, 0, 0, 0.15)'
            }
          }}
          onMouseLeave={(e) => {
            if (clickable) {
              e.currentTarget.style.boxShadow = 'none'
            }
          }}
          onClick={() => {
            if (clickable) {
              Streamlit.setComponentValue(item)
            }
          }}
        >
          {image_field && item[image_field] && (
            <img
              src={item[image_field]}
              alt={getTitle(item)}
              style={imageStyle}
              onError={(e) => {
                e.currentTarget.style.display = 'none'
              }}
            />
          )}
          
          <div style={titleStyle}>
            {getTitle(item)}
          </div>
          
          {Object.entries(item).map(([key, value]) => 
            renderField(key, value)
          )}
        </div>
      ))}
    </div>
  )
}

export default withStreamlitConnection(MyComponent)