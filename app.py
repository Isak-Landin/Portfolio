from flask import Flask
from application.projects.projects import projects_blueprint

app = Flask(__name__)
app.register_blueprint(projects_blueprint, url_prefix='/projects')

