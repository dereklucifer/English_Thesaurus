import json
from difflib import get_close_matches

data = json.load(open('data.json'))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        best_match = get_close_matches(word, data.keys())[0]
        answer = input("Did you mean %s instead? Enter Y if yes, or N if no: " % best_match)
        if answer == "Y":
            return data[best_match]
        elif answer == "N":
            return "The word doesn't exist, Please double check it"
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist, Please double check it"


word = input("Enter word: ")

output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
