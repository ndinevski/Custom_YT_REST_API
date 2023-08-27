import React from 'react'
    let login = async () => {
        window.location.replace('http://127.0.0.1:8000/social-auth/login/google-oauth2/');
    }

const Login = () => {
  return (
    <div className="home">
        <div className='stats-header, app-header'>
            <h2 className="stats-title-home">&#x1F4C8; YTanalytics</h2>
        </div>
        <div>
            <div className="home-heading">
                <h1>Historical <span className="darkercolor">YouTube</span></h1>
                <h1>statistics</h1>
            </div>
            <div className="home-description">
                <p>Search and save statistics for any YouTube channel</p>
                <p>Know your competitors and improve your channel</p>
            </div>
            <button className="home-button" onClick={login}>Sign In with Google</button>  
        </div>
    </div>
  )
}

export default Login