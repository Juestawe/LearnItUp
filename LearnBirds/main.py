import glob
from helpers import get_bird_number, has_internet, missingGermanNames, increment_array
from setup import get_name_dict, get_number_arrays, get_probabs
import os
from initiate import create_base_files
import random
import numpy as np
from pydub import AudioSegment
from pydub.playback import play
from fuzzywuzzy import process

#language = input("Which language will you be learning in?\nIn welcher Sprache möchtest du lernen?\neng/deu?\n")
language = "deu"
random.seed()
lastTen = [0] * 10

if not os.path.exists("birdNames.txt") and has_internet():
    create_base_files()
elif not os.path.exists("birdNames.txt") and not has_internet():
    if language == "eng":
        print("Can't create birdNames.txt without internet connection")
    elif language == "deu":
        print("birdNames.txt kann ohne Internet nicht erstellt werden")
else:
    birdNameDict = get_name_dict()
    possible_inputs = []
    if language == "deu":
        for key in birdNameDict.keys():
            possible_inputs.append(birdNameDict[key][0])
    elif language == "eng":
        for key in birdNameDict.keys():
            possible_inputs.append(birdNameDict[key][1])
    numberList, nameList = get_number_arrays()
    numbers, probabilities = get_probabs()
    os.chdir("BirdSounds")
    textFiles = glob.glob("*.wav")
    sample = np.random.choice(numbers, size=1, p=probabilities)
    for k, textFile in enumerate(textFiles):
        nr = get_bird_number(textFile)
        if nr == sample[0]:
            audioFile = textFiles[k]
            break
    audio = AudioSegment.from_file(audioFile, format="wav")
    # play(audio)
    # print(nameList)
    # print(numberList)
    if language == "deu":
        user_input = input("Welcher Vogel sang das gegebene?:\n")
    elif language == "eng":
        user_input = input("Which bird sang that:\n")

    # Get the best match with a score
    best_match, score = process.extractOne(user_input, possible_inputs)

    if score > 70:  # Adjust threshold as needed
        print(f"Did you mean '{best_match}'? (Confidence: {score}%)")
    else:
        print("No good match found.")
