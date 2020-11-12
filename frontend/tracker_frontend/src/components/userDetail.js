import React, { Component, useEffect, useState} from "react";

function Users (match) {
    useEffect( () => {
        fetchUsers();
        console.log(match)
    }, [])


    const [user, setUser] = useState({});


    const fetchUsers = async () => {
        const fetchUsers = await fetch(`http://localhost:8000/api/users/1/`);
        const user = await fetchUsers.json();
        setUser(user);
    }

    return(
        <div>
            <h1>{user.name}</h1>
        </div>
    );


}

export default Users;
