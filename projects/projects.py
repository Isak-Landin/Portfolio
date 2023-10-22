from flask import Blueprint, render_template, abort
from databaseInteraction.project_db_interaction import get_project_by_id


projects_blueprint = Blueprint('projects', __name__, template_folder='templates', static_folder='/projects/static')


@projects_blueprint.route('/<project_id>')
def project(project_id):
    # Fetch the project data from a database or other source using project_id
    project_ = get_project_by_id(project_id)
    if not project_:
        abort(404)  # Return a 404 Not Found if the project doesn't exist
    return render_template('project_base.html', project=project)