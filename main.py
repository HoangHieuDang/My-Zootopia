import animals_database as anim

def main():
    animals_list = anim.animals_list_display('animals_data.json')
    #print(animals_list)
    anim.animals_list_to_HTML_file('animals_template.html', animals_list)

if __name__ == "__main__":
    main()