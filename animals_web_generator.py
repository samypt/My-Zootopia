import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def itterate(data):
    for animal in data:
        print('Name: ', animal['name'])
        print('Diet: ',animal['characteristics']['diet'])
        print('Location: ',animal['locations'][0])
        if 'type' in animal['characteristics']:
            print('Type: ',animal['characteristics']['type'])
        print('\n')



itterate(load_data("animals_data.json"))