
#Егор / пока что веб простаиваится из-за лени остальных участников, привет Ване и Мише

from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def firstone():
    return render_template("test1.html")
if __name__ == "__main__":
    app.run(debug=True)