import React, {useState, useEffect} from 'react'
import App from '../App.js'

const Search = () => {
    const [message, setMessage] = useState('');
    const [input, setInput] = useState(message);

    const handleChange = (event) => {
        setMessage(event.target.value);
    };

    const handleClick = () => {
        setInput(message);
        fetch('http://127.0.0.1:8000/search-backend', {
            method: 'POST',
            headers: {
            }
        })
        window.location.replace("http://localhost:8000/statistics")
    };

    let setChannelName = () => {
        App.channel_name = input?.toString()
    }



  return (
    <div className="home">
        <div className='stats-header, app-header'>
            <h2 className="stats-title-home">&#x1F4C8; YTstats</h2>
        </div>
        <div>
            <div className="home-heading">
                <h1>Welcome <span className="darkercolor">{App.channel_name}</span></h1>
            </div>
            <div className="home-description">
                <p>Search for YouTube channel</p>
            </div>
            <form action="" className="search-bar">
	            <input type="text" id="message" name="message" onChange={handleChange} value={message}/>
	            <button className="search-btn" type="submit" onClick={handleClick}>
		            <span>Search</span>
	            </button>       
            </form>
            {setChannelName()}
        </div>
    </div>
  )
}

export default Search