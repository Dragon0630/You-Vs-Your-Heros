from flask import Flask, render_template, request, jsonify
import classes.modify_json as JSON

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("base.html")

@app.route('/modify', methods = ['POST'])
def update_text():
    if request.method == 'POST':
        name = request.form['name']
        response_data = {'message': 'Data received successfully', 'name': name}
        return jsonify(response_data), 200
    else:
        return jsonify({'error': 'Method not allowed'}), 405

if __name__ == "__main__":
    app.run(debug=True)