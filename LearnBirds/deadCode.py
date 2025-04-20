while True:
    try:
        if language == "eng":
            birdNumber = int(input("With how many birds would you like to start learning?"))
            if birdNumber in startNumbers:
                break
        elif language == "deu":
            birdNumber = int(input("Mit wie vielen Vögeln möchtest du starten?"))
            if birdNumber in startNumbers:
                break
    except (ValueError, TypeError):
        if language == "eng":
            print(f"Your input could not be converted into a number between 1 and {birdNumber}")
        elif language == "deu":
            print(f"Deine Eingabe konnte nicht in eine Zahl zwischen 1 und {birdNumber} konvertiert werden")
while True:
    if language == "eng":
        chooseBirds = input("Do you want to choose the birds to start with yourself? (y/n)")
        if chooseBirds not in allowedChoiceAnswers:
            print("Your input is not interpretable as a valid answer")
            continue
        break
    elif language == "deu":
        chooseBirds = input("Möchtest du die Startvögel selbst auswählen? (j/n)")
        if chooseBirds not in allowedChoiceAnswers:
            print("Deine Eingabe ist nicht als eine valide Antwort interpretierbar")
            continue
        break
with open("learningList.txt", "w") as writeFile:
    with open("birdNames.txt", "r") as readFile:
        if chooseBirds == "n":
            #lineNumbers =
            pass