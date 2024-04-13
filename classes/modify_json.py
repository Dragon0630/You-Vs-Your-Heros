from flask import jsonify
import json
import requests
import sqlite3

#api key MdfoNfYe3KAEiHy0FaRvS6o6THPuR8DoWasEp1sF

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
        response_data = {'name': name, 'curl':curl, 'squat': squat, 'bench':bench, 'run':run, 'swim': swim, 'climb':climb, 'sprint':sprint, 'jump':jump, 'reaction':reaction }
        
        json_object = json.dumps(response_data)
        file_name=r'.\info\user_info\user_info.json'

        with open(file_name, 'w') as outfile:
            outfile.write(json_object)

        return response_data
  