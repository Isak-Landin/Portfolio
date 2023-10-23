from flask import Flask, Blueprint, abort, render_template


contact_blueprint = Blueprint('contact', __name__, template_folder='templates', static_folder='static')


@contact_blueprint.route('/')
def contact_main():
    return render_template('contact.html', active_page='contact')