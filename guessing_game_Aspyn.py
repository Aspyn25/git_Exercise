from random import randint

# make a random number
min = 1
max = 1000
ran_num = randint(min,max)

i = 1 # Guess count

while True :

    # ask the number
    try:
        # if not guess_num.isnumeric()
        guess_num = int(input(f"Enter your guess from {min} to {max}: "))
    except ValueError:
        print("you should put the number.")
        continue

    #compared with random number
    if guess_num == ran_num:
        print("You got it! The hidden number is ", ran_num)
        print(f"It took you {i} guess(es).")
        break

    elif guess_num < ran_num and min < guess_num:
        min = guess_num + 1
        print("Wrong! Guess count:", i)
        
    
    elif guess_num > ran_num and max > guess_num:
        max = guess_num - 1
        print("Wrong! Guess count:", i)
    
    else  : 
        print("you put the number which is out of range, try agian.")

    i += 1
        
        
            
