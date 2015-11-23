from flask import Flask, render_template
import utils

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.debug = True
    app.run('0.0.0.0', port=8000)
