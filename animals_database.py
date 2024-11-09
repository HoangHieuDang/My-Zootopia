import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def animals_list_display(file_path):
    """reading the content of the json file
       print out the list of animals and their following information:
       - Name
       - Diet
       - The first location from the locations list
       - Type
       if one of these fields doesn't exist, don't print it
    """
    animals_data = load_data(file_path)
    animals_str_for_display = ""
    for animal in animals_data:
        if "name" in animal:
            animals_str_for_display += f"name: {animal['name']}\n"
        if "diet" in animal["characteristics"]:
            animals_str_for_display += f"diet: {animal['characteristics']['diet']}"
        if "type" in animal["characteristics"]:
            animals_str_for_display += f"type: {animal['characteristics']['type']}"
        if "locations" in animal:
            if animal["locations"]:
                animals_str_for_display += f"location: {animal['locations'][0]}"
    return animals_str_for_display


def animals_list_to_HTML_file(file_path, animals_data_str):
    """
    Input the animal list into an HTML File by
    replacing the string '__REPLACE_ANIMALS_INFO__'
    with the animal list
    """
    if file_path.endswith('.html'):
        print("Valid HTML file")
        with open(file_path, "r") as fileobj:
            html_data = fileobj.read()
    else:
        print("\n please input an html file\n")
        return None
    if '__REPLACE_ANIMALS_INFO__' in html_data:
        print("Replace animals info exists")
        new_html_data = html_data.replace("__REPLACE_ANIMALS_INFO__", animals_data_str)
        with open(file_path, "w") as fileobj:
            fileobj.write(new_html_data)
        return True
    else: print("String to replace not found in the HTML !")



