import animals_database as anim

def main():
    animals_list = anim.animals_html_list('animals_data.json')
    anim.animals_list_to_HTML_file('animals_template.html', animals_list)

if __name__ == "__main__":
    main()