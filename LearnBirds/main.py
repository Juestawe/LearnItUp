import glob
from helpers import get_bird_common_names, get_name_from_file, has_internet, missingGermanNames
import os
from initiate import create_base_files, create_learning_list
import random
from pydub import AudioSegment
from pydub.playback import play

language = input("Which language will you be learning in?\nIn welcher Sprache möchtest du lernen?\neng/deu?\n")
random.seed()

if not os.path.exists("birdNames.txt") and has_internet():
    create_base_files()
elif not os.path.exists("birdNames.txt") and not has_internet():
    if language == "eng":
        print("Can't create birdNames.txt without internet connection")
    elif language == "deu":
        print("birdNames.txt kann ohne Internet nicht erstellt werden")
elif not os.path.exists("learningBirds.txt"):
    create_learning_list()
else:
    pass
