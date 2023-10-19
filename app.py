from flask import Flask
from app.projects import projects

app = Flask(__name__)
app.register_blueprint(projects.projects_blueprint, url_prefix='/projects')
