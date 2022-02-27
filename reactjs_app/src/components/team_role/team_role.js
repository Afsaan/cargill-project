import React, {useState, useEffect} from "react";
import {Alert, Button, Snackbar} from '@mui/material';

export const TeamRole = ({ listOfRole,listOfTeam }) =>{

    const [role , setRole] = useState("ML engineer")
    const [team , setTeam] = useState("ML")
    const [message , setMessage] = useState(null)
    const [open, setOpen] = React.useState(false);
    const [messageType, setMessageType] = useState("")

    const handleClick = () => {
      setOpen(true);
    };
  
    const handleClose = (event, reason) => {
      if (reason === 'clickaway') {
        return;
      }
  
      setOpen(false);
    };

    const AlertBox = () => {
        return(
            <>
            <Snackbar open={open} autoHideDuration={6000} onClose={handleClose}>
                <Alert onClose={handleClose} severity={messageType} sx={{ width: '100%' }}>
                        {message}
                </Alert>
            </Snackbar>
            </>
        )
    }

    const submitForm = () => {
        fetch('map-role/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({role,team}),
            })
            .then(response => response.json())
            .then(data => {
            const success = "Successfully Mapped the Role and Team"
            setMessage(success);
            setOpen(true)
            setMessageType("success")
            })
            .catch((error) => {
            const success = "Some Probelm Occured"
            setMessage(success);
            setOpen(true)
            setMessageType("error")
            });
    }
    
    return(
        <>  
            <div>
                <label>Choose a Role: </label> 
                <select id="role" value={role} onChange={e => setRole(e.currentTarget.value)}>
                {
                    listOfRole.map((currElem, id) => {
                    return (
                                <option value={currElem.role} key={id}>{currElem.role}</option>
                            )})
                }
                </select>
            </div>
            <br></br>
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
            <Button type='submit' onClick={submitForm} variant="contained">Add</Button>
            
            {<div>{message?<AlertBox/>:""}</div>}

            
        </>
    )
}