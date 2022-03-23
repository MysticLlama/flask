import sqlite3 as sql
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
id=0
admin = False

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
    global admin
    if not admin:
        return render_template('home.html', posts=posts)
    conn = sql.connect("site.db")
    c=conn.cursor()
    s=[]
    for row in c.execute("select * from user"):
        s.append(str(row[1])+" : "+str(row[2]))
    return render_template("about.html",text=s)


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
    #print("id is",id)
    form = RegistrationForm()
    if form.validate_on_submit():
        ts= "select username from user where username='"+str(form.username.data)+"'"
        c.execute(ts)
        res=c.fetchone()[0]
        print(res)
        if res == str(form.username.data):
            flash(f'Username is taken!','danger')
            conn.close()
            return render_template('register.html', title='Register', form=form)
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
    global admin
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            admin =True
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        admin = False
        conn=sql.connect("site.db")
        c=conn.cursor()
        s= "select id from user where email ='{em}' and password = '{ps}'".format(em=form.email.data,ps=form.password.data)
        c.execute(s)
        #print(c.fetchone()!= None)
        if c.fetchone() is not None:
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
