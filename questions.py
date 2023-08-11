# Store Questions in list/2d Array
question_prompt = [
    ["What are to colour of apples?\na. Red\nb. Purple\nc. Orange", "a"],
    ["What are the colour of bananas?\na. Teal\nb. Magenta\nc. Yellow","c"],
    ["What are the colour of grapes?\na. Orange\nb. Purple\nc. Yellow", "b"]
]

# ***** Main routine ***
# calculate score 
score = 0

# iterate throguh list to ask questions 
for question in question_prompt:
    print(question[0])
    answer = input("Answer: ")
  # if user correct add 1 to score 
    if answer == question[1]:
        score += 1
        print("Correct you got {} points".format(score))
    else:
        print("Sorry that is incorrect")

    print("Score: {}".format(score))
