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


def access_data(data):
    output = ""
    for animal in data:
        output += '<li class="cards__item">'
        output += f'<div class="card__title">{animal["name"]}</div>\n'
        output += f'<p class="card__text">'
        output += f"<strong>Diet:</strong> {animal['characteristics']['diet']}<br/>\n"
        output += f"<strong>Location:</strong> {animal['locations'][0]}<br/>\n"
        if 'type' in animal['characteristics']:
            output += f"<strong>Type:</strong> {animal['characteristics']['type']}<br/>\n"
        output += "</p>\n"
        output += '</li>\n'
    return output


new_data = load_template(HTML_TEMPLATE).replace(REPLACEMENT,access_data(load_data(JSON_PATH)))
save_template(NEW_HTML_TEMPLATE, new_data)