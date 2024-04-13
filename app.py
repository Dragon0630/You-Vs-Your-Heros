from flask import Flask, render_template, request, jsonify, send_from_directory, g
from classes import modify_json as JSON
import json
from classes.computation import Computation
import logging
#from classes.generate_image import generate_image

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("base.html")

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
    indexNumber = comp.randomNumber()
    results = comp.compare()
    hero_name = results['hero_name']
    score_result = results['score_result']
    #generate_image()
    return render_template("page2.html", heroName=hero_name, scoreResult=score_result, safeHeroName=results['safe_hero_name'], choice=indexNumber)

@app.route('/get_player_stats', methods = ['GET'])
def get_player_stats():
    with open(r'.\\info\\user_info\\user_info.json', 'r') as json_file:
        data = json.load(json_file)
    return jsonify(data)



@app.route('/get_hero_stats/<hero_name>', methods = ['POST', 'GET'])
def get_hero_stats(hero_name):
    hero_file_path = fr'./info/character_info/{hero_name}/{hero_name}.json'
    try:
        with open(hero_file_path, 'r') as hero_file:
            hero_data = json.load(hero_file)
        return jsonify(hero_data)
    except FileNotFoundError:
        logging.error(f'File not found: {hero_file_path}')  # Log the error
        return jsonify({'error': 'Hero not found'}), 404


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