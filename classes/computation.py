import json

class computation:
    def __init__():
        file_name=r'.\info\user_info\user_info.json'
        f = open(file_name)

        data = json.load(f)

        user_strength_scores = []
        user_agility_scores = []
        user_endurance_scores = []

        hero_strength_scores = []
        hero_agility_scores = []
        hero_endurance_scores = []

        for s_category in data["Strength"]:
            user_strength_scores.append(data["Strength"][s_category])
        
        for a_category in data["Agility"]:
            user_agility_scores.append(data["Agility"][a_category])

        for e_category in data["Endurance"]:
            user_endurance_scores.append(data["Endurance"][e_category])
        
        # Closing file
        f.close()