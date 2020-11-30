from flask import Flask, render_template, send_from_directory
import os

#Metodo para trabajar con el servidor local
app = Flask(__name__)

#Rutas

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/projects')
def projects():
	return render_template('projects.html')

#Inicio del servidor
if __name__ == '__main__':
	app.run(debug= True)