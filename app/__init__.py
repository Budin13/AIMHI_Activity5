from flask import Flask
from dotenv import dotenv_values
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


ENV_VARIABLES = dotenv_values(".env")


app = Flask(__name__)
SWAGGER_URL = "/swagger"  # URL for exposing Swagger UI (without trailing '/')
API_URL = "/static/swagger.json"


app.config.from_object(ENV_VARIABLES["SERVER_CONFIGURATION"])

db = SQLAlchemy()
db.init_app(app)


migrate = Migrate(app, db, compare_type=True)
