import './App.css';
import React, {useState, useEffect} from "react";
import { ShowRoles } from "./components/roles/get_roles";
import { TeamRole } from "./components/team_role/team_role";
import {Grid, Container} from '@mui/material';

function App() {
  const [role , setRole] = useState([]);
  const [team , setTeam] = useState([]);

  const getData = async() => {
    try
    {
      const response_role = await fetch("role/");
      const response_team = await fetch("team/");
    
      setRole(await response_role.json());
      setTeam(await response_team.json());
    }
    catch(err){
      console.log('api is not working')
    }
     
  }

  useEffect(() => { 
      getData();
  },[]);

return (
  <>
      <h1><center>Cargill Team API DEMO</center></h1>
      <Container maxWidth="md">
        <Grid container spacing={2}>
          <Grid item xs={6}>
            <h1>Team Role Mapping</h1>
            <TeamRole listOfRole={role} listOfTeam={team}/>
          </Grid>
          <Grid item xs={6}>
            <h1>Get Assocaited Role</h1>
            <ShowRoles listOfTeam={team}/>
          </Grid>
        </Grid>
      </Container>
  </>
)
}
export default App;
