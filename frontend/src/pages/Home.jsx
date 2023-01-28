import axios from 'axios';
import { useEffect, useState, Fragment } from 'react';

export const Home = () => {

    const [data, setData] = useState([]);
    

    const getFlights = () => {
        axios.get('/')
        .then((res) => {
            setData(res.data);
        });
        
    }



    return (
        <>
            <div style={{padding: '15px'}}>
                <button id="myForm" onClick={getFlights}>Display</button>
            </div>
            <div id="hello">
                {data}
            </div>

        </>
    );
}
