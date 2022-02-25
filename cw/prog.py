from flask import Flask
from flask import render_template
from flask import request

from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/dashboard/<firstname>/<lastname>')
def dashboard(firstname,lastname):
   return 'welcome %s %s' %(firstname,lastname) 

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user1 = request.form['firstname']
      user2 = request.form['lastname']
      return redirect(url_for('dashboard',firstname = user1,lastname=user2))
   else:
      #user1 = request.args.get('firstname')
      #user2= request.args.get('lastname')
      return render_template('login.html')

if __name__ == '__main__':
   app.run(debug = True)