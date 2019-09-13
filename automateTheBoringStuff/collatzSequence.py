def collatz(number):
    if number % 2 == 0:
        number = number // 2
        print(str(number))
        return number
    else:
        number = 3 * number +1
        print(str(number))
        return number

while True:
    print('Type in an ingteger.')

    try:
        integer = int(input())
        while integer != 1:
            integer = collatz(integer)
    except:
        ValueError
        print('This is not an integer.')
        continue
    break
