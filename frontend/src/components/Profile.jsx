import { useState } from 'react'
import axios from "axios";

export const Profile = (props) => {

  const [profileData, setProfileData] = useState(null)
  const [image, setImage] = useState(null)

  const onImageChange = (e) => {
    const img = e.target.files[0]
    setImage(img)
  }

  const sendReceipt = (e) => {
    //e.preventDefault()
    let formData = new FormData();
    formData.append('image', image);
    for (let key of formData.entries()) {
      console.log(key[0] + ', ' + key[1]);
  }

    axios({
      method: "POST",
      url:"http://localhost:8000/receiptscanner",
      data: formData,
      headers: {'Content-Type': 'multipart/form-data' }
      //"Authorization": 'Bearer ' + props.token,
    })
    .then((response) => {
      const res = response.data
      res.access_token && props.setToken(res.access_token)
    }).catch((error) => {
      if (error.response) {
        console.log(error.response)
        console.log(error.response.status)
        console.log(error.response.headers)
        }
    })}

  const getData = () => {
    axios({
      method: "GET",
      url:"http://localhost:8000/login/profile",
      headers: {
        Authorization: 'Bearer ' + props.token
      }
    })
    .then((response) => {
      const res = response.data
      res.access_token && props.setToken(res.access_token)
      setProfileData(({
        profile_name: res.username
        }))
    }).catch((error) => {
      if (error.response) {
        console.log(error.response)
        console.log(error.response.status)
        console.log(error.response.headers)
        }
    })}

  return (
    <div className="Profile">

        <p>To get your profile details: </p><button onClick={getData}>Click me</button>
        {profileData && 
          <div>
              <p>Profile name: {profileData.profile_name}</p>
              <p>About me: i like chocolate</p>
              <input type="file" multiple accept="image/*" onChange={onImageChange} />
              <button onClick={sendReceipt}>Submit</button>
            </div>
        }

    </div>
  );
}

export default Profile;