import React, {useState, useEffect} from "react";
import { TeamRole } from '../team_role/team_role';

export const Role = () => {
        const [role , setRole] = useState([])
    
        useEffect(() => { 
            fetch("/role/").then(response => {
                    console.log(response)
                    return response.json()
            }).then(data => setRole(data))
    },[]);
    return (
        <>
        {/* <i class="fas fa-h1    ">{JSON.stringify(role)}</i> */}
        <TeamRole listOfRole={role}/>
        </>
    )
}