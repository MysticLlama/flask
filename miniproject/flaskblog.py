from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
import sqlite3 as sql

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
id=0

posts = [
	{
		'author': 'Corey Schafer',
		'title': 'Blog Post 1',
		'content': 'First post content',
		'date_posted': 'April 20, 2018'
	},
	{
		'author': 'Jane Doe',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'date_posted': 'April 21, 2018'
	}
]


@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', posts=posts)


@app.route("/about")
def about():
	return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
	global id
	conn = sql.connect("site.db")
	c=conn.cursor()
	c.execute("select max(id) from user") 
	id =c.fetchone()[0]+1
	print("id is",id)
	
	form = RegistrationForm()
	if form.validate_on_submit():
		s="insert into user values (" + str(id)+",'"+str(form.username.data)+"','"+str(form.email.data)+"','img','"+str(form.password.data)+"')"
		print("executed",s)
		
		
		id+=1
		c.execute(s)
		conn.commit()
		conn.close()
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.data == 'admin@blog.com' and form.password.data == 'password':
			flash('You have been logged in!', 'success')
			return redirect(url_for('home'))
			
		else:
			conn=sql.connect("site.db")
			c=conn.cursor()
			s= "select id from user where email ='{em}' and password = '{ps}'".format(em=form.email.data,ps=form.password.data)
			c.execute(s)
			#print(c.fetchone()!= None)
			if(c.fetchone() !=None):
				flash('You have been logged in!', 'success')
				return redirect(url_for('home'))
			else:
				flash('Login Unsuccessful. Please check username and password', 'danger')
	return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
	app.run(debug=True)
