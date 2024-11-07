import json

HTML_TEMPLATE = "animals_template.html"
JSON_PATH = "animals_data.json"
NEW_HTML_TEMPLATE = "animals.html"
REPLACEMENT = "__REPLACE_ANIMALS_INFO__"


def load_data(file_path):
    """ Loads a JSON file with UTF-8 encoding """
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def load_template(file_path):
    """ Loads an HTML template with UTF-8 encoding """
    with open(file_path, "r", encoding="utf-8") as handle:
        return handle.read()


def save_template(file_path, content):
    """ Saves an HTML file with UTF-8 encoding """
    with open(file_path, "w", encoding="utf-8") as handle:
        handle.write(content)


def serialize_animal(animal_obj):
    output = ""
    output += '<li class="cards__item">'
    output += f'<div class="card__title">{animal_obj["name"]}</div>\n'
    output += f'<p class="card__text">'
    output += '<ul>'
    output += f"<li><strong>Diet:</strong> {animal_obj['characteristics']['diet']}</li><br/>\n"
    output += f"<li><strong>Location:</strong> {animal_obj['locations'][0]}</li><br/>\n"
    if 'type' in animal_obj['characteristics']:
        output += f"<li><strong>Type:</strong> {animal_obj['characteristics']['type']}</li><br/>\n"
    output += '</ul>'
    output += "</p>\n"
    output += '</li>\n'
    return output


def access_data(data):
    output = ""
    for animal_obj in data:
        output += serialize_animal(animal_obj)
    return output


new_data = load_template(HTML_TEMPLATE).replace(REPLACEMENT,access_data(load_data(JSON_PATH)))
save_template(NEW_HTML_TEMPLATE, new_data)