from marshmallow import Schema, fields

class RolePayloadSchema(Schema):
    role = fields.String(required=True)

class RoleResponseSchema(Schema):
    role = fields.String(required=True)

class TeamPayloadSchema(Schema):
    team = fields.String(required=True)

class TeamResponseSchema(Schema):
    team = fields.String(required=True)

class TeamRolePayloadSchema(Schema):
    team = fields.String(required=True)
    role = fields.String(required=True)

class TeamRoleResponseSchema(Schema):
    team = fields.String(required=True)
    role = fields.String(required=True)

def role_serializer(role):
    return {
        'role' : role.role
    }

def team_serializer(team):
    return {
        'team' : team.name
    }
