from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("base.html")

@app.route('/modify', methods = ['POST'])
def update_text():
    data = request.get_json

if __name__ == "__main__":
    app.run(debug=True)