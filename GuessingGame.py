import random

lowest = 1
highest = 25

# Select random number
answer = random.randint(lowest, highest)

def guess():
    guess=input(f"Guess a number from {lowest} to {highest}: ")
    
    try_number = 0
    
    while(int(guess)!=answer):
        try_number += 1
        if(int(guess)<answer):
            print("Answer is higher")
        else:
            print("Answer is lower")
        guess=input(f"Guess a number from {lowest} to {highest}: ")
        
    print(f"You are a winner! It took you {try_number} try(s)")
    
            
if __name__ == "__main__":
    guess()