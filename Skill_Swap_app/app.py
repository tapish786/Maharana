from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'your_secret_key'

db = SQLAlchemy(app)

from routes.auth import auth_bp
from routes.users import users_bp
from routes.swaps import swaps_bp

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(users_bp, url_prefix='/users')
app.register_blueprint(swaps_bp, url_prefix='/swaps')

@app.route('/')
def home():
    return 'Skill Swap App is running!'


if __name__ == '__main__':
    # 🔁 Lazy import to avoid circular import
    from routes.users import users_bp
    from routes.auth import auth_bp
    from routes.swapes import swapes_bp

    # Register blueprints
    app.register_blueprint(users_bp, url_prefix='/users')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(swapes_bp, url_prefix='/swapes')

    # 🧠 Create DB tables inside context
    with app.app_context():
        db.create_all()

    app.run(debug=True)
