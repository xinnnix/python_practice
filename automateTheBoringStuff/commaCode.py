#This is the comma code

def comma(listToPrint):
    i = 0
    thePrint = ''
    while i < len(listToPrint)-1:
        thePrint = thePrint + str(listToPrint[i]) + ', '
        i +=1
    print(str(thePrint) + 'and ' + str(listToPrint[-1]))
                                  

spam = ['cat','dog','flower','rain']
print('This is spam:')
print(spam)
print('This is the comma version of spam:')
comma(spam)
