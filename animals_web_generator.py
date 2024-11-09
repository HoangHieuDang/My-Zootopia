import animals_database as anim

def main():
    #all_animals_list:
    #animals_list = anim.animals_html_list('animals_data.json')
    #anim.animals_list_to_HTML_file('animals_template.html', animals_list)
    #skin_type_list:
    skin_type_list = anim.animals_html_skin_type_filter_list('animals_data.json')
    anim.animals_list_to_HTML_file('animals_template.html', skin_type_list)

if __name__ == "__main__":
    main()