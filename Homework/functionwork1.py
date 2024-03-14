"""
#Question1
def csv(num):
    num = str(num)
    num.split(" ")
    print(list(num))
    print(tuple(num))
csv(input("Type in a sequence of numbers: "))

#Question2
def reverse(word):
    word = word [::-1]
    print(word)
reverse(input("Type in any word: "))

#Question3
def lit(strings) :
  strings = list(strings)
  print(strings)
lit(input("Type in A word: "))


#Question4
def lit4(*num):
    num = list(num)
    print(min(num))
lit4(3,4,5,67,89,234,2,3,6,) #why is it that if you put in a list the code doesnt work ?


#Question 5
def lit5(*numb):
    numb = set(numb)
    print(list(numb))
lit5(2, 34, 56, 8, 9, 2, 78, 2, 53, 123, 2,9,56,78,53,45,123)


#Question 6
def lit6(Num):
    Num= [4,5]
    if not Num :
        print("List is Empty")
    else :
        print('Not Empty')
lit6("Num")


#Question7
import random
def lit7(*Numb):
    print(random.choice(Numb))
lit7 (2, 34, 5, 60, 78, 999, 345, 12, 0, 3, 5)


#Question8
def AB(a,b):
    a = [3, 4, 6, 78, 9, 0, 234, 56, 79 ]
    b = [4, 6, 8, 9, 10 ,3, 45, 88, 79, 564]
    for  x in a :
        if x in b:
            print(x)
AB("a","b")# Why must i type a and b in string form


#Question9
def lit9(*num):
    for i in num:
        print(i, end="" )
lit9(45, 6, 7, 89)

#Question10
def list10(lit10,light):
    lit10 = [2, 4, 6, 89, 56, 0, 90, 7, 3, 31, 23, 55]
    light = []
    for x in lit10:
        if x % 2 != 0:
            light.append(x)
        elif x % 2 == 0 :
            continue
    print(light)
list10("lit10","light")
"""

#Question11
def Ryhme():
    rhyme = """Twinkle, twinkle, little star,\n\t How I wonder what you are!\n\t\tUp above the world so high,
    \t\t Like a diamond in the sky.\n Twinkle, twinkle, little star,\n\t How I wonder what you are"""
    print(rhyme)
Ryhme()

#Question13
def list11(lit11,tup11):
    lit11 = [5, 6, 7, 8, 98, 2, 23, 45]
    lit11.reverse
    tup11 = tuple(lit11)
    print(lit11 )
    print(tup11)
list11("lit11","\n tup11") #How do I put it on seperate lines