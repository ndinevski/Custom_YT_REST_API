import React, {useState, useEffect} from 'react'
import { Link, useParams } from 'react-router-dom';
import NavBar from '../components/NavBar'
import { ReactComponent as ArrowLeft}  from '../assets/arrow-left.svg'

const Statistic = () => {
    const { id } = useParams();
    let [statistic, setStatistic] = useState(null)
    let [data, setData] = useState('');

    useEffect(() => {
        async function getStatistic(){
            let response =  await fetch('http://127.0.0.1:8000/channel/UCX6OQ3DkcsbYNE6H8uQQuVA/historical/' + id)
            let data = await response.json()
            console.log(data)
            setStatistic(data)
        }
        getStatistic()
    }, [id])

    let deleteStatistic = async () =>{
        fetch('http://127.0.0.1:8000/channel/UCX6OQ3DkcsbYNE6H8uQQuVA/historical/' + id, {
            method: 'DELETE',
            'headers': {
                'Content-Type': 'application/json'
            }
        })
    }

    let parentToChild = () => {
        setData();
    }

    return (
        <div className="stats">
            <NavBar parentToChild={<div className="stats-header">
                <h3>
                    <Link to="/statistics">  
                        <ArrowLeft />
                    </Link>
                </h3>
            </div>}/>
            <div className="center">
                <h3 className="stats-title">{statistic?.channel_name}</h3>
                <div>
                    <h4 className="stat-title"><p>{statistic?.date_and_time}</p></h4>
                    <h4>Subscribers: {statistic?.subscriber_count}</h4>
                    <h4>Views: {statistic?.view_count}</h4>
                    <h4>Videos: {statistic?.video_count}</h4>
                </div>
            </div>
            <div>
            <Link to="/statistics" >
                <button className="button-5" onClick={deleteStatistic}>Delete statistic</button>
            </Link>
        </div>
        </div>
    )
}

export default Statistic