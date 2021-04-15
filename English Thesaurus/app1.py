# We have to import the json library in order to read our data
# get_close_matches returns a list of similar words
import json
from difflib import get_close_matches
data = json.load(open('data.json'))


def translate(w):
    """Function to find a word and it's definition"""
    w = w.lower()
    if w in data:
        return data[w]
    #  title and upper will check for words like Paris or NATO
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        # %s is replaced with the first item from the function list
        yn = input("Did you mean %s instead? Enter Y if yes or N if no: " % get_close_matches(w, data.keys())[0])
        yn = yn.lower()
        if yn == 'y':
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == 'n':
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your query."
    else:
        return "The word doesn't exist. Please double check it."


word = input('Enter word: ')

output = translate(word)

# This will check to see if our returned value is a list or string.
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
