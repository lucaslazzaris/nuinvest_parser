import React from 'react'
import { Link } from 'react-router-dom'

export default function TopBar() {
  return (
    <nav className="navbar navbar-light bg-light">
    <div className="container">
      <Link className="navbar-brand" to="/">Home</Link>
      <div className="d-flex">
        <ul className="navbar-nav">
          <li className="nav-item">
            <Link className="nav-link" to="/sobre">Sobre</Link>
          </li>
        </ul>
      </div>
    </div>
  </nav>
  )
}
