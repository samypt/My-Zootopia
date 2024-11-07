import json
import data_fetcher


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
    print(f'Website was successfully generated to the file {file_path}.')


def serialize_animal(animal_obj):
    """Generates well-structured HTML for a single animal."""
    details = [
        f"<li><p class='card__text'><strong>Diet:</strong> {animal_obj['characteristics'].get('diet', 'N/A')}</p></li>",
        f"<li><p class='card__text'><strong>Location:</strong> {animal_obj['locations'][0] if animal_obj['locations'] else 'Unknown'}</p></li>"
    ]
    if animal_type := animal_obj['characteristics'].get('type'):
        details.append(f"<li><p class='card__text'><strong>Type:</strong> {animal_type}</p></li>")

    return (
        '<li class="cards__item">\n'
        f'  <div class="card__title">{animal_obj["name"]}</div>\n'
        '    <ul>\n' +
        ''.join(f'      {detail}\n' for detail in details) +
        '    </ul>\n'
        '</li>\n'
    )


def access_data(data):
    """Generates HTML for a list of animals."""
    return "".join(serialize_animal(animal_obj) for animal_obj in data)


def main():
    animal = input('Enter a name of an animal: ')
    fetched_data = data_fetcher.fetch_data(animal)
    if not fetched_data:
        animal_data = f"<h2>The animal {animal} doesn't exist.</h2>"
    else:
        animal_data = access_data(fetched_data)
    # Load template and replace placeholder with animal data
    new_content = load_template(HTML_TEMPLATE).replace(REPLACEMENT, animal_data)
    save_template(NEW_HTML_TEMPLATE, new_content)


if __name__ == '__main__':
    main()
