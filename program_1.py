
# Program #1: Random Dice
# Write a "randDice" function (with no input) that randomly chooses two numbers between 1 and 6 (inclusive) and then adds them (this is to simulate the rolling of 2 dice).  
# The dice sum will be the output of this function.
import random 

def randDice():
    # Write your logic to generate 2 numbers between 1 and 6 here
   dice1=random.randint(1,6)
   dice2=random.randint(1,6)

   return dice1+dice2


def main():
   total=0

   for t in range(100):
      total+=randDice()

   avg=total/100
   print(f"For 100 rolls, the average was {avg}")


if __name__ == "__main__":
   main()

#########
# Then write a mainline that calls the "randDice" function 100 times in a for loop.  
# The mainline then prints the average of the 100 rolls, rounded to the nearest 0.01.
