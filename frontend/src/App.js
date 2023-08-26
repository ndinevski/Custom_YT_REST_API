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
import Login from './pages/Login'
import Search from './pages/Search';

function App() {
  let channelName = ''
  let channelId = ''

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
            <Route path='/search' element={<Search/>} />
            <Route path='/login' element={<Login/>} />
            <Route path='/' element={<Login/>} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;