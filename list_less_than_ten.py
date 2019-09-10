
number_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] #list(array)
less_than_five_list = list() #empty list to append every number less than five init

def check():
    for item in number_list: #looping throught every index in the array and assigning it to item.
        if item < 5: # if any number lesser than 5 should be added to less_than_five_list with the .append() method
            less_than_five_list.append(item)

check() #calling function here
print("These are the numbers lesser than 5:")
print(less_than_five_list) #printing less_than_five_list



            # ------- instruction ----------

#Take a list, say for example this one:

  #a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of
#the list that are less than 5.
#Instead of printing the elements one by one, make a new list that has all
#the elements less than 5 from this list in it and print out this new list.
