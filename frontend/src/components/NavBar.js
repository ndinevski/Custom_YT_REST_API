import React from 'react'
import { Link } from 'react-router-dom'

const NavBar = ({parentToChild}) => {
  return (
    <div>
        <div className="stats-header, app-header">
            {parentToChild}
            <div className="navbarlist">
                <Link to="/">
                    <h3 className="navbar">Home</h3>
                </Link>
                <Link to="/statistics">
                    <h3 className="navbar">Statistics</h3>
                </Link>
                <Link to="/videos">
                    <h3 className="navbar">Videos</h3>
                </Link>
                <Link to="/logout">
                    <h3 className="navbar separatetitle">Logout</h3>
                </Link>
            </div>
        </div>    
    </div>
  )
}

export default NavBar