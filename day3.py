# WAF  to print factorial of 'n'
# n = int(input("Enter a number n:"))
def calc_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

n = int(input("Enter a number:"))
print(calc_factorial(n))

# fact = 1
# for i in range(1, n + 1):
#     fact = fact * i
# print(fact)



# lambda function uses a keyword lambda and uses parameter and can have a single expression
# lambda a, b, c : a + b + c
# sum = lambda a,b: a + b
# print(sum(4,5))

## There are two types of function built in and user defined
##print()
##
##
# def sum(a, b=1):
#     return a + b

# print(sum(5))

# # Average value
# def average(a, b, c):
#     avg = (a + b + c) / 3
#     return avg

# print(average(5, 10, 15))



# function reusable components of code
# def sum(a, b): # parameters
#     s = a + b
#     return s

# #function call
# ans = sum(3, 4) # arguments
# print(ans)

# # PRINT SUM OF FIRST N NATURAL NUMBERS
# num = int(input("Enter the numbers positive only"))
# sum = 0

# for i in range(1, num + 1):
#     sum += i

# print(sum)

# for i in range(1, 10, 2):
#     print(i)


# word = "artificial intelligence"

# count = 0

# for ch in word:
#     if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
#         count += 1

# print("ans =",count)

# count = 0
# for ch in word:
#     if (ch == 'i'):
#         count += 1
# print("count of i =", count)

# string  = "hello"
# # in => membership operator
# # in operator check presence value
# for var in string:
#     print(var)


# # odd number
# i = 0

# while (i <= 9): 
#     i += 1
#     if (i % 2 == 0):
      
#         continue
#     print(i)
    
 

# i = 1

# while (i <= 10):
#     if (i % 6 == 0):
#         break
#     print(i)
#     i += 1


# # multiplication table of any num
# n = int(input("Enter num:"))

# i = 1
# while (i <= 10):
#     print(n * i)
#     i += 1



# i = 5 # iterator
# while (i >= 1):
#     print(i)
#     i -= 1



## infinite loop
# while True:
#     print("Hello , World")


## Loops



## Match Case
# color = input("enter color: ")
# match color:
#     case "Green":
#         print("Go")
#     case "Yellow":
#         print("Look")
#     case "Red":
#         print("Stop")
#     case _: # d3fault case
#         print("Wrong Color!")



# age = int(input("Enter the age "))

# if age < 13:
#     print("child")
# elif age > 13 and age < 18:
#     print("Teenager")

# elif age >= 18:
#     print("adult")

# else:
#     print("Enter valid number")