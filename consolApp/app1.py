import pandas
import difflib
import json
from difflib import get_close_matches
data = json.load(open("sourcefiles/data.json"))
'''Define a function to get the matched words'''
def findMatch(word):
    word= word.lower()
    if word in data: 
        return data[word]
    elif word.title() in data: 
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0:
        yn = input("Did you mean %s instead? \nEnter Y if yes, or N if no:" %get_close_matches(word,data.keys())[0])
        if (yn=="Y") or (yn=="y"): 
            return data[get_close_matches(word,data.keys())[0]]
        elif (yn=="N") or (yn=="n"): 
            return "The word doesn't exist. Please  double check it."
        else:
            return "We don't understand your entry."
    else:
        return "The word doesn't exist. Please  double check it."

#Global part 
word = input("Enter word: ")
count=0
output = findMatch(word)
if type(output) == list:
    for i in output:
        count+=1
        print(count, i)
else:
    count+=1
    print(count, output)