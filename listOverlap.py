
# ------ Instruction -----------

# and write a program that returns a list that contains
# only the elements that are common between the lists
# (without duplicates). Make sure your program works on
#  two lists of different sizes.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 21]

c = []

for i in a:
    if i in b :

        c.append(i)

print(c)










# # This is the sum function we want to test for correctness
# def my_sum_function(num_list):
#     """Return the total of all numbers in the given list added together."""
#     my_sum = 0
#     for num in num_list:
#         my_sum += num
#
#         # Example error in function implementation (using wrong operator)
#         # my_sum *= num
#
#     return my_sum
#
#
# # This is the function we have written to automatically test the sum function
# def test_sum():
#     # Test functions usually contain contain several assertion statements, and
#     # each has a condition that must be true. If not, then an error is thrown.
#     # This is the general format commonly used for most assertion statements
#     # assert function(input_data) == expected_result
#
#     # An optional helpful error message can be included after the condition
#     # assert function(input_data) == expected_result, "Helpful error message"
#
#     # These are some assertions that test the correctness of the sum function
#     assert my_sum_function([3, 5]) == 8
#     assert my_sum_function([99, 1]) == 100
#     assert my_sum_function([-5, 0, -2]) == -7
#     assert my_sum_function([11, 22, 33, 44, 55, -66]) == 99
#     assert my_sum_function([3.7, 8.5]) == 12.2
#     assert my_sum_function([4]) == 4, "Sum is incorrect for single number"
#     assert my_sum_function([]) == 0, "Sum is incorrect for empty list"
#
#     # Notice that test code itself could have errors in assertion statements
#     assert my_sum_function([5,5]) == 10
#
#     assert 50 + 50 == 100
#
#
# if __name__ == "__main__":
#     # Run the test function
#     test_sum()
