# Create a function in Python that accepts two parameters. 
# The first will be a list of numbers.
# The second parameter will be a string that can be one of the following values: asc, desc, and none.
#
# If the second parameter is "asc," then the function should return a list with the numbers in ascending order. If it's "desc," then the list should be in descending order, and if it's "none," it should return the original list unaltered.
list = [3, 4, 1, 6, 24, 33, 49]

def sort_list(list, sorter):
    if sorter == 'none':
        print(list)
    elif sorter == 'asc':
        print(sorted(list))
    elif sorter == 'dsc':
        print(sorted(list, reverse=True))
    else:
        print('no sorter found')

sort_list(list, None)
