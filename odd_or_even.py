




user_input = int(input("Enter a number of your choice: ")) # explicitly request input as integer

#trying to make this programe oop as possible
def user_input_comparisin(user_input):
    if (user_input % 2 == 0): # iof user_input divide by 20 and reminder is 0
        print(f" {user_input} is a even number")
    else:
        print(f" {user_input} is an odd number ")


user_input_comparisin(user_input)

            # -------- Instruction -------------

#Ask the user for a number. Depending on whether the number is even or odd,
#print out an appropriate message to the user. Hint: how does an even / odd
# number react differently when divided by 2?
