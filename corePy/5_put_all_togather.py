def to_correct_sentenses(raw_strings): 
    the_capitalized= raw_strings.capitalize()
    interrogatives= ("who","what","why","where","how","are","is","were","have","has")
    if raw_strings.startswith(interrogatives):
        return "{}?".format(the_capitalized)
    else:
        return "{}.".format(the_capitalized)
result =[]
while True : 
    user_input= input("Say something: ")
    if user_input == "0":
        break
    else:
        result.append(to_correct_sentenses(user_input))

print(" ".join(result))