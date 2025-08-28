from flask import render_template
from app.services.csv_analyze import aptos


def init_routes(app):
    @app.route('/')
    def home():
        return render_template('index.html', nomes=aptos())

    @app.route('/about')
    def about():
        return "About"