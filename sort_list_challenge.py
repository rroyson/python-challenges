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
