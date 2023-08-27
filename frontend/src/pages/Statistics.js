import React, {useState, useEffect} from 'react'
import {Link} from 'react-router-dom'
import NavBar from '../components/NavBar'

const Statistics = () => {
    let [statistics, setStatistics] = useState([])
    let [variables, setVariables] = useState([]);
    
    useEffect(() => {
        getStatistics()
        getVariables()
    }, [])

    let getStatistics = async () => {
        getVariables()
        let response = await fetch('http://127.0.0.1:8000/channel/'+ variables.YOUTUBE_CHANNEL_ID +'/historical')
        let data = await response.json()
        setStatistics(data)
    }

    let createStatistic = async () =>{
        getVariables()
        fetch('http://127.0.0.1:8000/channel/'+ variables.YOUTUBE_CHANNEL_ID +'/historical/update', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        window.location.reload(false)
    }

    let getVariables = async () => {
        let response = await fetch('http://127.0.0.1:8000/api/variables')
        let data = await response.json()
        setVariables(data)
    }


    return (
    <div className='stats'>
        <NavBar parentToChild={<h2 className="stats-title">&#x1F4C8; Historical Statistics for {statistics[0]?.channel_name} <span className="stats-count">{statistics.length}</span></h2>}/>
        
        <div className="stats-list">
            {statistics.map((statistic, index) => (
                <div className='stats-list-item' key={index}>
                    <h4 className='stat-link'><Link to={'/statistics/'+statistic.id}><u>{statistic.date_and_time}</u></Link></h4>
                    <h4>Subscribers: {statistic.subscriber_count}</h4>
                    <h4>Views: {statistic.view_count}</h4>
                    <h4>Videos: {statistic.video_count}</h4>
                </div>
            ))}
        </div>

        <div>
            <Link to="/statistics" >
                <button className="button-5" onClick={createStatistic}>Add statistic</button>
            </Link>
        </div>
    </div>
  )
}

export default Statistics