from flask import Flask, render_template, request
import numpy as np
import pandas as pd

app=Flask(__name__)

 

@app.route('/')
def home1():
    return  render_template("login.html")
database={'Dasitha@123':'123','Sithumi@234':'234','Pavanthi@345':'345', '2018y14510':'123456'}

@app.route('/form_login',methods=['POST','GET'])
def login():
    name1=request.form['username']
    pwd=request.form['password']
    if name1 in database:
	    return render_template('index.html',name=name1)

@app.route('/logout')
def logout():
    return render_template("login.html")
	        
if __name__=="__main__":
    app.run(debug=True)
    

