import { useCallback } from 'react'


export default function StockContent({stockData}) {
  const renderStocks = useCallback(
    () => {
      return stockData.map((stock) => {
        return (
          <div key={`${stock[1]}${stock[2]}`}>
            {stock.join(';').replace('/./g', ',')}
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
    <div className="stocks-content" data-test-id="stocks-row">
      {renderStocks()}
    </div>
  )
}
