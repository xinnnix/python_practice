myPets = ['Zophie','Pooka','Fat-tail']
while True:
    print('Enter a pet name (or enter nothing to quit):')
    name = input()
    if name == '':
        break
    elif name not in myPets:
        print('I do not have a pet named ' + name)
    else:
        print(name + ' is my pet.')
