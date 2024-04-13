from flask import jsonify
import json


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
        response_data = {'name': name, 'curl':curl, 'squat': squat, 'bench':bench, 'run':run, 
                         'swim': swim, 'climb':climb, 'sprint':sprint, 'jump':jump, 'reaction':reaction }
        
        json_object = json.dumps(response_data)

        with open('/info/user_info/user_info.json') as outfile:
            outfile.write(json_object)

        return response_data
