import React from 'react';

export default function Footer() {
  return (
    <footer className="footer mt-auto py-3 bg-light">
      <div className="container">
        <div className="text-muted">
          Essa página é meramente informativa e nos responsabilizamos pelo uso
          dos dados aqui mostrados.
        </div>
        <div className="text-muted">
          Qualquer bug enviar para{' '}
          <a href="mailto:lucascercal.l@gmail.com">lucascercal.l@gmail.com</a>,
          será um prazer ajudar.
        </div>
      </div>
    </footer>
  );
}
