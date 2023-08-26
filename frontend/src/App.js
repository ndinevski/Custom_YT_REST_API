import{
  BrowserRouter as Router,
  Routes,
  Route
}from 'react-router-dom'

import './App.css';
import Statistics from './pages/Statistics'
import Statistic from './pages/Statistic'
import VideosRating from './pages/VideosRating'
import VideosViews from './pages/VideosViews'

function App() {
  let channelName = ''

  return (
    <Router>
      <div className="container dark">
        <div className='app'>
          <Routes>
            <Route path='/statistics' exact element={<Statistics/>} />
            <Route path='/statistics/:id' element={<Statistic/>} />
            <Route path='/statistics/:id/delete' element={<Statistic/>} />
            <Route path='/videos/views' element={<VideosViews/>} />
            <Route path='/videos/rating' element={<VideosRating/>} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;