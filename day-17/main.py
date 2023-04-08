#!/bin/python3

# QUIZ CLI APP
from question_model import Question
from data import computers_data
from quiz_brain import QuizBrain

# Store all the questions and their answers in a tuple
question_bank = [Question(question["text"], question["answer"]) for question in computers_data]

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")
