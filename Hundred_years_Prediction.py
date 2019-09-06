def user_input(name,age,copies):

    current_calender_year = 2019
    current_age = int(age)
    result = current_calender_year - current_age+100
    convert_copies_to_int = int(copies)

    for i in range(convert_copies_to_int): #range(index) = from 0 - index
        print(f"Sup {name}, you will be 100 in {age} lol")

#calling function under here
user_input(input("Pls Enter your name: "), input("Pls enter your age: "), input("how amount of time to print result: ") )


                # --------- Instruction --------- #

#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
#Extras:
#Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
#Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
