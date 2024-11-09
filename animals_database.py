import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def animals_list_display(file_path):
    """reading the content of the json file
       print out the list of animals and their following informations:
       - Name
       - Diet
       - The first location from the locations list
       - Type
       if one of these fields doesn't exist, don't print it
    """
    animals_data = load_data(file_path)
    animals_display_str = "\n____Animal List____\n"
    for animal in animals_data:
        if "name" in animal:
            animals_display_str += f"name: {animal['name']}\n"
        if "diet" in animal["characteristics"]:
            animals_display_str += f"diet: {animal['characteristics']['diet']}\n"
        if "type" in animal["characteristics"]:
            animals_display_str += f"type: {animal['characteristics']['type']}\n"
        if "locations" in animal:
            if animal["locations"]:
                animals_display_str += f"location: {animal['locations'][0]}\n"
        animals_display_str += "___________________\n"
    return animals_display_str

"""
def animals_list_to_HTML_file(file_path, animals_data_str):
    if file_path.endswith('.html'):
        with open(file_path, "r") as fileobj:
            html_data = fileobj.read()
    else:
        print("\n please input an html file\n")
        return None
    html_data.replace("__REPLACE_ANIMALS_INFO__", animals_data_str)
    with open(file_path, "w") as fileobj:
        fileobj.write(html_data)
"""


