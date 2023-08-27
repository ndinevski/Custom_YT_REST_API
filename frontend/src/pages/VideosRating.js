import React, {useState, useEffect} from 'react'
import {Link} from 'react-router-dom'
import NavBar from '../components/NavBar.js'

const VideosRating = () => {
    let [videos_by_rating, setVideosRating] = useState([])
    let [variables, setVariables] = useState([]);
    let image = ""
    let videoUrl = ""

    useEffect(() => {
        getVideosRating()
        getVariables()
    }, [])

    let getVideosRating = async () => {
        getVariables()
        let response = await fetch('http://127.0.0.1:8000/channel/UCX6OQ3DkcsbYNE6H8uQQuVA/videos_by_rating')
        let data = await response.json()
        setVideosRating(data)
    }

    let getVariables = async () => {
        let response = await fetch('http://127.0.0.1:8000/api/variables')
        let data = await response.json()
        setVariables(data)
    }

    let setThumbnail = (thumbnail) => {
        image = thumbnail
    }

    let setUrl = (url) => {
        videoUrl = url
    }

    return (
        <div>
            <NavBar parentToChild={<h2 className="stats-title">&#x1F4C8; Top 10 Videos for {videos_by_rating[0]?.channel_name}</h2>}/>
            
            <h1 class="choicevideo"><Link  to='/videos/views' className='notselectedvideo'>MOST VIEWED</Link> <span className='selectedvideo'>BEST RATED</span></h1>
            <div>
                <div className='stats'>
                    <div className="card-list">
                        {videos_by_rating.map((video, index) => (
                            <div className='card-list-item' key={index}>
                                <div>
                                    <div>
                                    {setThumbnail(video.thumbnail)}
                                    {setUrl(video.url)}
                                        <div>
                                            <p className='video-title'>#{index+1} {video.title}</p>
                                            <a href={videoUrl} rel="noreferrer" target="_blank"><img alt="Video thumbnail" className='video-image'src={image}></img></a>
                                            <div className="video-stats">
                                                <p>{video.view_count} views</p>
                                                <p>{video.like_count} likes</p>
                                                <p>{video.comment_count} comments</p>
                                            </div>
                                            <div className='video-description'>
                                                <p>Description:</p>
                                                <small>{video.description}</small>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        ))}
                    </div>
                </div>
            </div>
        </div> 
    )
}

export default VideosRating