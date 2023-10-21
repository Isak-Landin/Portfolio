from flask import Flask, Blueprint, abort, render_template


contacts_blueprint = Blueprint('contacts', __name__, template_folder='templates')


@contacts_blueprint.route('/')
def contacts_main():
    return render_template('contacts')