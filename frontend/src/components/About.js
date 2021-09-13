import React from 'react'

export default function About() {
  return (
    <div class="p-5 mt-3 mb-3 bg-light rounded-3">
      <h1 class="text-center">Leitor de notas de corretagem da Nu Invest</h1>
        <div class="row justify-content-center">
          <div class="col text-left">
            <p>Esse projeto tem como objetivo facilitar a gestão financeira de investimentos pessoais. Em vez de transcrever
              todas as ações compradas e vendidas de uma nota de corretagem, com este leitor, é possível apenas copiar e
              colar em alguma planilha eletrônica. Atualmente o leitor funciona apenas com dados da corretora Nu Invest
              pois é a única corretora em que o autor possui conta. Caso queira sugerir uma nova corretora, por favor, entre
              em contato com <a href='mailto:lucascercal.l@gmail.com'>lucascercal.l@gmail.com</a></p>
            <p>Sobre o autor: Lucas Cercal Lazzaris é um engenheiro de software com formação em engenharia mecânica e que
              curte práticas de open source. </p>
            <p>Github: <a href='https://www.github.com/lucaslazzaris'>lucaslazzaris</a></p>
          </div>
        </div>
    </div>
  )
}
