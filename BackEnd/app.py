# backend/app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    # Importa rotas
    from routes.users import users_bp
    from routes.residues import residues_bp
    from routes.measurements import measurements_bp

    app.register_blueprint(users_bp, url_prefix='/api/users')
    app.register_blueprint(residues_bp, url_prefix='/api/residues')
    app.register_blueprint(measurements_bp, url_prefix='/api/measurements')

    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
