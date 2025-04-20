import requests
import os

missingGermanNames = {
    "Troglodytes troglodytes": "Zaunkönig",
    "Phylloscopus collybita": "Zilpzalp",
    "Erithacus rubecula": "Rotkehlchen",
    "Sylvia atricapilla": "Mönchsgrasmücke",
    "Oriolus oriolus": "Pirol",
    "Turdus pilaris": "Wacholderdrossel",
    "Regulus ignicapilla": "Sommergoldhähnchen"
}


def get_bird_common_names(latin_name):
    # Step 1: Match the scientific name to get the species key
    match_url = f"https://api.gbif.org/v1/species/match?name={latin_name}"
    match_response = requests.get(match_url).json()
    
    if "speciesKey" not in match_response:
        return {"error": "Species not found in GBIF"}
    
    species_key = match_response["speciesKey"]
    
    # Step 2: Fetch vernacular names using the species key
    vernac_url = f"https://api.gbif.org/v1/species/{species_key}/vernacularNames"
    vernac_response = requests.get(vernac_url).json()
    
    # Extract English and German names
    names = {
        "latin": latin_name,
        "english": None,
        "german": None
    }
    
    for entry in vernac_response.get("results", []):
        if entry.get("language") == "eng":
            names["english"] = entry.get("vernacularName")
        elif entry.get("language") == "deu":
            names["german"] = entry.get("vernacularName")
    
    return names


def get_name_from_file(file_name):
    os.chdir("BirdSounds")

    file = open(file_name)
    line = file.readline()
    start_read_index = line.find("species")+len("species':'")
    end_read_index = line[start_read_index:].find('"') + start_read_index
    
    species = line[start_read_index:end_read_index]
    os.chdir("..")
    return species.split(";")[1]


def has_internet():
    try:
        # Try to connect to a reliable server with a short timeout
        requests.get("https://api.gbif.org", timeout=3)
        return True
    except (requests.ConnectionError, requests.Timeout):
        return False

def get_bird_number(file_name):
    start_index = file_name.find("recording_") + len("recording_")
    end_index = file_name.find(".")
    return file_name[start_index:end_index]