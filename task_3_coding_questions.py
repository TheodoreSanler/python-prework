# Question 1:
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function.

#def hello_name(user_name):

#Answer:
def hello_name(username):
    print(f'"hello_{username}!"')

hello_name("USERNAME")


#Question 2:
# Write a python function, first_odds that prints the odd numbers from 1-100
# and returns nothing.

#Answer:
def first_odds():
    print(list(range(1,100,2)))

first_odds()


# Question 3:
# Please write a Python function, max_num_in_list to return the max number of a 
# given list. 

#Answer:
def max_num_in_list(a_list):
    return max(a_list)

test_list = [1, 54, 23, 41, 89, 33, 2]
print(max_num_in_list(test_list))


# Question 4:
# Write a function to return if the given year is a leap year. A leap year is 
# divisible by 4, but not divisible by 100, unless it is also divisible by 400.
#The return should be boolean Type (true/false)

# Answer:
def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 100 == 0 and a_year % 400 == 0:
       return True
    elif a_year % 4 == 0 and a_year % 100 == 0 and a_year % 400 != 0:
        return False
    elif a_year % 4 == 0 and a_year % 100 != 0:
        return True
    else:
        return False

print(is_leap_year(1300))


# Question 5:
# Write a function to check to see if all numbers in list are consecutive numbers.
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not 
# consecutive numbers. The return should be boolean Type.

# Answer:
def is_consecutive(a_list):
         new_list = list(range(min(a_list),max(a_list)+1,1))
         if a_list == new_list:
            return True
         else:
            return False
               
    
test_list_true = [2,3,4,5,6,7]
print(is_consecutive(test_list_true))

test_list_false =[1,2,4,5]
print(is_consecutive(test_list_false))





