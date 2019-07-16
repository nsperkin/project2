import os

from flask import Flask, render_template, session, redirect, url_for, request
from flask_session import Session
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

channels = {}

if __name__ == '__main__':
	socketio.run(app)

@app.route("/")
def index():
	if 'displayname' in session:
		return redirect(url_for('home'))
	else:
		return render_template('index.html')

@app.route("/login", methods=["POST"])
def login():
	session['displayname'] = request.form.get("displayname")
	session['lastChannel'] = ""
	return redirect(url_for('home'))

@app.route("/logout")
def logout():
	session.pop('displayname', None)
	return render_template("index.html")

@app.route("/home")
def home():
	if 'displayname' in session:
		if session['lastChannel'] != "":
			return redirect('channel', name=session['lastChannel'])
		else:
			return render_template('home.html', chan=channels, message="No Channel Selected!")
	else:
		return render_template('index.html')

@app.route("/newChannel", methods=["POST"])
def newChannel():
	channel = request.form.get("channel")
	channels.update({channel:[]})

	return redirect(url_for('channel', name=channel))


@app.route("/channel/<string:name>")
def channel(name):
	if "displayname" in session:
		session['lastChannel'] = name
		return render_template('home.html', chan=channels, message=name)
	else:
		return render_template('index.html')

@socketio.on('submit message')
def messsage(data):
	message = data["message"]
	print("================================")
	print(message)
	displayname = session["displayname"]
	emit("announce message", {"message": message, "displayname": displayname}, broadcast=True)