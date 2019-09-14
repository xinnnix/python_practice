import random

messages = ['It is certain',
            'It is decidedly so',
            'Reply hazy try again',
            'Ask again later',
            'Concentrate and ask again',
            'My reply is no',
            'Outlook not so good',
            'Very doubtful']
for i in range(9):
    print(messages[random.randint(0, len(messages) - 1)])
