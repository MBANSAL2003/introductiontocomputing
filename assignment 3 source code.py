#QUESTION 1

#Python Program to Count Occurrence of a Character in a String

string = input("Please enter your own String : ")
char = input("Please enter your own Character : ")
i = 0
count = 0

while(i < len(string)):
    if(string[i] == char):
        count = count + 1
    i = i + 1

print("The total Number of Times ", char, " has Occurred = " , count)


print(100*("-x"))

#QUESTION 2

#to get next date of given day

year=int(input(" WRITE THE YEAR:"))

if(year % 400==0):
    leap_year=True
elif(year % 100==0):
    leap_year=False
elif(year % 4==0):
    leap_year=True
else:
    leap_year=False

#taking month as input from user

month=int(input("WRITE A MONTH[1-12]:"))

if month in(1,3,5,7,8,10,12):
    month_duration=31
elif month==2:
    if leap_year:
        month_duration=29
    else:
        month_duration=28
else:
    month_duration=30
            
#taking date as input from user

day=int(input('WRITE THE DAY[1-31]:'))

if day<month_duration:
    day+=1
else:
    day=1
    if month==12:
        month=1
        year+=1
    else:
        month+=1
            

#printing out the next day from given date input by user

print('THE NEXT DATE IS [YYYY/MM/DD] %d-%d-%d.'%(year,month,day))


print(100*("-x"))


#QUESTION 3

my_list = [3,9,10]
print('The list is')
print(my_list)
print('The resultant tuple is :')
my_result = [(val, pow(val, 2)) for val in my_list]
print(my_result)

print(100*("-x"))


# QUESTION 4

#firstly take input of grade from the user...
print('enter grade of student:')
n1=int(input())

if n1==10:
    print("your grade is 'A+' and outstanding performance")
elif n1==9:
    print("your grade is 'A' and excellent performance")
elif n1==8:
     print("your grade is 'B+' and very good performance")
elif n1==7:
     print("your grade is 'B' and good performance")
elif n1==6:
     print("your grade is 'C+' and average performance")
elif n1==5:
     print("your grade is 'C' and below average performance")
elif n1==4:
     print("your grade is 'D' and poor performance")
else:
    print('error')

print(100*("-x"))


#QUESTION 5

i=0
a="ABCDEFGHIJK"
for i in range(6):
    j=i
    while (j>0):
        print(" ",end="")
        j=j-1
    k=0
    for k in range (len(a)-2*i):
        print(a[k],end="")
        
    print("")
   
  
# QUESTION 6

sid=int(input("Enter your sid: \n"))
name=input("Enter name: \n")
students={sid:name}

while True:
    option=input("Do you want to enter another student entry(Y or N):").upper()
    if option=='Y':
        sid=int(input("Enter sid: "))
        name=input("Enter name: ")
        students[sid]=name
    elif option=='N':
        break
    else:
        print("Invalid input!")

# part(a)-print the dictionary
print("<a>\n",students)

#part (b)-sort according to the names
print("<b>\n",{k:v for k,v in sorted(students.items(), key=lambda x:x[1])})

#part (c)-sort according to the sids 
print("<c>\n",{k:v for k,v in sorted(students.items())})

#part (d)-search for a student by their sid 
sid=int(input("Search Name with SID: \n"))
print("<d>\n",students[sid])

print(100*("-x"))


# QUESTION 7
    
# Function to display the Fibonacci sequence
def recur_fibo(n):
    if n<=1:
        return n
    else:
        return(recur_fibo(n-1)+recur_fibo(n-2))
no_of_terms=int(input("ENTER THE NUMBER OF TERMS IN THE SERIES:  \n"))
if no_of_terms <=0:
    print("Please enter positive integer")
else:
    print("Fibonacci sequenceL: ")
    sum=0
    for i in range(no_of_terms):
        print(recur_fibo(i))
        sum=sum+recur_fibo(i)
avg=float(sum/no_of_terms)
print("AVERAGE OF THE RESULTANT FIBONACCI SERIES IS: ",avg)

print(100*("-x"))


# QUESTION 8

Set_1 ={1,2,3,4,5}
Set_2 ={2,4,6,8}
Set_3 ={1,5,9,13,17}

#part (a)
Set_union=Set_1.union(Set_2)
Set_intersection=Set_1.intersection(Set_2)
Part_A_Set=Set_union - Set_intersection
print("<a>\n",Part_A_Set)

#part (b)-eliminating intersection of sets taken two at a time from the union of all three sets 
Part_B_set= Set_1.union(Set_2.union(Set_3))- Set_1.intersection(Set_2) -Set_2.intersection(Set_3) - Set_3.intersection(Set_1)
print("<b>\n",Part_B_set)

# part (c)-subtracting intersection of three from two taken at one time
Part_C_Set=((Set_1.intersection(Set_2)).union((Set_1.intersection(Set_3)).union(Set_2.intersection(Set_3))))-(Set_1.intersection(Set_2.intersection(Set_3)))
print("<c>\n",Part_C_Set)

#part (d)- ignoring the numbers from 1 to 10 that are occuring in set1
Part_D_Set=set()
for i in range(1,11):
    if i not in Set_1:
        Part_D_Set.add(i)
print("<d> \n",Part_D_Set)

#part e
Part_E_Set=set()
if i in range(1,11):
    if i not in Set_1 and i not in Set_2 and i not in Set_3:
        Part_E_Set.add(i)
print("<e>\n",Part_E_Set)

print(100*("-x"))


    
    
