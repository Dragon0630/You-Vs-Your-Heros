from flask import Flask, render_template, request, jsonify, send_from_directory
from classes import modify_json as JSON
import json
from classes.computation import Computation
#from classes.generate_image import generate_image

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("base.html")

@app.route("/tile_heroes",methods=['GET'])
def catalog():
    return render_template("tile_heroes.html")

@app.route("/profile",methods=['POST'])
def profile():
    return render_template("profile.html")

@app.route('/modify', methods = ['POST'])
def update_text():
    if request.method == 'POST':
        response_json = JSON.modify_json.__init__(request.get_json())
        return response_json
    else:
        return 405

@app.route('/comparison', methods = ['GET'])
def compare():
    comp = Computation()
    results = comp.compare()

    hero_name = results['hero_name']
    score_result = results['score_result']
    #generate_image()
    return render_template("page2.html", heroName=hero_name, scoreResult=score_result, safeHeroName=results['safe_hero_name'])

@app.route('/get_player_stats', methods = ['GET'])
def get_player_stats():
    with open(r'.\\info\\user_info\\user_info.json', 'r') as json_file:
        data = json.load(json_file)
    return jsonify(data)

@app.route("/webgl", methods = ['GET', 'POST'])
def index():
    return render_template("/unity/index.html")


@app.route('/unity/<path:filename>')
def serve_unity_files(filename):
    return send_from_directory('unity', filename)


#@app.route('/get-image')
#def get_image():
    #attributes = request.args.get('attributes')  # Assuming attributes are passed as a query parameter
    #image_path = generate_image(attributes)
    #return send_file(image_path, mimetype='image/png')


if __name__ == "__main__":
    app.run(debug=True)