from flask import Flask, render_template, request
import utils


app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route("/responce")
def responce():
	if request.method == "GET" and 'question' in request.args and request.args.get('question') != '':
		query = request.args.get('question')
	else:
		query = "Who played spiderman" #default if none entered
	responce = utils.getResult(query)

	return render_template("responce.html", question=query, answer=responce)

if __name__ == "__main__":
    app.debug = True
    app.run('0.0.0.0', port=8000)
