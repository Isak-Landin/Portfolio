from flask import Flask, Blueprint, abort, render_template


about_blueprint = Blueprint('about', __name__, template_folder='templates', static_folder='/about/static')


@about_blueprint.route('/')
def about():
    return render_template('about.html', active_page='about')