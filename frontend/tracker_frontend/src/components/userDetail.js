import React, {useEffect, useState} from "react";
import maps from "./maps"

function Users (match) {
    useEffect( () => {
        fetchUsers();
        console.log(match)
    })


    const [user, setUser] = useState({});
    const [accessToken, setToken] = useState({});
   

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
    },[]);

    console.log(accessToken.token)
    const fetchUsers = async () => {
        const fetchUsers = await fetch(`http://localhost:8000/api/users/8/`,{
            headers: {
                Authorization: `Token ${accessToken.token}`
            },
        });
        const user = await fetchUsers.json();
        setUser(user)
    }

    return(
        <div>
            <h1>{user.first_name}</h1>
        </div>
    );

}

export default Users;
