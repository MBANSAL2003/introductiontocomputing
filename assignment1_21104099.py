#question 1

#to find average of thre numbers, first we required to take 3 number
print("enter first number")
n1=input()
print("enter second number")
n2=input()
print("enter third number")
n3=input()
# average of 'n' numbers is the sum of all 'n' numbers divided by n

print("average of three numbers is", float(n1)/3+float(n2)/3+float(n3)/3)

print(100*"-x")

#question 2

#first we take gross income of user
print("gross income of user=")
n1=input()
#now we take standard deduction
print("standard deduction=")
n2=input()
#now we take no of dependent
print("no of dependent")
n3=input()
#For each dependent, a taxpayer is allowed an additional $3,000 deduction
print("additional dependent  deduction=")
n4=input()
#now we calculate taxable income(Taxable income = Gross Income - Standard deduction - (Dependent deduction * No. of dependents)

print("taxable income=", int(n1)-int(n2)-(int(n3)*int(n4)))


#now finally we calculate final income tax by tax=Taxable Income * Tax Rate
print("taxable income=")
n5=input()
print("tax rate=")
#as tax rate is 20% means 20/100=0.2(float value)
n6=input()
# TAX=
print("income tax=", int(n5)*float(n6))

print(100*"-x")

#question 3

#first we take student name, his sid, gender, course name, CGPA

print('name')
n1=input()

print('SID')
n2=input()

print('gender')
n3=input()

print('course name')
n4=input()

print('CGPA')
n5=input()

#now we make a combined list

print('reqiured list(L1)=', [n1,int(n2),n3,n4,float(n5)])


print(100*"-x")

#question 4

#first we take marks of 5 students

print('marks of 1st student')
n1=input()

print('marks of 2nd student')
n2=input()

print('marks of 3rd student')
n3=input()

print('marks of 4th student')
n4=input()

print('marks of 5th student')
n5=input()

#now we make list of the marks
print('list L1=', [float(n1),float(n2),float(n3),float(n4),float(n5)])

L1= [n1,n2,n3,n4,n5]
L1.sort()
print(L1)

print(100*"-x")

#question 5

#list=color ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

n1=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#a)
n1.remove('Black')
print(n1)

#b)
n2=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
n2.remove('Black')
print(n2)
n2.remove('Pink')
print(n2)
n2.insert(3,'Purple')
print(n2)

print(100*"-x")

