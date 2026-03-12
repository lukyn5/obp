from flask_sqlalchemy import SQLAlchemy
from flask import Flask

sql = SQLAlchemy()  # Initialize SQLAlchemy without an app


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sqlite.db'  # Example database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable track modifications to save resources
db.init_app(app)  # Initialize SQLAlchemy with the app


@app.route('/')
def home():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)