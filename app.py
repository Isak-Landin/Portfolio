from flask import Flask
from projects.projects import projects_blueprint
from contact.contact import contact_blueprint
from home.home import home_blueprint
from about.about import about_blueprint

import os

app = Flask(__name__, template_folder='templates', static_folder='static')
app.register_blueprint(projects_blueprint, url_prefix='/projects')
app.register_blueprint(contact_blueprint, url_prefix='/contact')
app.register_blueprint(home_blueprint, url_prefix='/')
app.register_blueprint(about_blueprint, url_prefix='/about')


@app.route('/debug')
def debug():
    current_directory = os.getcwd()
    return f"Current Working Directory: {current_directory}"
