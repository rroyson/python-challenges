def repeat_characters(string):
    new_string = ''
    for letter in string:
        new_string += letter + letter
    print(new_string)



repeat_characters('Hello')
