#QUESTION 1

#“Python is a case sensitive language”.

#a)
str="Python is a case sensitive language"
# to find length og string
print(len(str))
#b)
# for reversing order of string
print(str[::-1])

#c)
# for printing just a case sensitive
y=str[10:26]
print(y)

#d)
# for replacing a 'case sensitve' with 'object oriented'
print(str.replace("a case sensitive","object oriented"))

#e)
#for finding position of 'a' in our original string
print(str.index("a"))

#f)
#for removing all white spaces
print(str.replace(" ",""))

print(100*"-x")

#QUESTION 2
# first we take input from user in name, sid, department and cgpa

print("name")
n1=input()

print("sid")
n2=input()

print("department")
n3=input()

print("cgpa")
n4=input()
# now printing a string containing required data
print('Hey',n1,'Here!')
print('my SID is', int(n2))
print('I am from',n3,"department and my CGPA is",n4)

print(100*"-x")

#QUESTION 3

a=56
b=10

#a)
print(a&b)

#b)
print(a|b)

#c)
print(a^b)

#d)
print(a<<2)
print(b<<2)

#e)
print(a>>2)
print(b>>4)

print(100*"-x")

#QUESTION 4

#finding greatest of 3 numbers
#lets first take 3 numbers and numbers can be decimal as well so we use float

num1=float(input("enter the first number:"))
num2=float(input("enter the second number:"))
num3=float(input("enter the third number:"))

# now we use if and else condition

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

   print('largest number is:', largest)

print(100*"-x")

#QUESTION 5
str="my name is mehul"
# now we use if and else condition to find whether word 'name' is present or not..
if 'name' in str:
   print("yes")
else:
    print('no')

print(100*"-x")
    
#QUESTION 6
# first we take sides of triangle and as specified in question it should be integers
num1=int(input("enter the length of 1st side "))
num2=int(input("enter the length of 2nd side "))
num3=int(input("enter the length of 3rd side "))
 # now we again use if and else condition as we know traingle will form only when sum of any 2 sides is greater than third side
if  num1+num2>num3 and num2+num3>num1 and num3+num1>num2:
   print("yes, a triangle can be formed")

else:
   print("no, A triangle cannot be formed")
