import animals_database as anim

def main():
    #all_animals_list:
    #animals_list = anim.animals_html_list('animals_data.json')
    #anim.animals_list_to_HTML_file('animals_template.html', animals_list)
    #skin_type_list:
    #skin_type_list = anim.animals_html_skin_type_filter_list('animals_data.json')
    #anim.animals_list_to_HTML_file('animals_template.html', skin_type_list)
    #print(anim.animal_info_from_api("fox"))
    input_animal = input("Please enter a name of an animal: ")
    search_animal = anim.search_animal_from_api(input_animal)
    anim.animals_list_to_html_file('animals_template.html', anim.animals_html_list_from_api(search_animal))

if __name__ == "__main__":
    main()