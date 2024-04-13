from flask import jsonify

class modify_json:
    def __init__(data):
        name = data['name']
        curl = data['strength']['curl']
        squat = data['strength']['squat']
        bench = data['strength']['bench']
        run = data['endurance']['run']
        swim = data['endurance']['swim']
        climb = data['endurance']['climb']
        sprint = data['agility']['sprint']
        jump = data['agility']['jump']
        reaction = data['agility']['reaction']
        response_data = {'message': 'Data received successfully', 'name': name, 'curl':curl  }
        return jsonify(response_data), 200

    