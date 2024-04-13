import os
import shutil

def create_character_folders(names):
    # Navigate to the "character_info" folder
    character_info_path = "C:\\UVsHeroes\\You-Vs-Your-Heros\\info\\character_info"
    os.makedirs(character_info_path, exist_ok=True)
    os.chdir(character_info_path)
    
    # Create folders with provided names
    for name in names:
        os.makedirs(name, exist_ok=True)
        
        # Copy and rename the template.json file to each folder
        shutil.copy2("C:\\UVsHeroes\\You-Vs-Your-Heros\\templates\\template.json", os.path.join(name, f"{name}.json"))

if __name__ == "__main__":
    names = ["Paul_Atreides", "Chani", "Joker", "Gru", "Shrek", "John_Wick", "Hiccup", "Maui", "Barney_The_Dinosaur", "Jar_Jar_Binks", "A_Minion", "Snorlax", "Ash_Ketchum", "Gaston", "Mr_Incredible", "Clone_Trooper", "Frodo_Baggins", "Jack_Sparrow", "Frank_Castle", "Legolas", "Gimli"]  # Replace with your list of names
    create_character_folders(names)
