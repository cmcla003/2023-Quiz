import random

# set up list to store already asked questions 
asked = []

# randomly slect number 
num_1 = random.randint(1,12)
num_2 = random.randint(1,12)

def question_type():
  error = "Please enter + - / or x"
  # ask user tpye of question they want 
  quest_type = input("Do you want to + - / or x").lower().strip()
  
  if quest_type == "+":
    answer = num_1 + num_2
    question = "{} + {} = ".format(num_1,num_2)
  elif quest_type == "-":
    answer = num_1 - num_2
    question = "{} - {} = ".format(num_1,num_2)
  elif quest_type == "x":
    answer = num_1 * num_2
    question = "{} x {} = ".format(num_1,num_2)
  elif quest_type == "/":
    answer = num_1 / num_2
    question = "{} / {} = ".format(num_1,num_2)

  return answer, question
  else:
    print(error)
  
  



