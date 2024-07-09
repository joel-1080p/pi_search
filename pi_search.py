from pathlib import Path
import json

   
##########################
##########################
# T9 Style mapping.
def map_characters():
    T9_MAPPING = {
        'A': '2', 'B': '2', 'C': '2',
        'D': '3', 'E': '3', 'F': '3',
        'G': '4', 'H': '4', 'I': '4',
        'J': '5', 'K': '5', 'L': '5',
        'M': '6', 'N': '6', 'O': '6',
        'P': '7', 'Q': '7', 'R': '7', 'S': '7',
        'T': '8', 'U': '8', 'V': '8',
        'W': '9', 'X': '9', 'Y': '9', 'Z': '9'
    }
    return T9_MAPPING



##########################
##########################
# Convert the name to its corresponding T9 digits.
def name_to_digits(char_map, name):
    return ''.join(char_map[letter] for letter in name.upper() if letter in char_map)



##########################
##########################
# Search for the T9 digit representation of a name in the digits of pi.
def search_name_in_pi(char_map ,pi_file_path, name):
    
    # Convert the name to digits
    name_digits = name_to_digits(char_map, name)
    
    # Read the pi digits from the file
    with open(pi_file_path, 'r') as file:
        pi_digits = file.read().replace('\n', '').replace(' ', '')

    # Search for the name digits in the pi digits
    if name_digits in pi_digits:
        position = pi_digits.find(name_digits)
        return f"The term {name} (represented as {name_digits}) was found in pi position {position}."
    else:
        return f"The sequence '{name_digits}' (from the name '{name}') was not found in the digits of pi."



##########################
##########################
##########################
##########################
##########################
def main(search_term: str):
    pi_file_path = f'{Path.cwd()}/pi_search/pi.txt'
        
    char_map = map_characters()
    result = search_name_in_pi(char_map, pi_file_path, search_term)

    return json.dumps({"text":result.strip()})



if __name__ == '__main__':
    main()

    
