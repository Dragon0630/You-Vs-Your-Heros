from flask import Flask, render_template, request, jsonify, send_from_directory
from classes import modify_json as JSON
import json
from classes import computation as comp

app = Flask(__name__)


@app.route("/You-Vs-Your-Heros/")
def home():
    return render_template("index.html")

@app.route('/You-Vs-Your-Heros/modify', methods = ['POST'])
def update_text():
    if request.method == 'POST':
        response_json = JSON.modify_json.__init__(request.get_json())
        return response_json
    else:
        return 405

@app.route('/You-Vs-Your-Heros/comparison', methods = ['GET'])
def compare():
    winner = comp.computation.__init__()
    return render_template("page2.html")


@app.route('/You-Vs-Your-Heros/get_player_stats', methods = ['GET'])
def get_player_stats():
    with open(r'.\\info\\user_info\\user_info.json', 'r') as json_file:
        data = json.load(json_file)
    return jsonify(data)

@app.route("/You-Vs-Your-Heros/webgl", methods = ['GET', 'POST'])
def index():
    return render_template("/unity/index.html")


@app.route('/unity/<path:filename>')
def serve_unity_files(filename):
    return send_from_directory('unity', filename)


if __name__ == "__main__":
    app.run(debug=True)