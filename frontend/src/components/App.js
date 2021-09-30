import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import TopBar from './TopBar';
import Footer from './Footer';
import Home from './Home';
import About from './About';
import FlashMessage from './FlashMessage';
import NotFound from './NotFound';
import './App.css';

function App() {
  return (
    <div className="d-flex flex-column vh-100">
      <Router>
        <TopBar />
        <FlashMessage />
        <main className="container" id="content">
          <Switch>
            <Route path="/" exact component={Home} />
            <Route path="/sobre" exact component={About} />
            <Route path="*" component={NotFound} />
          </Switch>
        </main>
      </Router>
      <Footer />
    </div>
  );
}

export default App;
