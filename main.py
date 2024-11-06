from random import randint
"""
Ex1. 
Write a Python program to sum all the items in a user defined list (use loops not built in sum functions)

u_list = []
#getting length of list
l_length = int(input("Please enter in the length of list: "))
#adding items to list
for i in range(0,l_length):
  num = int(input("Please enter a number: "))
  u_list.append(num)
sum = 0
#Summing all items in list
for num in u_list:
  sum+=num
print(sum)
"""
"""
Ex2. Write a Python program to multiplies all the items in a user defined list (use loops not built in product functions)

u_list = []
#getting length of list
l_length = int(input("Please enter in the length of list: "))
#adding items to list
for i in range(0,l_length):
  num = int(input("Please enter a number: "))
  u_list.append(num)
prod = 1
#Summing all items in list
for num in u_list:
  prod*=num
print(prod)
"""
"""
Ex3. Write a Python program to get the largest number from a user defined list (use loops not built in min/max functions)

u_list = []
#getting length of list
l_length = int(input("Please enter in the length of list: "))
#adding items to list
for i in range(0,l_length):
  num = randint(0,50)
  u_list.append(num)
l_num = u_list[0]
for num in u_list:
  if num>l_num:
    l_num = num
print(l_num," ",u_list)
"""
"""
Ex4. Write a Python program to get the smallest number from a user defined list (use loops not built in min/max functions)

u_list = []
#getting length of list
l_length = int(input("Please enter in the length of list: "))
#adding items to list
for i in range(0,l_length):
  num = randint(0,50)
  u_list.append(num)
s_num = u_list[0]
for num in u_list:
  if num<s_num:
    s_num = num
print(s_num," ",u_list)
"""
"""
Ex5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings

u_list = []
#getting length of list
l_length = int(input("Please enter in the length of list: "))
for i in range(0,l_length):
  word = input("Please enter a word: ")
  u_list.append(word)
count = 0
for word in u_list:
  if len(word)>2 and word[0]==word[-1]:
    count+=1
print(count)
"""
"""
Ex6. Write a Python program to remove duplicates from a list (hint: create a copy of the list to remove items from, or use a list to keep track of the indices of duplicates)
"""
#Method 1
rand_list = []
for i in range(0, 10):
  num = randint(1, 10)
  rand_list.append(num)
print(rand_list)
#create new list without duplicates
cp_rlist = []
for num in rand_list:
  if num not in cp_rlist:
    cp_rlist.append(num)
del rand_list
print(cp_rlist)
