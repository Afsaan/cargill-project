import React, {useState, useEffect} from "react";
import {Button} from '@mui/material';

export const ShowRoles = ({ listOfTeam }) =>{

    const [team , setTeam] = useState("ML")
    const [roleslist , setRolesList] = useState([])


    const submitForm = () => {
        fetch(`/get-role/${team}`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
            })
            .then(response => response.json())
            .then(data => {
            console.log('Success:', data);
            setRolesList(data);
            })
            .catch((error) => {
            console.error('Error:', error);
            });
    }
    

    return(
        <>  
            <div>
                <label>Choose a Team: </label> 
                <select id="team" value={team} onChange={e => setTeam(e.currentTarget.value)}>
                {
                    listOfTeam.map((currElem, id) => {
                    return (
                                <option value={currElem.team} key={id}>{currElem.team}</option>
                            )})
                }
                </select>
            </div>
            <br></br>
            <Button type='submit' onClick={submitForm} variant="contained">Show Roles</Button>

            <ul>
            {
                    roleslist.map((currElem, id) => {
                    return (
                                <li key={id}>{currElem.role}</li>
                            )})
                } 
            </ul>
            
        </>
    )
}