'''num=int(input("Enter a numerator: "))
num2=int(input("Enter a demonerator: "))
if num % num2 ==0:
    print(f"{num} is divisible by {num2}")
else:
    print(f"{num} is not divisible by {num2}")
    
import random
name=input("Enter a name: ")
salami=["1000BDT","120BDT","100BDT","12000000BDT"] 
letter=input("Enter a single character: ")
if len(letter)==1 and letter.isalpha():
    salami_selected=random.choice(salami)
    print(f"{name} has gotten {salami_selected}")
else:
    print("Enter a valid chracter")      
    
mean1=23
total_num=30
wrong_num=14
correct_num=6
sum=mean1*total_num
num2=(sum-(wrong_num)-(correct_num))
print("new num is :",num2)
ans=num2/total_num
print(ans)
  '''
num1=input("Enter a number: ")
num2=input("Enter another number: ")
print("Before swapping num1=",num1,"Num2=",num2) 
temp=num1
num1=num2 
num2=temp
print("After swapping num1=",num1,"Num2=",num2) 