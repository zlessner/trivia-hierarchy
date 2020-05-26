import random, copy
from questions import capital_questions, math_questions

class Questions:
    def __init__(self, capital_questions, math_questions):
        self.capital_questions = capital_questions
        self.math_questions = math_questions



        cap_keys = list(self.capital_questions.keys())
        math_keys = list(self.math_questions.keys())

        random.shuffle(cap_keys)
        random.shuffle(math_keys)


        shuffled_capital_questions = dict()
        shuffled_math_questions = dict()

        for key in cap_keys:
            shuffled_capital_questions.update({key:self.capital_questions[key]})
        for key in math_keys:
            shuffled_math_questions.update({key:self.math_questions[key]})

        
        ranNumGen = random.random()

        if ranNumGen < .5:
            print('''
            What is the capital of {country}? '''.format(country=next(iter(shuffled_capital_questions))))

            user_input = input() 

            if user_input == shuffled_capital_questions.get(next(iter(shuffled_capital_questions))):
                print ("You are correct!")
            else:
                print ("Sorry, that answer is incorrect. The capital of {question} is {answer}.".
                format(question=next(iter(shuffled_capital_questions)), 
                answer=shuffled_capital_questions.get(next(iter(shuffled_capital_questions)))))

        else:
            print(next(iter(shuffled_math_questions)))

            user2_input = input()

            if user2_input == shuffled_math_questions.get(next(iter(shuffled_math_questions))):
                print ("You are correct!")
            else:
                print ("Sorry, that answer is incorrect. {question}={answer}.".
                format(question=next(iter(shuffled_math_questions)), 
                answer=shuffled_math_questions.get(next(iter(shuffled_math_questions)))))




run = Questions(capital_questions, math_questions)