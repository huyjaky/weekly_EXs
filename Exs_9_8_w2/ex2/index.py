

def input_data ():
    str_data = input('Enter the string u want: ')

    characters_list = list(str_data)
    characters_dict = {key: None for key in characters_list}
    
    for character in characters_list:
        number_charact_in_str = str_data.count(character)

        characters_dict.update({character: number_charact_in_str})
    print(characters_dict)
