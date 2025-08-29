from flask import render_template
from app.services.csv_analyze import campi, aptos_por_campus


def init_routes(app):
    @app.route('/')
    def home():
        return render_template('index.html', campi=campi())

    @app.route('/classificados/<campus>')
    def about(campus):
        return render_template('aptos_por_campus.html', campus=campus, nomes=aptos_por_campus(campus))