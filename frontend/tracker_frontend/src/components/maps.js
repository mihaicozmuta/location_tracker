import React, {useEffect, useState , Component } from 'react';
import GoogleMapReact from 'google-map-react';
import Marker from './Marker';
import Users from './userDetail';

const AnyReactComponent = ({ text }) => <div>{text}</div>;


function SimpleMap () {


  const [accessToken, setToken] = useState({});
  const [user, setUser] = useState({});
   
    useEffect(() => {
        // POST request using fetch inside useEffect React hook
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username: 'mihai-cozmuta' , password: 'mihai-cozmuta'})
        };
        fetch('http://localhost:8000/api/login', requestOptions)
            .then(response => response.json())
            .then(data => setToken(data));
  
    });

    console.log(accessToken.token)


    useEffect(() => {
      // POST request using fetch inside useEffect React hook
      const requestOptions = {
          method: 'GET',
          headers: {Authorization: `Token ${accessToken.token}`},
      };
      fetch('http://localhost:8000/api/locations/1', requestOptions)
          .then(response => response.json())
          .then(data => setUser(data));
  

  });

  console.log(user.latitude)
  console.log(user.longitude)


  //   useEffect => {
  //     const fetchUsers = await fetch(`http://localhost:8000/api/users/8/`,{
  //         headers: {
  //             Authorization: `Token ${accessToken.token}`
  //         },
  //     });
  //     const user = await fetchUsers.json();
  //     setUser(user)
  // }
  const lat = user.latitude
  const lon = user.longitude

  const props = {
    center: {
      lat: 46.78026705316211,
      lng: 23.596632492608634
    },
    zoom: 10
  };

  {
    return (
      // Important! Always set the container height explicitly
      <div style={{ height: '100vh', width: '100%' }}>
        <GoogleMapReact
          bootstrapURLKeys={{ key: 'AIzaSyAV5kvNho0jXsgJUuWjOBO9kpOVPtz8XVA'}}
          yesIWantToUseGoogleMapApiInternals
          defaultCenter={props.center}
          defaultZoom={props.zoom}
        >
          <Marker
            lat={lat}
            lng={lon}
            text="My Marker"
            color = "red"
          />
        </GoogleMapReact>
      </div>
    );
  }
}

export default SimpleMap;