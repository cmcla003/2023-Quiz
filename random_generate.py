import random

# Store Questions and Answer in list
question_prompt = [
    "What are to colour of apples?\na. Red\nb. Purple\nc. Orange",
    "What are the colour of bananas?\na. Teal\nb. Magenta\nc. Yellow",
    "What are the colour of grapes?\na. Orange\nb. Purple\nc. Yellow"
]
correct_ans = ["a", "c", "b"]

# ***** Main routine ***
score = 0
# sets up list to store asked questions
asked = []

keep_going = ""
while keep_going == "":

    # Select random question
    select = random.randint(0,2)
    # more item to asked list and assess if asked before
    if question_prompt[select] in asked:
        continue
    # ask the question is  in asked list
    else:
        print(question_prompt[select])
        guess = input("Answer: ").lower().strip()
        asked.append(question_prompt[select])

    # Checks answer and adds to score
    if guess == correct_ans[select]:
        score += 1
        print("Correct you got {} points".format(score))
    else:
        print("Sorry that is incorrect")









