import React, {useState, useEffect} from 'react'
import CSRFToken from '../components/CSRFToken';

const Search = () => {

    const handleClick = () => {
        fetch('http://127.0.0.1:8000/search-backend', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            }
        })
        window.location.reload(false)
    };

  return (
    <div className="home">
        <div className='stats-header, app-header'>
            <h2 className="stats-title-home">&#x1F4C8; YTanalytics</h2>
        </div>
        <div>
            <div className="home-heading">
                <h1>Welcome <span className="darkercolor"></span></h1>
            </div>
            <div className="home-description">
                <p>Search for YouTube channel</p>
            </div>
            <form action="" method="post" className="search-bar">
                <CSRFToken/>
	            <input type="text" name="handle" required id="id_handle"/>
	            <input type='submit' value="Submit"/>
            </form>
        </div>
    </div>
  )
}

export default Search