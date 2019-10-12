# Implimenting CRUD create Read Update & Delete.
dataBase = list()

def add(user_input):
    dataBase.append(user_input)

# index must be an Int
def read(dataBase_index):
    show_index = dataBase[dataBase_index]
    return show_index

#index is Int and Strings is a String
def update(index, strings):
    replace_index = dataBase[index] = strings
    return replace_index

def delete(index):
    database = dataBase.pop(index)
    return database

def take(user_input):
    print(user_input)

game_Running = True

while game_Running:
    take = (input("\nhit C to creat, S to Show,  R to read, U to Update & D to delete n Q to End Game!: "))
    # changing wat ever user enter to up case string
    take_upper = take.upper()
    #Testing: to make sure take_upper is conver some case to upper cases
    # print(take_upper)

    if take_upper == "S":
        list_index = 1
        for list_item in dataBase:
            print(f"\n{list_index}: {list_item}") 
            list_index += 1 

    elif take_upper == "C":
        add_on = input("\nEnter String: ")
        add(add_on)
    elif take_upper == "R":
        index = int(input("\nEnter Index to view: "))
        print("\n")
        print(f"{read(index)}")
    elif take_upper == "U":
        index = int(input("\nEnter Index to Update: "))
        string_replacement = input("\nEnter string to update: ")
        print(update(index, string_replacement))

    elif take_upper == "D":
      index = int(input("\nEnter index to delete: "))
      print(f"deleted - - - - >: {delete(index).upper()}")

    elif take_upper == "Q":
        game_Running = False

    else:
        print(" Pls Enter the right letter")
        print( "_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n")

else:
    print(" Thanks For Playing buy: 'python3 tutorial.py' to restart game")