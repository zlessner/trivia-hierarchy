# create class of questions
# create function

import random, copy

capital_questions = {
    'Nigeria': 'Abuja',
    'Iran': 'Tehran',
    'Vietnam': 'Hanoi'}

keys = list(capital_questions.keys())

random.shuffle(keys)


shuffled_capital_questions = dict()
for key in keys:
    shuffled_capital_questions.update({key:capital_questions[key]})


print('''
What is the capital of {country}? '''.format(country=next(iter(shuffled_capital_questions))))

answer = input() 

if answer == shuffled_capital_questions.get(next(iter(shuffled_capital_questions))):
    print ("You are correct!")
else:
    print ("Sorry, that answer is incorrect")