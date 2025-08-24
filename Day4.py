# Rock,Paper,Scissors
import random

player = input(">> Rock, Paper or Scissors ? Your move - ")
pc = random.randint(0,2)
computer=""

# 0 - rock
# 1 - paper
# 2 - scissors

if pc==0:
    computer = computer+"Rock"
elif pc==1:
    computer=computer+"Paper"
else:
    computer=computer+"Scissors"

if(player==computer):
    print(f"Computer chose - {computer}")
    print("It's a draw.")
else:

    if(player=="Rock"):
        if(computer=="Paper"):
            print(f"Computer chose - {computer}")
            print("You Lose.")
        else:
            print(f"Computer chose - {computer}")
            print("You Win.")

    if(player=="Paper"):
        if(computer=="Scissors"):
            print(f"Computer chose - {computer}")
            print("You Lose.")
        else:
            print(f"Computer chose - {computer}")
            print("You Win.")

    if(player=="Scissors"):
        if(computer=="Rock"):
            print(f"Computer chose - {computer}")
            print("You Lose.")
        else:
            print(f"Computer chose - {computer}")
            print("You Win.")