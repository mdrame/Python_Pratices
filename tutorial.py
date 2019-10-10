

# Ask the user for a number and determine whether the number
#  is prime or not. (For those who have forgotten, a prime 
#  number is a number that has no divisors.). You can (and should!) 
#  use your answer to Exercise 4 to help you. Take this opportunity 
#  to practice using functions, described below.



def prompt(userInput):
    if userInput % 2 == 0:
        print(f"Yeah {userInput} is a prime number")
    else:
        print(f"{userInput} is  Not a prime number")


prompt(int(input("Pls enter a number so I can determine if it is a prime number: ")))