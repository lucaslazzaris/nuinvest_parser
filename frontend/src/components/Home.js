import React from 'react'

export default function Home() {
  return (
  <>
    <div class="p-5 mt-3 mb-3 bg-light rounded-3">
      <h1 class="text-center">Leitor de notas de corretagem da Nu Invest</h1>
      <form
        id="files-form"
        enctype="multipart/form-data"
        action="/processar_nota"
        method="post"
      >
        <div class="row justify-content-center">
          <div class="col text-center">
            <label class="form-label" for="files">Selecione os arquivos</label>
          </div>
        </div>
        <div class="row justify-content-center">
          <div class="col-8">
            <p>
              <input
                class="form-control"
                type="file"
                id="files"
                name="files[]"
                accept=".pdf"
                multiple
              />
            </p>
          </div>
        </div>
        <div class="d-grid col-2 mx-auto">
            <button class="btn btn-primary" type="submit">Enviar</button>
        </div>
      </form>
    </div>

    <div class="stocks-content hidden"></div>
  </>
  )
}
