from flask import Flask, render_template, request
import classes.modify_json as JSON

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("base.html")

@app.route('/modify')
def update_text():
    if request.method == 'POST':
        name = request.form['name']
        squat = request.form['squat']
    #         var curl = document.getElementById('curl').value;
    # var squat = document.getElementById('squat').value;
    # var bench = document.getElementById('bench').value;
    # var run = document.getElementById('run').value;
    # var swim = document.getElementById('swim').value;
    # var climb = document.getElementById('climb').value;
    # var sprint = document.getElementById('sprint').value;
    # var jump = document.getElementById('jump').value;
    # var reaction = document.getElementById('reaction').value;
        # Do something with the data (e.g., save it to a JSON file)
        response_data = {'message': 'Data received successfully', 'name': name}
        return jsonify(response_data), 200
    else:
        return jsonify({'error': 'Method not allowed'}), 405

if __name__ == "__main__":
    app.run(debug=True)