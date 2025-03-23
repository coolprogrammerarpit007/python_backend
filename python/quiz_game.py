# Python Quiz Game

questions = ("How many elements are in the periodic table ?",
             "Which animal lays the largest egg: ?",
             "What is the most abundant gas in Earth's atmosphere: ?",
             "How many bones are in the human body ?",
             "Which is the largest continent in the world ?")
options = (
    ("A. 116","B. 117","C. 118","D. 120"),
("A. Lion","B. Elephant","C. Whale","D. Ostrich"),
("A. Nitrogen","B. Oxygen","C. Carbon die Oxide","D. Hydrogem"),
("A. 214","B. 450","C. 360","D. 206"),
("A. Asia","B. Europe","C. Australia","D. North America"),
)
answers = ("C","D","A","D","A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-----------------------")
    print(question)
    print("------- Your Options Are: ")
    for option in options[question_num]:
        print(option)


    guess = input("Enter (A,B,C,D) ").upper()
    if guess == answers[question_num]:
        score += 1
        print("Correct")
    else:
        print("InCorrect")
    question_num += 1

print(f"You Final Score in the quiz game is: {score}")