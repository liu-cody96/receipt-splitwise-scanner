import axios from 'axios';
import { useEffect, useState, Fragment } from 'react';

export const Home = () => {

    const [data, setData] = useState([]);
    

    const getFlights = () => {
        axios.get('http://localhost:8000/')
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
        <p><h1 align="center">Python Flask Upload and display image</h1></p>
        <div class="container">
        <div class="row">
            <h2>Select a file to upload</h2>
            <form method="post" action="/" enctype="multipart/form-data">
                <dl>
                    <p>
                        <input type="file" name="file" autocomplete="off" required/>
                    </p>
                </dl>
                <p>
                    <input type="submit" value="Submit"/>
                </p>
            </form>
        </div>
        </div>

        </>
    );
}
