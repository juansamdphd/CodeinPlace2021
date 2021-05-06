"""
Khansole version that allows a user to select an operation to practice. The constant COUNT_CORRECT allows to number of successive correct guesses before exiting the program
The current setting is good for two digit operations, but this changed by adjusting the range with the MIN_NUMBER and MAX_NUMBER constants
"""

import random  #Imports random library

MIN_NUMBER = 10 # constant
MAX_NUMBER = 99 # constatnt
COUNT_CORRECT = 5 # constant

def main(): # defines main function of the script
    # Welcoming message
    print("Hi! Welcome to a Khansole version \nmade by juansanarmdph as part of CodeinPlace2021")
    
    # Select math operation to practice
    operation = input("What math operation would you like to practice today,\naddition, substraction, multiplication, or division?: ")
    
    # Pracitce addition
    if operation == "addition":
        guess = 0
        # random.seed(1)
        while guess < COUNT_CORRECT:
            num1 = random.randint(MIN_NUMBER, MAX_NUMBER) # generates a random int between 10 and 99
            num2 = random.randint(MIN_NUMBER, MAX_NUMBER) # generates a random int between 10 and 99
            num3 = num1 + num2 # adds random int generated above
            print("What is " + str(num1) + " + " + str(num2) + "?")
            user_num = int(input("Your answer: "))
            if user_num == num3: # evaluates if the user answer is correct
                guess = guess + 1 # if correct, then guess + 1 (i.e, 1 answer is correct) 
                print("Correct! You've gotten " + str(guess) + " correct in a row.")
            else:
                print("Incorrect. The answer the expected answer is " + str(num3))
                guess = 0 # resets guess "counter"
            if guess == COUNT_CORRECT: # Evaluates if the user has guessed the number set in the COUNT_CORRECT constant
                print("Congratulations! You mastered addition.")
    
    # Practice substraction
    elif operation == "substraction":
        guess = 0
        # random.seed(1)
        while guess < COUNT_CORRECT:
            num1 = random.randint(MIN_NUMBER, MAX_NUMBER) # generates a random int between 10 and 99
            num2 = random.randint(MIN_NUMBER, MAX_NUMBER) # generates a random int between 10 and 99
            num3 = num1 - num2 # adds random int generated above
            print("What is " + str(num1) + " - " + str(num2) + "?")
            user_num = int(input("Your answer: "))
            if user_num == num3: # evaluates if the user answer is correct
                guess = guess + 1 # if correct, then guess + 1 (i.e, 1 answer is correct) 
                print("Correct! You've gotten " + str(guess) + " correct in a row.")
            else:
                print("Incorrect. The answer the expected answer is " + str(num3))
                guess = 0 # resets guess "counter"
            if guess == COUNT_CORRECT: # Evaluates if the user has guessed the number set in the COUNT_CORRECT constant
                print("Congratulations! You mastered addition.")
    
    # Practice multiplication
    elif operation == "multiplication":
        guess = 0
        # random.seed(1)
        while guess < COUNT_CORRECT:
            num1 = random.randint(MIN_NUMBER, MAX_NUMBER) # generates a random int between 10 and 99
            num2 = random.randint(MIN_NUMBER, MAX_NUMBER) # generates a random int between 10 and 99
            num3 = num1 * num2 # adds random int generated above
            print("What is " + str(num1) + " * " + str(num2) + "?")
            user_num = int(input("Your answer: "))
            if user_num == num3: # evaluates if the user answer is correct
                guess = guess + 1 # if correct, then guess + 1 (i.e, 1 answer is correct) 
                print("Correct! You've gotten " + str(guess) + " correct in a row.")
            else:
                print("Incorrect. The answer the expected answer is " + str(num3))
                guess = 0 # resets guess "counter"
            if guess == COUNT_CORRECT: # Evaluates if the user has guessed the number set in the COUNT_CORRECT constant
                print("Congratulations! You mastered addition.")
    
    # Practice division
    elif operation == "division":
        guess = 0
        # random.seed(1)
        while guess < COUNT_CORRECT:
            num1 = random.randint(MIN_NUMBER, MAX_NUMBER) # generates a random int between 10 and 99
            num2 = random.randint(MIN_NUMBER, MAX_NUMBER) # generates a random int between 10 and 99
            num3 = num1 / num2 # adds random int generated above
            print("What is " + str(num1) + " / " + str(num2) + "?")
            user_num = int(input("Your answer: "))
            if user_num == num3: # evaluates if the user answer is correct
                guess = guess + 1 # if correct, then guess + 1 (i.e, 1 answer is correct) 
                print("Correct! You've gotten " + str(guess) + " correct in a row.")
            else:
                print("Incorrect. The answer the expected answer is " + str(num3))
                guess = 0 # resets guess "counter"
            if guess == COUNT_CORRECT: # Evaluates if the user has guessed the number set in the COUNT_CORRECT constant
                print("Congratulations! You mastered addition.")

if __name__ == "__main__":
    main()
