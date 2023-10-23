from flask import Blueprint, render_template, abort
from databaseInteraction.project_db_interaction import get_project_by_id


home_blueprint = Blueprint('home', __name__, template_folder='templates', static_folder='/home/static')


@home_blueprint.route('/')
def home():
    return render_template('home.html', active_page='home')