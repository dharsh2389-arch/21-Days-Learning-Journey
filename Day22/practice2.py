'''Create a quiz program with 3 questions.
Program should:
Ask questions one by one
Check if the answer is correct
Display final score
Example
Copy code

Question: Capital of India?
Your answer: Delhi
Correct!

Question: 5 + 3 = ?
Your answer: 8
Correct!

Final Score: 2/2'''

score = 0
questions = {
    "Capital of India": "Delhi",
    "5 + 3": "8",
    "Python is a programming language (yes/no)": "yes"
}
for question, answer in questions.items():
    user = input(question + ": ")
    if user.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
print("Final Score:", score, "/", len(questions))

'''Output
Capital of India: delhi
Correct!
5 + 3: 8
Correct!
Python is a programming language (yes/no): yes
Correct!
Final Score: 3 / 3
'''
