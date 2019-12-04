from flask import Flask
from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app=app)
migrate = Migrate(app=app, db=db)
login = LoginManager(app=app)

from src import routes, models


@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': models.User,
        'Post': models.Post
    }

if __name__ == '__main__':
    app.run(debug=True)
