import React, { Component, useEffect, useState} from "react";
import axios from 'axios'


function Users (match) {
    useEffect( () => {
        fetchUsers();
        console.log(match)
    })


    const [user, setUser] = useState({});
    const [accessToken, setToken] = useState({});
    //const accessToken = 'f1c5566858243f44c131e98b29b00afb9ab66936'

    // const headers = {
    //     'username': 'mihai-cozmuta',
    //     'password': 'mihai-cozmuta'
    // };

    // const getToken = await fetch(`http://localhost:8000/api/login/`)

    
    // useEffect(() => {
    //     // POST request using axios inside useEffect React hook
    //     const credentials = {
    //         "username":"mihai-cozmuta",
    //         "password":"mihai-cozmuta"
    //     };
    //     axios.post(`http://localhost:8000/api/login`, credentials)
    //         .then(response => setToken(response.token));
    
    // // empty dependency array means this effect will only run once (like componentDidMount in classes)
    // }, []);


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
    
    // empty dependency array means this effect will only run once (like componentDidMount in classes)
    }, []);

    console.log(accessToken.token)
    const fetchUsers = async () => {
        const fetchUsers = await fetch(`http://localhost:8000/api/users/8/`,{
            headers: {
                Authorization: `Token ${accessToken.token}`
            },
        });
        const user = await fetchUsers.json();
        setUser(user);


    }

    return(
        <div>
            <h1>{user.username}</h1>
        </div>
    );


}

export default Users;
