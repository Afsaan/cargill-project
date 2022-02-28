import logging
from flask_restful import Resource
from flask import request, jsonify
from flask_migrate import Migrate 
from flask_apispec.views import MethodResource
from flask_apispec import doc, use_kwargs, marshal_with
from models import app, docs, db, Role, Team, api
from config import path
from serializer import (
                        role_serializer, 
                        team_serializer, 
                        RolePayloadSchema, 
                        TeamPayloadSchema, 
                        TeamRolePayloadSchema,
                        RoleResponseSchema,
                        TeamResponseSchema,
                        TeamRoleResponseSchema
                        )
logging.basicConfig(filename=f'{path.logging_path}', level=30)
migrate = Migrate(app, db)

class RoleAPI(MethodResource, Resource):

    @doc(description='Get all the roles', tags=['Role'])
    @marshal_with(RoleResponseSchema, code=200)
    def get(self):
        return jsonify(list(map(role_serializer, Role.query.all())))

    @doc(description='Add roles', tags=['Role'])
    @use_kwargs(RolePayloadSchema, location=('json'))
    @marshal_with(None, code=200, description='{"msg": "Role added "}')
    def post(self, role):
        role = Role(request.get_json()['role'])
        db.session.add(role)
        db.session.commit()
        app.logger.info(f'Role added for {role}')
        return jsonify({"msg": "Role added "})

class TeamAPI(MethodResource, Resource):

    @doc(description='Get all the teams', tags=['Team'])
    @marshal_with(TeamResponseSchema, code=200)
    def get(self):
        return jsonify(list(map(team_serializer, Team.query.all())))

    @doc(description='add teams', tags=['Team'])
    @use_kwargs(TeamPayloadSchema, location=('json'))
    @marshal_with(None, code=200, description = '{"msg": "Team added "}')
    def post(self):
        team = Team(request.get_json()['team'])
        db.session.add(team)
        db.session.commit()

        return jsonify({"msg": "Team added "})

class GetTeamRoleAPI(MethodResource, Resource):
    @doc(description='Get associated Roles with Teams', tags=['Get Assocaited Role'])
    @marshal_with(RoleResponseSchema, code=200)
    def get(self, team):
        team = Team.query.filter_by(name=team).first()
        if team != None:
            return jsonify(list(map(role_serializer , team.role)))
        # print(data.id)
        # check if team name exist in db or not
        return {"data" : "no team available"}

class AddTeamRoleAPI(MethodResource, Resource):

    @doc(description='To map the given team with given roles', tags=['Manage Team Role'])
    @use_kwargs(TeamRolePayloadSchema, location=('json')) #TeamRoleResponseSchema
    @marshal_with(None, code=200, description="{'data' : 'team and role mapped'}")
    def post(self, team, role):
        
        #get role object
        role = Role.query.filter_by(role=request.get_json()['role']).first()
        if role == None:
            return jsonify({"msg" : "role does not exists"})

        #get team object
        team = Team.query.filter_by(name=request.get_json()['team']).first()
        if team == None:
            return jsonify({"msg" : "Team does not exists"})

        team.role.append(role)
        db.session.commit()

        return {'data' : "team and role mapped"}


# mapping url to class
api.add_resource(TeamAPI , '/team/')
api.add_resource(RoleAPI , '/role/')
api.add_resource(AddTeamRoleAPI , '/map-role/')
api.add_resource(GetTeamRoleAPI , '/get-role/<string:team>')

# documentation of API
docs.register(RoleAPI)
docs.register(TeamAPI)
docs.register(AddTeamRoleAPI)
docs.register(GetTeamRoleAPI)

if __name__ == "__main__":
    app.run(debug=True)
