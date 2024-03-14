
#Question 1
nl = []
yp = range(1500,2701)
for num in yp:
    if (num % 7 == 0) and (num % 5 == 0):
        nl.append(num)
print(nl)
    

#Question 2???
import random

rand_input = random.randrange(1, 10)
guess_num = int(input("Guess a number from 1 to 9 until your correct: "))
print("Rand number: ", rand_input)
while rand_input != guess_num:
    guess_num = int(input("Guess a number from 1 to 9 until your correct: "))
print("Correct Guess!!")

#Question 3
samp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 35, 46, 80]
odd = []
even = []
for x in samp :
    if x % 2 == 0 :
        even.append(x)
    elif x % 2 != 0 :
        odd.append(x)
    
print("Number of even no: ", len(even))
print("Number of odd no: ", len(odd))


#Question 4
def sum(nums):
    total = 0
    for x in nums:
        total += x
    return total

print(sum([1,2,3,4,5,7,2,89,204]))


#Question 5
def factorial(n):
    i = n
    result = 1
    while i > 0 :
        result *= i
        i -= 1

    return result
n= int(input("Please type in a value to get its factorial: "))
print(factorial(n))
     
#Question 6 
# (*) is used for unknown
def rec(word) :
    upper_case = 0 
    lower_case = 0
    for x in word:
        if x== "":
          pass
        print(len(word), x == x.upper())
        if x == x.upper():
            upper_case += 1
        
        elif x == x.lower():
            lower_case += 1
        
    return upper_case, lower_case

word= input("Please type in a sentence with a mix of upper and lower case letters")


print(rec(word))
