def createList(n):
    lst = []
    for i in range(n+1):
        lst.append(i)
    return(lst)

numbers = createList(100)

for num in numbers:
    if num % 5 == 0 and num % 3 == 0:
        print('FizzBuzz', num)
    elif num % 3 == 0:
        print('Fizz', num)
    elif num % 5 == 0:
        print('Buzz', num)
    else:
        print('Nadda')
