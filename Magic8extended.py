import random
name = "rhonda"
question = "am I smelly?"
answer = ""

if (name == "") and (question == ""):
  print("Im going to answer the secret question you are thinking about.")
elif question == "":
  print(name + ",","Im going to answer the secret question you are thinking about.")
elif name == "":  
  print("Question:",question)
else:
  print(name,"asks:",question)

random_number = random.randint(1, 9)

if random_number == 1:
  answer = "Yes-definitely"
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Better not tell you now."
elif random_number == 6:
  answer = "My sources say no."
elif random_number == 7:
  answer = "Outlook not so good."
elif random_number == 8:
  answer = "Very doubtful."
elif random_number == 9:
  answer = "Ask again later."
else:
  answer = "Error"

print("Random 8-Ball's answer:", answer)
