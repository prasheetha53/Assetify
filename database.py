# app.py

from flask import Flask
from flask_mongoengine import MongoEngine
from routes.settings import settings  # Assuming you have a settings blueprint
from routes.register import register  # Assuming you have a register blueprint
from routes.login import login        # Assuming you have a login blueprint
from .ai_service import ai_service  # Assuming you have an AI service blueprint

app = Flask(__name__)

# Database configuration
app.config['MONGODB_SETTINGS'] = {
    'db': 'assetify_db',  # Change this to your database name
    'host': 'localhost',
    'port': 27017,
    'username': 'your_username',  # Optional: Add credentials if required
    'password': 'your_password'
}

# Initialize MongoEngine
db = MongoEngine(app)

# Register blueprints
app.register_blueprint(settings)
app.register_blueprint(register)
app.register_blueprint(login)
app.register_blueprint(ai_service)

if __name__ == '__main__':
    app.run(debug=True)
