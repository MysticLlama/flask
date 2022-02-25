from flask import Flask


app=Flask(__name__)

@app.route("/")
def hi():
	return "<p>Hi</p>"
	
	
	
@app.route("/meme")
def howdy():
	return "<a href=\"{{url_for('/')}}\" >Login</a>"
	
	
	
	
if __name__ == "__main__":
	app.run(debug=True)