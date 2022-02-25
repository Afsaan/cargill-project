import os
from flask import Flask
from flask_restful import Api
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_sqlalchemy import SQLAlchemy
from flask_apispec.extension import FlaskApiSpec


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Cargil API',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/swagger/',  # URI to access API Doc JSON 
    'APISPEC_SWAGGER_UI_URL': '/docs/'  # URI to access UI of API Doc
})

db = SQLAlchemy(app)
# manager = Manager(app)
docs = FlaskApiSpec(app)
   
#wrap a app inside api
api = Api(app)

team_role_identifier = db.Table('team_role_identifier',
    db.Column('team_id', db.Integer, db.ForeignKey('team.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
)

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    role = db.relationship("Role", secondary=team_role_identifier , backref = "team")

    def __init__(self, name):
        self.name = name

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(30))

    def __init__(self, role):
        self.role = role
        