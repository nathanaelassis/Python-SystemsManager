#!/usr/bin/python3

from functools import wraps
from ldap3 import Server, Connection
from flask import Flask, render_template, request, redirect, session, g

from blueprints.docker_routes import docker_routes
from blueprints.gitlab_routes import gitlab_routes
from blueprints.jenkins_routes import jenkins_routes

app = Flask(__name__)
app.secret_key = 'TqMYB8^wbe!%cTcx3UbV!qUsZ2*#*XK6B3ZFj*zK'
app.url_map.strict_slashes = False
app.register_blueprint(docker_routes)
app.register_blueprint(gitlab_routes)
app.register_blueprint(jenkins_routes)

@app.before_request
def load_auth():
	if 'auth' in session:
		g.auth = True
	else:
		g.auth = False

@app.route('/')
def index():
    if g.auth:
        return redirect('/docker')
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    usuario = request.form['usuario']
    senha = request.form['senha']

    server = Server('27.11.90.30', use_ssl=False)
    ldap = Connection(server,
            user='uid={},dc=ldap,dc=example,dc=com'.format(usuario),
            password=senha)
    if ldap.bind():
        session['auth'] = True
        return redirect('/docker')
    else:
        return redirect('/')

@app.route('/logoff')
def logoff():
    del session['auth']
    return redirect('/')

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000, debug=True)
