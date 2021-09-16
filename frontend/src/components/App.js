import React from 'react'
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import TopBar from './TopBar'; 
import Footer from './Footer';
import Home from './Home'; 
import About from './About'; 
import './App.css' 
const axios = require('axios');

function App() {
  return (
  <div className="d-flex flex-column vh-100">
    <Router>
      <TopBar />
      <main class='container' id="content">
        <Switch>
          <Route path='/' exact component={Home} />
          <Route path='/sobre' exact component={About} />
        </Switch>
      </main>
    </Router>  
    <Footer />
  </div>
  )
}

export default App;