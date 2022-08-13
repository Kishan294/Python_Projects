from cgitb import text
import imp
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from logo import logo
question_bank = []
for question in question_data:
    question_text = question['text'] 
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

print(logo)
print("Welcome to Quiz Game")
while quiz.still_has_question():
    quiz.next_question()

print("You sucessfully complete the game")
print(f"Your final score is {quiz.score}/{quiz.question_number}")


