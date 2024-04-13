import json
import random

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

        Minion = ["/../info/character_info/A_Minion/A_Minion.json"]
        Ash = ["/../info/character_info/Ash_Ketchum/Ash_Ketchum.json"]
        Barney = ["/../info/character_info/Barney_The_Dinosaur/Barney_The_Dinosaur.json"]
        Chani = ["/../info/character_info/Chani/Chani.json"]
        Clone = ["/../info/character_info/Clone_Trooper/Clone_Trooper.json"]
        Frank = ["/../info/character_info/Frank_Castle/Frank_Castle.json"]
        Frodo = ["/../info/character_info/Frodo_Baggins/Frodo_Baggins.json"]
        Gaston = ["/../info/character_info/Gaston/Gaston.json"]
        Gimli = ["/../info/character_info/Gimli/Gimli.json"]
        Gru = ["/../info/character_info/Gru/Gru.json"]
        Hiccup = ["/../info/character_info/Hiccup/Hiccup.json"]
        Jack = ["/../info/character_info/Jack_Sparrow/Jack_Sparrow.json"]
        Jar_Jar = ["/../info/character_info/Jar_Jar_Binks/Jar_Jar_Binks.json"]
        John = ["/../info/character_info/John_Wick/John_Wick.json"]
        Joker = ["/../info/character_info/Joker/Joker.json"]
        Legolas = ["/../info/character_info/Legolas/Legolas.json"]
        Maui = ["/../info/character_info/Maui/Maui.json"]
        Mr_Incredible = ["/../info/character_info/Mr_Incredible/Mr_Incredible.json"]
        Paul = ["/../info/character_info/Paul_Atreides/Paul_Atreides.json"]
        Shrek = ["/../info/character_info/Shrek/Shrek.json"]
        Snorlax = ["/../info/character_info/Snorlax/Snorlax.json"]
        Spiderman = ["/../info/character_info/spiderman/spiderman.json"]


        character_list = [Minion, Ash, Barney, Chani, Clone, Frank, Frodo, Gaston, Gimli, Gru, Hiccup, Jack, Jar_Jar, John, Joker, Legolas, Maui,
                          Mr_Incredible, Paul, Shrek, Snorlax, Spiderman]
        
        hero = random.choice(character_list)

        for user_s_category in data["Strength"]:
            user_strength_scores.append(data["Strength"][user_s_category])
        
        for user_a_category in data["Agility"]:
            user_agility_scores.append(data["Agility"][user_a_category])

        for user_e_category in data["Endurance"]:
            user_endurance_scores.append(data["Endurance"][user_e_category])

        f.close()
        f = open(hero[0])
        hero_data = json.load(f)
        
        for hero_s_category in hero_data["Strength"]:
            hero_strength_scores.append(data["Strength"][hero_s_category])
        
        for hero_a_category in hero_data["Agility"]:
            hero_agility_scores.append(data["Agility"][hero_a_category])

        for hero_e_category in hero_data["Endurance"]:
            hero_endurance_scores.append(data["Endurance"][hero_e_category])

        f.close()

        hero_score = 0
        user_score = 0
        for x in user_strength_scores:
            if user_strength_scores[x] > hero_strength_scores[x]:
                user_score += 1
            if user_strength_scores[x] < hero_strength_scores[x]:
                hero_score += 1
            else:
                pass
                
        for x in user_endurance_scores:
            if user_endurance_scores[x] > hero_endurance_scores[x]:
                user_score += 1
            if user_endurance_scores[x] < hero_endurance_scores[x]:
                hero_score += 1
            else:
                pass

        for x in user_agility_scores:
            if user_agility_scores[x] > hero_agility_scores[x]:
                user_score += 1
            if user_agility_scores[x] < hero_agility_scores[x]:
                hero_score += 1
            else:
                pass
        
        # Closing file
        