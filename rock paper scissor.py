import random
your_choice = (input("what's your choice:"))
print (your_choice)
computer_choice = random.choice(["rock", "paper", "scissors"])
if your_choice == "paper" and computer_choice == "rock":
  print ("computer choose " + computer_choice)
  print ("you win")
elif your_choice == "rock" and computer_choice == "scissors":
  print ("computer choose " + computer_choice)
  print ("you win")
elif your_choice == "scissors" and computer_choice == "paper":
  print ("computer choose " + computer_choice)
  print ("you win")
elif your_choice == computer_choice :
  print ("computer choose " + computer_choice)
  print ("it's a tie")
else:
  print ("computer choose " + computer_choice)
  print ("you lose")