import json
import requests

def animal_info_from_api(animal):
    """
    Get the information of the input animal from api-ninjas animals api
    return the parsed json data
    """
    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(animal)
    response = requests.get(api_url, headers={'X-Api-Key': 'EIKjltF0DIx93gB/45wrYg==4s7vkTmEkPzqRMgM'})
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)
        return None

def search_animal_from_api(animal_str):
    """
    handles user's choice of animal and get the animal's info
    return the json file which was gotten from the api and a boolean flag to
    signal the existence of the animal in the database
    """
    if animal_info_from_api(animal_str):
        return True,animal_info_from_api(animal_str)
    else:
        return False,animal_str

def animals_html_list_from_api(search_animal_result_tuple):
    """
    reading the content of the parsed json animal data
    from the search_animal_from_api function's returned tuple
    iterate through the animal data
    return the list of animals and their information as HTML list elements
    """
    is_animal_exist,input_animal = search_animal_result_tuple
    html_list = ""
    if is_animal_exist:
        for animal in input_animal:
            html_list += single_animal_html_serialize(animal)
        return html_list
    else:
        html_list += f"<h2>The animal '{input_animal}' doesn't exist!</h2>"
        return html_list

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
    html_list = ""
    animals_data = load_data(file_path)
    for animal in animals_data:
        html_list += single_animal_html_serialize(animal)
    return html_list

def animals_html_skin_type_filter_list(json_file_path):
    """
    reading the content of the json file
    iterate through the animal data
    displaying the possible skin type to choose from
    return the list of animals and their information as HTML list elements
    """
    #load the data from the file path
    animals_data = load_data(json_file_path)

    #getting a unique set of all skin types
    skin_type_set = set()
    skin_type_display = "\nList of all skin types:\n"
    for animal in animals_data:
        if "skin_type" in animal["characteristics"]:
            if animal["characteristics"]["skin_type"].lower() not in skin_type_display:
                skin_type_display += f"{animal['characteristics']['skin_type'].lower()}\n"
            skin_type_set.add(animal["characteristics"]["skin_type"].lower())
    print(skin_type_display)
    skin_type = input("Please choose one skin type from the list above: ")

    #check if user's skin_type input exists in the list:
    if skin_type.lower() in skin_type_set:
        # create 2 html serialized lists: 1 list for skin type, 1 list for unknown skin type
        animals_skin_type_chosen = f"<h2>Animals with skin type {skin_type}</h2>"
        animals_skin_type_unknown = f"<h2>Animals with unknown skin type</h2>"
        #create counter unknown, if unknown == 0, print out a html <p> element
        #to inform that there is no animal with unknown skin type
        unknown = 0
        for animal in animals_data:
            if "skin_type" in animal["characteristics"]:
                if animal["characteristics"]["skin_type"].lower() == skin_type:
                    animals_skin_type_chosen += single_animal_html_serialize(animal)
            else:
                unknown += 1
                animals_skin_type_unknown += single_animal_html_serialize(animal)
        if unknown == 0:
            animals_skin_type_unknown += f"<div class='card__title'><p>NONE</p></div>"
        animals_final_list = animals_skin_type_chosen + animals_skin_type_unknown
        return animals_final_list
    else:
        print("the input skin-type doesn't exist in the database, please try again")
        return None

def animals_list_to_html_file(html_file_path, html_animals_data_str):
    """
    Input the animal list into an HTML File by
    replacing the string '__REPLACE_ANIMALS_INFO__'
    with the animal list
    """
    #check if the input file a html file or not
    if html_file_path.endswith('.html'):
        print("Valid HTML file")
        with open(html_file_path, "r") as fileobj:
            html_data = fileobj.read()
    else:
        print("\n please input an html file\n")
        return None
    #Check if placeholder for template replacement exists in the html file
    if '__REPLACE_ANIMALS_INFO__' in html_data:
        #replace the html serialized string to the __REPLACE_ANIMALS_INFO__ placeholder in html file
        new_html_data = html_data.replace("__REPLACE_ANIMALS_INFO__", html_animals_data_str)
        try:
            with open(html_file_path, "w") as fileobj:
                fileobj.write(new_html_data)
        except Exception as a:
            print("Something is wrong when trying to write into HTML: " + str(a))
            return False
        else:
            print("Website was successfully generated to the file animals.html.")
            return True
    else:
        print("String to replace not found in the HTML !")
        return False



