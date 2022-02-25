import imp
from flask_restful import Api, Resource
from flask import Flask, request, jsonify
from flask_migrate import Migrate 
from flask_apispec.views import MethodResource
from flask_apispec import doc, use_kwargs
from models import app, docs, db, Role, Team, api
from serializer import (
                        role_serializer, 
                        team_serializer, 
                        RolePayloadSchema, 
                        TeamPayloadSchema, 
                        TeamRolePayloadSchema
                        )

migrate = Migrate(app, db)

class RoleAPI(MethodResource, Resource):

    @doc(description='Role API', tags=['Role'])
    def get(self):
        return jsonify(list(map(role_serializer, Role.query.all())))

    @doc(description='Role API', tags=['Role'])
    @use_kwargs(RolePayloadSchema, location=('json'))
    def post(self, role):
        role = Role(request.get_json()['role'])
        db.session.add(role)
        db.session.commit()
        return jsonify({"msg": "Role added "})

class TeamAPI(MethodResource, Resource):

    @doc(description='Team API', tags=['Team'])
    def get(self):
        return jsonify(list(map(team_serializer, Team.query.all())))

    @doc(description='Team API', tags=['Team'])
    @use_kwargs(TeamPayloadSchema, location=('json'))
    def post(self):
        team = Team(request.get_json()['team'])
        db.session.add(team)
        db.session.commit()

        return jsonify({"msg": "Team added "})

class GetTeamRoleAPI(MethodResource, Resource):
    @doc(description='Get Team Role API', tags=['Get Assocaited Role'])
    def get(self, team):
        team = Team.query.filter_by(name=team).first()
        if team != None:
            return jsonify(list(map(role_serializer , team.role)))
        # print(data.id)
        # check if team name exist in db or not
        return {"data" : "no team available"}

class AddTeamRoleAPI(MethodResource, Resource):

    @doc(description='Add Team Role API', tags=['Manage Team Role'])
    @use_kwargs(TeamRolePayloadSchema, location=('json'))
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
