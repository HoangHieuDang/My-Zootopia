import animals_database as anim
import data_fetcher as fetcher
"""
The main Zootopia Program includes
    # function to list all animals
    # function to filter animals based on skin type
    # function to search for animal using ninjas animal api
    # main function
"""
def all_animals_list():
    """
    list all animals from a json database
    """
    animals_list = anim.animals_html_list('animals_data.json')
    anim.animals_list_to_html_file('animals_template.html', animals_list)

def skin_type_filter():
    """
    filter animals according to their skin types
    """
    skin_type_list = anim.animals_html_skin_type_filter_list('animals_data.json')
    anim.animals_list_to_html_file('animals_template.html', skin_type_list)

def api_animal_search():
    """
    search an animal from ninjas animal api and put the info into a html page
    """
    input_animal = input("Please enter a name of an animal: ")
    search_animal = fetcher.search_animal_from_api(input_animal)
    anim.animals_list_to_html_file('animals_template.html', fetcher.animals_html_list_from_api(search_animal))

def main():
    """
    Main function
    """
    #----search an animal from ninjas animal api and put the info into a html page
    api_animal_search()

if __name__ == "__main__":
    main()