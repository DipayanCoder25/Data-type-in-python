''' print('Step 1: start')
print("Step 2:Declar x,y,sum")
print("Step 3:Input values x and y")
print("Step 4: Sum = x+ y")
print("step 5:Display sum")
print("Stop")
x = 10
y = 20
sum = x+y
print(sum)
print("the sum is :",sum)
print(f'= Sum :{sum}')
team_a_a=13
team_a_b=13
team_a_c=13

team_b_a=13

team_b_b=13
team_b_c=13
# calculte ths sum
team_a_total_score= team_a_c+team_a_b+team_a_a
team_b_total_score = team_b_a+team_b_b+team_b_c
print(f'The total sum of team a is :{team_a_total_score}')
print(f'The total sum of team b is :{team_b_total_score}')

'''
'''
name  ="Dipayan"
age = 12
grade = 7
height = 5.6
student_id = True 
print("Name is",name)
print("Age is ",age)
print("Grade is ",grade)
print("Height is ",height)
print("Student Id is ",student_id)

print(f"My name is {name} and age is {age} and grade is {grade} and height is {height} and student id is {student_id} ")
'''
'''
height =float(input("Height"))
base =float(input("Base "))
area = 0.5*height*base
print(f"Area is {area}")
'''
'''
r =float(input("Enter radious "))
area = 3.1416*r*r
print("Area is ",area)

h=int(input("enter height"))
area = 4*h
print("Area is ",area)
'''
'''
import keyword
print(keyword.kwlist)

b1=float(input("base 1 is "))
b2=float(input("Base 2 is "))
h=float(input("Height is "))
area =0.5*(b1+b2)*h
print("Area is ",area)

a =4
b= 2
c=5
d=4
x=int(input("Input x :"))
y=int(input("Input y :"))
ans =a*x*x+b*y*y*y+c*x+d
print("Ans is :",ans)

age=int(input("Enter your age: "))
if age>=18:
    print("You are eligable to vote")
    print("You are inside of if condition")
print("Your outside of if condition")
    
num=int(input("Enter a number"))
if num>0:
    print("Positive number")
else:
    print("Negative number") 
       
username=input("Enter username: ").lower()
if username== "admin":
    print("Login succesful done")
else:
    print("Login denied done")    
    
price=input("Enter price: ")
sale_price=input("Enter sale price: ")
if price<sale_price:
    profit=sale_price-price
    print("Profit is {0}".format(profit))
else:
    print("No profit")    
     
run=int(input("Enter the total run: "))
ball=int(input("Enter the total balls faced : "))    
strike_rate=(run/ball)*100
if  strike_rate>=150:
    print("Amazing performane {:2}".format(strike_rate))
else:
    print("Good try.Mybe do better next time {:2}".format(strike_rate))
'''
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
c=int(input("Enter a number: "))  
if a>b and a>c:
    print("A is the largest of three integers")
elif b>a and b>c:
    print("B is the largest of three integers")
else:
    print("C is the largest")    
      
