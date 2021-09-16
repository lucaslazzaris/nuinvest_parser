import { useCallback } from 'react'


export default function StockContent({stockData}) {
  const renderStocks = useCallback(
    () => {
      let i = 0;
      return stockData.map((stock) => {
        i++;
        return (
          <div key={i}>
            {stock.join(';').replaceAll('.', ',')}
          </div>
        )
      })
    },
    [stockData],
  )

  if (!stockData) {
    return null;
  }

  return (
    <div className="stocks-content">
      {renderStocks()}
    </div>
  )
}
