# Write a program that takes a list of numbers
#  (for example, a = [5, 10, 15, 20, 25]) and 
#  makes a new list of only the first and last 
#  elements of the given list. For practice,
#   write this code inside a function.




a = [5, 10, 15, 20, 25]

def list_end():

    '''creating two different variable consisting 
     of the first and last index of a array '''

    # < ------ D R Y -------- >
    # first_element_in_a = a[0]
    # last_element_in_a = a[-1]
    # print(last_element_in_a) testing 

    new_list = list()
    new_list.append(a[0])
    new_list.append(a[-1])

    print(f"The first and last element of the new list is {new_list}")


list_end()