import glob
from helpers import get_bird_common_names, get_name_from_file, missingGermanNames, get_bird_number
import os
import random

def create_base_files():
    bird_numbers = {}
    os.chdir("BirdSounds")
    text_files = glob.glob("*.txt")
    os.chdir("..")
    bird_names = []
    for textFile in text_files:
        current_name = get_name_from_file(textFile)
        if current_name not in bird_names:
            bird_names.append(current_name)
            bird_numbers[current_name] = [get_bird_number(textFile)]
        else:
            bird_numbers[current_name].append(get_bird_number(textFile))
    with open('birdNames.txt', 'w') as file:
        for current_name in bird_names:
            name_dict = get_bird_common_names(current_name)
            if name_dict['german'] is None:
                try:
                    file.write(f"{name_dict['latin']}:{missingGermanNames[name_dict['latin']]},{name_dict['english']}\n")
                except KeyError:
                    print(f"{name_dict['latin']} does not have a German name, will be shown as 'None'")
                    file.write(f"{name_dict['latin']}:{name_dict['german']},{name_dict['english']}\n")
            else:
                file.write(f"{name_dict['latin']}:{name_dict['german']},{name_dict['english']}\n")
    with open("birdNumbers.txt", "w") as file:
        for key in bird_numbers.keys():
            file.write(f"{key}:")
            for number in bird_numbers[key]:
                file.write(f"{number},")
            file.write("\n")


def create_learning_list():
    with open("birdNames.txt", "r") as readFile:
        bird_lines = readFile.readlines()
        bird_randoms = random.sample(bird_lines, 3)
    with open("learningBirds.txt", "w") as writeFile:
        for line in bird_randoms:
            writeFile.write(line)