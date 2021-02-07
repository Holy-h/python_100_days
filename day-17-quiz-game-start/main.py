from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

"""
TODO: 2. Write a for loop to iterate over the question_data.
Create a Question object from each entry in question_data.
Append each Question object to the question_bank.    
"""
question_bank = []
for question in question_data:
    q_text = question.get("question")
    q_answer = question.get("correct_answer")
    new_q = Question(q_text, q_answer)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print(f"You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
