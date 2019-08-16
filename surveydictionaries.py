import json
import pickle

survey_list = []

while True:
    name = input("What is your name?: ")
    fav_band = input("What is your favorite band?: ")
    fav_artist = input("Who is your favorite solo artist?: ")
    fav_genre = input("What is your favorite genre of music?: ")

    survey_dict = {}

    survey_dict['name'] = name
    survey_dict['band'] = fav_band
    survey_dict['artist'] = fav_artist
    survey_dict['genre'] = fav_genre

    survey_list.append(survey_dict)
    f = open("survey.json", "w")
    dictionarytoJson = json.dumps(survey_dict)
    json.dump(dictionarytoJson, f)
    print(dictionarytoJson)
    f.close()

    people = input("Is there another person?: ")
    if people == "yes" or people == "Yes":
        continue
    else:
        break
    
