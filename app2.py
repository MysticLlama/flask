from flask import Flask
from flask import render_template


app=Flask(__name__)

#@app.route('/')
#def index():
	#return "Wowee"
	
	
@app.route('/')
@app.route('/index')
def index():
	name="Carl"
	return render_template('index.html',title='Hey',username=name)
	
	
if __name__ == "__main__":
	app.run(debug=True)