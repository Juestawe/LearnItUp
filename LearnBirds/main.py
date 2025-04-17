import glob
from helpers import get_bird_common_names, get_name_from_file, has_internet, missingGermanNames
import os

os.chdir("BirdSounds")
textFiles = glob.glob("*.txt")
os.chdir("..")
birdNames = []
for textFile in textFiles:
    currentName = get_name_from_file(textFile)
    if currentName not in birdNames:
        birdNames.append(currentName)

with open('birdNames.txt', 'w') as file:
    for currentName in birdNames:
        nameDict = get_bird_common_names(currentName)
        if nameDict['german'] == None:
            file.write(f"{nameDict['latin']}:{missingGermanNames[nameDict['latin']]},{nameDict['english']}\n")
        else:
            file.write(f"{nameDict['latin']}:{nameDict['german']},{nameDict['english']}\n")

#print(get_name_from_file("birdnet_mobile_4209716759_recording_0.txt"))


