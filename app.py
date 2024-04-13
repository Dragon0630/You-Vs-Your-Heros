from flask import Flask, render_template, request, jsonify
import classes.modify_json as JSON

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("base.html")

@app.route('/modify', methods = ['POST'])
def update_text():
    if request.method == 'POST':
        JSON.modify_json.__init__(request.get_json())
    else:
        return 405

if __name__ == "__main__":
    app.run(debug=True)