
import { Role } from "../role/role";
import { Team } from "../team/team";

export const TeamRole = ({ listOfRole }) =>{
    return(
        <>
            {listOfRole.map(Role => {
                return (
                    <ul :key={number.toString()}>
                        <li>{Role.content}</li>
                    </ul>
                )
            })}
        </>
    )
}