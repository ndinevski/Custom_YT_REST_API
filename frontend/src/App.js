import{
  BrowserRouter as Router,
  Routes,
  Route
}from 'react-router-dom'

import './App.css';
import Statistics from './pages/Statistics'
import Statistic from './pages/Statistic'

function App() {
  return (
    <Router>
      <div className="container dark">
        <div className="app">
          <Routes>
            <Route path='/statistics' element={<Statistics/>} />
            <Route path='/statistics/:id' element={<Statistic/>} />
            <Route path='/statistics/:id/delete' element={<Statistic/>} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;