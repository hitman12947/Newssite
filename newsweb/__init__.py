from flask import Flask, render_template as render, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_json('config.json')
db = SQLAlchemy(app)

from newsweb import routes


if __name__ == "__main__":
    app.run(debug=True)
