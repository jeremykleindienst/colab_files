# You can find many exercises by searching for "python exercise list" or "python exercise pandas" or "python exercise scikit-learn"
# Here are a couple of pages that might help:

# - https://www.w3resource.com/python-exercises/list/
# - https://www.w3resource.com/python-exercises/python-functions-exercises.php
# - https://www.w3resource.com/python-exercises/dictionary/
# - https://www.w3resource.com/python-exercises/tuple/
# - https://www.w3resource.com/python-exercises/lambda/index.php
# - https://pynative.com/python-dictionaries/


list = [6,3,7,9,23,4,54,-8]



# 1. Write a Python function to sum all the items in a list.
# Source: https://www.w3resource.com/python-exercises/list/python-data-type-list-exercise-1.php
def sum_list(items):
    tot = 0
    for x in items:
        tot += x
    return tot
print(sum_list(list))



# 2. Write a Python function to multiplies all the items in a list.
# Source: https://www.w3resource.com/python-exercises/list/python-data-type-list-exercise-2.php
def multiply_list(items):
    tot = 1
    for x in items:
        tot *= x
    return tot
print(multiply_list(list))



# 3. Write a Python function to get the largest number from a list. Go to the editor
# https://www.w3resource.com/python-exercises/list/python-data-type-list-exercise-3.php
def max_num_in_list( list ):
    max = list[ 0 ]
    for a in list:
        if a > max:
            max = a
    return max
print(max_num_in_list(list))



# 4. Write a Python function to get the smallest number from a list. Go to the editor
# https://www.w3resource.com/python-exercises/list/python-data-type-list-exercise-4.php
def smallest_num_in_list( list ):
    min = list[ 0 ]
    for a in list:
        if a < min:
            min = a
    return min
print(smallest_num_in_list(list))



# 5. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
# https://www.w3resource.com/python-exercises/list/python-data-type-list-exercise-6.php
list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

def last(n): return n[-1]

def sort_list_last(tuples):
  return sorted(tuples, key=last)

print(sort_list_last(list))



# 6. Write a Python function that takes two lists and returns True if they have at least one common member.
# https://www.w3resource.com/python-exercises/list/python-data-type-list-exercise-11.php
list1 = [1, 2, 3, 4, 5]
list2 = [5, 6, 7, 8, 9]
list3 = [6, 7, 8, 9]
def common_data(list1, list2):
    for x in list1:
        for y in list2:
            if x == y:
                return True
    return False
print(common_data(list1, list2))
print(common_data(list1, list3))
