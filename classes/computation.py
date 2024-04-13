import json
import random

class Computation:
    def __init__(self):
        self.file_name = './info/user_info/user_info.json'
        self.user_data = self.load_json(self.file_name)
        self.hero_data = None
        self.characters = [
            "A_Minion", "Ash_Ketchum", "Barney_The_Dinosaur", "Chani", "Clone_Trooper",
            "Frank_Castle", "Frodo_Baggins", "Gaston", "Gimli", "Gru",
            "Hiccup", "Jack_Sparrow", "Jar_Jar_Binks", "John_Wick", "Joker",
            "Legolas", "Maui", "Mr_Incredible", "Paul_Atreides", "Shrek",
            "Snorlax", "spiderman"
        ]

    def load_json(self, file_path):
        with open(file_path, 'r') as file:
            return json.load(file)

    def choose_hero(self):
        chosen_hero = random.choice(self.characters)
        hero_file = f'./info/character_info/{chosen_hero}/{chosen_hero}.json'
        self.hero_data = self.load_json(hero_file)

    def calculate_scores(self):
        user_score = 0
        hero_score = 0

        for category in ["Strength", "Agility", "Endurance"]:
            user_scores = self.user_data.get(category, {})
            hero_scores = self.hero_data.get(category, {})

            for key, user_val in user_scores.items():
                hero_val = hero_scores.get(key, 0)  # Default to 0 if not present

                # Ensure both values are integers before comparison
                try:
                    user_val = int(user_val)
                    hero_val = int(hero_val)
                except ValueError:
                    print(f"Error converting scores to integers: user_val={user_val}, hero_val={hero_val}")
                    continue  # Skip this iteration if there's a conversion error

                if user_val > hero_val:
                    user_score += 1
                elif user_val < hero_val:
                    hero_score += 1

        return "User" if user_score > hero_score else "Hero"

    def compare(self):
        self.choose_hero()
        score_result = self.calculate_scores()
        hero_name = self.hero_data.get("name", "Unknown Hero")  # Safer access
        return {'hero_name': hero_name, 'score_result': score_result}

# Usage
if __name__ == "__main__":
    comp = Computation()
    result = comp.compare()
    print(f"The winner is: {result}")