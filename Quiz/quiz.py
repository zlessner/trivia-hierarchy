#consolidate code
#make flask front end

import random, copy
from questions import capital_questions, math_questions

class Questions:
    def __init__(self, capital_questions, math_questions):
        self.capital_questions = capital_questions
        self.math_questions = math_questions

        ranNumGen = random.random()
        question_value = dict()

        if ranNumGen < .5:
            category = self.capital_questions
            answer_value = "Sorry, that answer is incorrect. The capital of {question} is {answer}."

        else:
            category = self.math_questions
            answer_value = "Sorry, that answer is incorrect. {question}={answer}."


        keys = list(category.keys()) 

        random.shuffle(keys)

        for key in keys:
            question_value.update({key:category[key]})


        #Capital Questions
        if ranNumGen < .5:
            print('''
            What is the capital of {country}? '''.format(country=next(iter(question_value))))

        #Math Questions
        else:
            print(next(iter(question_value)))

        user_input = input() 

        if user_input.lower() == question_value.get(next(iter(question_value))).lower():
            print ("You are correct!")

        #Answer is based on what type of question it is    
        else:
            print (answer_value.
            format(question=next(iter(question_value)), 
            answer=question_value.get(next(iter(question_value)))))



run = Questions(capital_questions, math_questions)