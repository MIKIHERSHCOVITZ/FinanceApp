from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = 'your_secret_key'

    # Initialize the database
    from financeapp.db import init_db
    init_db()

    # Import the views
    from financeapp.views import main_bp

    # Register the blueprint
    app.register_blueprint(main_bp)

    return app
