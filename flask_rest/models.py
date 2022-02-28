from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_apispec.extension import FlaskApiSpec
from config import Swagger


app = Flask(__name__)
# app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:admin@localHost:5432/cargill"
app.config.update(Swagger().swagger_config)

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
        