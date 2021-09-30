import axios from 'axios';
import { useCallback, useState } from 'react';
import { connect } from 'react-redux';
import { emitFlashMessage } from '../actions'
import history from '../history'
import StockContent from './StockContent'

function Home({emitFlashMessage}) {
  const [stockData, setStockData] = useState(null);
  const onSubmit = useCallback((event) => {
    event.preventDefault();
    const formData = new FormData(document.getElementById('files-form'));
    axios
      .post('processar_nota', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      })
      .then(({data}) => {
        if (data.redirect_url) {
          history.push(data.redirect_url);
        } else {
          setStockData(data.stocks);
          if(data.flash_message){
            emitFlashMessage(data.flash_message);
          }
        }
      }
      ).catch(({response}) => {
        history.push(response.data.redirect_url);
        emitFlashMessage(response.data.flash_message);
        setStockData(null);
      });
  }, [emitFlashMessage]);

  return (
    <>
      <div className="p-5 mt-3 mb-3 bg-light rounded-3">
        <h1 className="text-center">Leitor de notas de corretagem da Nu Invest</h1>
        <form
          id="files-form"
          encType="multipart/form-data"
          action="/processar_nota"
          method="post"
          onSubmit={onSubmit}
          data-test-id="file-form"
        >
          <div className="row justify-content-center">
            <div className="col text-center">
              <label className="form-label" htmlFor="files">
                Selecione os arquivos
              </label>
            </div>
          </div>
          <div className="row justify-content-center">
            <div className="col-8">
              <p>
                <input
                  className="form-control"
                  type="file"
                  id="files"
                  name="files[]"
                  accept=".pdf"
                  multiple
                />
              </p>
            </div>
          </div>
          <div className="d-grid col-2 mx-auto">
            <button className="btn btn-primary" type="submit">
              Enviar
            </button>
          </div>
        </form>
      </div>

      {stockData ? (
        <StockContent stockData={stockData} />
      ) : null}
    </>
  );
}

export default connect(null, {emitFlashMessage})(Home);