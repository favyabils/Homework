

# Question 1
value = input(" input a set of comma seperated number values e.g 1,2,3 do not include space between values")
value2 = list((value))
value3 = tuple((value))
print("List:", value2)
print("Tuple:", value3)


data = input("Input a set comma seperated values: ")
list = data.split(",")
tuple =  tuple(list)
print("List:",list)
print("Tuple:", tuple)


#Question 2 :)
character =  input("Type in any word")
list = list(character)
list.reverse()
print(list)

cht = input("Type in any word: ")
chat = cht [::-1]
print(chat)

#Question 3
word = input("Type in A word: ")
lit = list((word))
print(lit)


#Question 4
lit4 = [23, 4, 5, 3, 5, 3, 3, 36, 2, 9, 0]
print(min(lit4))

#Question 5 in set each value must be unique
lit5 = [2, 34, 56, 8, 9, 2, 78, 2, 53, 123, 2]

my_set = set(lit5)
print(list(my_set))

#Question 6
lit6 = []
if not lit6 :
    print("List is Empty")
else :
    print('Not Empty')

#Question 7
import random
lit7 = [2, 34, 5, 60, 78, 999, 345, 12, 0, 3, 5]
print(random.choice(lit7))


#Question 8
a = [3, 4, 6, 78, 9, 0, 234, 56, 79 ]
b = [4, 6, 8, 9, 10 ,3, 45, 88, 79, 564]
for  x in a :
    if x in b:
      print(x)


#Question 9
lit9 = (45, 6, 7, 89)
for i in lit9:
  print(i, end="" )

#Question 10
lit10 = [2, 4, 6, 89, 56, 0, 90, 7, 3, 31, 23, 55]
light = []
for x in lit10:
    if x % 2 != 0:
        light.append(x)
    elif x % 2 == 0 :
        continue
print(light)

lit10 = [2, 4, 6, 89, 56, 0, 90, 7, 3, 31, 23, 55]

for x in lit10:
    if x % 2 != 0:
        print(x) 
        #???


#Question 11
rhyme = """Twinkle, twinkle, little star,\n\t How I wonder what you are!\n\t\tUp above the world so high,
\t\t Like a diamond in the sky.\n Twinkle, twinkle, little star,\n\t How I wonder what you are"""
print(rhyme)

#Question 13
lit11 = [5, 6, 7, 8, 98, 2, 23, 45]
lit11.reverse
tup11 = tuple(lit11)
print(lit11, tup11 )
