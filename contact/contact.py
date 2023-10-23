from flask import Flask, Blueprint, abort, render_template


contacts_blueprint = Blueprint('contact', __name__, template_folder='templates', static_folder='/contact/static')


@contacts_blueprint.route('/')
def contacts_main():
    return render_template('contact.html', active_page='contact')