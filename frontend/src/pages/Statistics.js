import React, {useState, useEffect} from 'react'
import {Link} from 'react-router-dom'

const Statistics = () => {
    let [statistics, setStatistics] = useState([])
    
    useEffect(() => {
        getStatistics()
    }, [])

    let getStatistics = async () => {
        let response = await fetch('http://127.0.0.1:8000/channel/UCX6OQ3DkcsbYNE6H8uQQuVA/historical')
        let data = await response.json()
        setStatistics(data)
    }
    let createStatistic = async () =>{
        fetch('http://127.0.0.1:8000/channel/UCX6OQ3DkcsbYNE6H8uQQuVA/historical/update', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        window.location.reload(false)
    }

    return (
    <div className='stats'>
        <div className="stats-header, app-header">
            <h2 className="stats-title">&#x1F4C8; Historical Statistics for {statistics[0]?.channel_name}</h2>
            <p className="stats-count">{statistics.length}</p>
        </div>
       
        <div className="stats-list">
            {statistics.map((statistic, index) => (
                <div className='stats-list-item' key={index}>
                    <h4 className='stats-link'><Link to={'/statistics/'+statistic.id}><u>{statistic.date_and_time}</u></Link></h4>
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