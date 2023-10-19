from flask import Blueprint, render_template, abort


projects = Blueprint('projects', __name__, template_folder='templates')

@projects.route('/<project_id>')
def project(project_id):
    # Fetch the project data from a database or other source using project_id
    project = get_project_by_id(project_id)
    if not project:
        abort(404)  # Return a 404 Not Found if the project doesn't exist
        Flask.tem
    return render_template('project_base.html', project=project)