import json

NEW_HTML_TEMPLATE = "animals.html"

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

def load_template(file_path):
    with open(file_path, "r") as handle:
        return handle.read()

def save_template(file_path, content):
    with open(file_path, "w") as handle:
        handle.write(content)


def access_data(data):
    output = ""
    for animal in data:
        output += '<li class="cards__item">'
        output += f"Name: {animal['name']}<br/>\n"
        output += f"Diet: {animal['characteristics']['diet']}<br/>\n"
        output += f"Location: {animal['locations'][0]}<br/>\n"
        if 'type' in animal['characteristics']:
            output += f"Type: {animal['characteristics']['type']}<br/>\n"
        output += "<br/>\n"
        output += '</li>'
    return output


new_data = load_template("animals_template.html").replace("__REPLACE_ANIMALS_INFO__",access_data(load_data("animals_data.json")))
save_template(NEW_HTML_TEMPLATE, new_data)