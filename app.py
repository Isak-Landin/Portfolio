from flask import Flask
from projects.projects import projects_blueprint

import os

app = Flask(__name__, template_folder='templates')
app.register_blueprint(projects_blueprint, url_prefix='/projects')

app.static_folder = 'static'


@app.route('/debug')
def debug():
    current_directory = os.getcwd()
    return f"Current Working Directory: {current_directory}"
