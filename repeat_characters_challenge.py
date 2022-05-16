# Create a Python function that accepts a string.
# The function should return a string, with each character in the original string doubled. 
# If you send the function "now" as a parameter, it should return "nnooww," and if you send "123a!", it should return "112233aa!!".

def repeat_characters(string):
    new_string = ''
    for letter in string:
        new_string += letter + letter
    print(new_string)



repeat_characters('Hello')
