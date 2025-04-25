import helpers
import numpy as np

numbers = []
probabilities = []

def get_probabs():
    with open("probabilities.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            colonIndex = line.find(":")
            numbers.append(line[:colonIndex])
            probabilities.append(line[colonIndex+1:-1])
    return numbers, probabilities

def get_name_dict():
    name_dict = {}
    with open("birdNames.txt") as name_file:
        name_lines = name_file.readlines()
    for line in name_lines:
        colon_index = line.find(":")
        comma_index = line.find(",")
        name_dict[line[:colon_index]] = [line[1+colon_index:comma_index], line[1+comma_index:-1]]
    return name_dict

def get_number_arrays():
    number_list = np.array([])
    name_list = np.array([])
    with open("birdNumbers.txt") as number_file:
        number_lines = number_file.readlines()
    for line in number_lines:
        colon_index = line.find(":")
        current_name = line[:colon_index]
        current_numbers = line[colon_index+1:-2].split(",")
        number_list = np.append(number_list, current_numbers)
        current_name_list = [current_name] * len(current_numbers)
        name_list = np.append(name_list, current_name_list)
    return name_list, number_list