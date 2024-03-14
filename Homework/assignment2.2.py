sen = input("Write a sentence: ")

sen.replace("a", "A")
temp = ""
for x in sen:

   if x == "a" :
      temp += "A"
   else:
      temp += x


sen = temp

print(sen)


