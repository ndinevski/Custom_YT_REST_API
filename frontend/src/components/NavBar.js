import React from 'react'
import { Link } from 'react-router-dom'

const NavBar = ({parentToChild}) => {
  return (
    <div>
        <div className="stats-header, app-header">
            {parentToChild}
            <div className="navbarlist">
                <a href="http://127.0.0.1:8000" className="navbar">Home</a>
                <Link to="/statistics">
                    <h3 className="navbar">Statistics</h3>
                </Link>
                <Link to="/videos/views">
                    <h3 className="navbar">Videos</h3>
                </Link>
                <a href="http://127.0.0.1:8000/logout" className="navbar separatetitle">Logout</a>
            </div>
        </div>    
    </div>
  )
}

export default NavBar