import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)

def single_animal_html_serialize(animal):
    """
    serialize the data of one single animal from animal data object
    put the following information into a html list element:
       - Name
       - Diet
       - The first location from the locations list
       - Type
       if one of these fields doesn't exist, don't print it
    """
    animals_str_for_display = ""
    animals_str_for_display += "<li class='cards__item'>"
    if "name" in animal:
        animals_str_for_display += f"<div class='card__title'>{animal['name']}</div>"
    animals_str_for_display += "<p class='card__text'>"
    animals_str_for_display += "<ul class='card__text__ul'>"
    if "diet" in animal["characteristics"]:
        animals_str_for_display += f"<li class='ul__list__item'>Diet: {animal['characteristics']['diet']}</li>"
    if "type" in animal["characteristics"]:
        animals_str_for_display += f"<li class='ul__list__item'>Type: {animal['characteristics']['type']}</li>"
    if "locations" in animal:
        if animal["locations"]:
            animals_str_for_display += f"<li class='ul__list__item'>location: {animal['locations'][0]}</li>"
    animals_str_for_display += "</ul>"
    animals_str_for_display += "</p>"
    animals_str_for_display += "</li>"
    return animals_str_for_display

def animals_html_list(file_path):
    """
    reading the content of the json file
    iterate through the animal data
    return the list of animals and their information as HTML list elements
    """
    animals_html_list = ""
    animals_data = load_data(file_path)
    for animal in animals_data:
        animals_html_list += single_animal_html_serialize(animal)
    return animals_html_list

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



