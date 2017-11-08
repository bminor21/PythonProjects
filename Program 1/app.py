import json                           # Module to easily load JSON data
from difflib import SequenceMatcher   # Function to compare text
from difflib import get_close_matches # Function to find closest match


data = json.load( open("data.json") ) # Gets the data from the JSON object as a dictionary

def getIndex( word, list ):
    print("Could not find " + word + ". Did you mean? " )
    i = 0
    for s in list:
        print( str(i) + " - " + s )
        i += 1
    while True:
        try:
            choice = int( input("Enter a value or -1 to go back: ") )
            if choice < -1 or choice > len(list)-1:
                print("Invalid option")
            else:
                break
        except ValueError:
            print("That's not a valid number.")
    return choice


def getDefinition(_input):
    try:
        if( _input[0].isupper() ):
            _input = _input.capitalize()
            results = get_close_matches( _input, data.keys() )
        else:
            _input = _input.lower()
            results = get_close_matches( _input, data.keys() )
        if len( results ) == 0:
            return "No definition found"
        elif( results[0] != _input ):
            idx = getIndex(_input, results )
            if( idx == -1 ):
                return ""
            else:
                return data[results[idx]]
        else:
            return data[ results[0] ]
    except KeyError:
        return "No definition found"

while True:
        _input = input("Enter a word or -1 to quit: ")
        if( _input == "-1" ):
            print("Exiting the program")
            break;

        w = getDefinition(_input)
        if len(w) > 0:
            print("\nWord : " + _input )
            print("Definition: ")
            for s in w:
                print("     -" + s )
            print("\n")
