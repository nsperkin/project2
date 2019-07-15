import os

from flask import Flask, render_template, session, redirect, url_for
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)


@app.route("/")
def index():
	if 'displayname' in session:
		return redirect(url_for('home'))
	else:
		return render_template('index.html')

@app.route("/home")
def home():
	return render_template('home.html')