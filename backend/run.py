from app import create_app, db
from flask_migrate import Migrate
from flask import Flask

app: Flask = create_app()
migrate: Migrate = Migrate(app, db)

if __name__ == '__main__':
    """
    Main entry point for the application.
    """
    with app.app_context():
        db.create_all()
    app.run(debug=True)