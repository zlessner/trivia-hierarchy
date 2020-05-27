from flask import Flask

import questions
import quiz

app = Flask(__name__)


@app.route('/')
def hello():
	question = quiz.Questions(questions.capital_questions, questions.math_questions)
	rhold = question.get_question()
	return  rhold

if __name__ == '__main__':
    app.run()
