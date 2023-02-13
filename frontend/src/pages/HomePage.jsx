import axios from 'axios';
import { useEffect, useState } from 'react';
import {Login} from '../components/Login'
import {Profile} from '../components/Profile'
import {Header} from '../components/Header'
import useToken from '../components/useToken'
import '../App.css'

export const HomePage = () => {

    const [data, setData] = useState([]);
    const { token, removeToken, setToken } = useToken();

    const getFlights = () => {
        axios.get('http://localhost:8000')
        .then((res) => {
            setData(res.data);
        });
        
    }



    return (
        <>
            <div style={{padding: '15px'}}>
                <button id="myForm" onClick={getFlights}>Display</button>
            </div>
            <div id="welcome">
                <h1>{data} </h1>
            </div>
            
            <div>
                {!token && token!=="" &&token!== undefined?  <Login setToken={setToken} /> // display login if token does not exist
                // display profile if token exists
                :(
                <> 
                <Header token={removeToken}/>
                <Profile token={token} setToken={setToken}/>
                </>
                )}
            </div>
        </>
    );
}
