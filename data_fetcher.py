import requests
import animals_database
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv('API_KEY')
"""
Includes:
    # Function to fetch data from ninjas animal api and return the parsed json data
    # Function to search an animal and get information about that animal from ninjas animal api
"""
def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    """
    api_url = 'https://api.api-ninjas.com/v1/animals?name={}'.format(animal_name)
    response = requests.get(api_url, headers={'X-Api-Key': API_KEY})
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
    if fetch_data(animal_str):
        return True,fetch_data(animal_str)
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
            html_list += animals_database.single_animal_html_serialize(animal)
        return html_list
    else:
        html_list += f"<h2>The animal '{input_animal}' doesn't exist!</h2>"
        return html_list