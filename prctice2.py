'''a1=int(input("enter the number"))
a2=int(input("Enter the 2nd number"))
a3=int(input("Enter the3rd number"))
sum=a1+a2+a3
percentage=(sum/300)*100
print(percentage)


notes_of_100=amount//100
remaining_of_100=amount%100
notes_of_50=remaining_of_100//50
remaining_of_50=remaining_of_100%50
notes_of_10=remaining_of_50//10
remaining_of_10=remaining_of_50%10
print("The total amount of 100 taka notes: ",notes_of_100)
print("The toal amount of 50 taka notes: ",notes_of_50)
print("The total amount of 10 taka notes: ",notes_of_10)
print("The rest money: ",remaining_of_10)

employe_name="Dipayan"
current_salary=5000000
performance_rating=4.5

incrment_perfonmance=(performance_rating-2)*5
increment_amount=(current_salary**incrment_perfonmance)/100
new_salary=current_salary+increment_amount
# homework all data print by myself
#LOAN EMI
loan_amount=10000
annual_interest_rate=7.5
loan_tenure_rate=10
monthly_interast_rate=annual_interest_rate/12/100
loan_tenure_monthly=loan_tenure_rate*12
#EMI caculating
emi=(loan_amount*monthly_interast_rate*(1+monthly_interast_rate)**loan_tenure_monthly)/\
    (1+monthly_interast_rate**loan_tenure_monthly-1)
print("Loan amount",loan_amount)
print("Monthly amoun",round(emi,2))

import math

num = float(input("Enter a number to find its square root: "))


ans = math.sqrt(num)

print(f"The square root of {num} is {ans}")

loan_amount=input("The total loan amount: ")
annual_interest_rate=input("Enter intarest rate: ")
loan_tenure_years=input("Enter loan tenure year: ")
monthly_interest_rate=annual_interest_rate/12/100
loan_tenure_monthly=loan_tenure_years*12
#EMI calculation formula
emi=(loan_amount*monthly_interest_rate*(1+monthly_interest_rate)**loan_tenure_monthly)/ \
    ((1+monthly_interest_rate)**loan_tenure_monthly-1)


print("Loan Amount: ", loan_amount)
print("Monthly EMI: ",round(emi,2))



# Investment details
principal = input("Enter invesment amount: ")  # Initial investment
annual_rate = input("Enter interest perchentage:   ") # Interest rate in %
times_compounded = 4  # Quarterly
years = input("Enter invesment duration: ")  # Investment duration

# Compound Interest Formula
final_amount = principal * (1 + (annual_rate / (times_compounded * 100))) ** (times_compounded * years)

print("Initial Investment:", principal)
print("Final Amount after", years, "years:", round(final_amount, 2))
print("Total Interest Earned:", round(final_amount - principal, 2))

month_number = int(input("Enter running month number: "))
temp = int(input("Enter today's temperature: "))


if month_number >= 6 and month_number <= 8:
    print("It's summer")
    print("You should wear light clothes.")
    if temp >= 30:
        print("Temperature is hot today.")
    elif temp <= 30:
        print("Temperature is not bad.")


elif month_number >= 3 and month_number <= 5:
    print("It's spring")
    print("You should wear light clothes.")
    if temp >= 30:
        print("Temperature is hot today.")
    elif temp <= 30:
        print("Temperature is not bad.")


elif month_number >= 9 and month_number <= 11:
    print("It's autumn")
    print("Wear heavy clothes and jackets.")
    if temp >= 30:
        print("Temperature is hot today.")
    elif temp <= 30:
        print("Temperature is not bad.")


elif month_number == 12 or month_number == 1 or month_number == 2:
    print("It's winter")
    print("Wear heavy clothes and jackets.")
    if temp >= 30:
        print("Temperature is hot today.")
    elif temp <= 30:
        print("Temperature is not bad.")

else:
    print("Invalid month number. Please enter a number between 1 and 12.")

username=input("Enter username: ")
gmail=input("Enter gmail: ")
if username=="abc" or gmail=="abc@gmail.com":
    print("Accepted")
else:
    print("Denied")
    
#home light control system
motion_deteced=True
is_night=False
manual=True
if motion_deteced and is_night:
    print("Light is on (Motion detected Day time)")
else:
    print("Day time (NO need of light)")
    
if motion_deteced or manual:
    print("Light is on (Motion or manul )")
else:
    print("Light off")  
          
if not manual:
    if motion_deteced and is_night:
        print("Light is on (Automated)")
    else:
        print("Light off (Automated)")
else:
    print("Manul override")        

h=float(input("Enter height: "))
w=float(input("Enter weight: "))
bmi=w/(h*h)
if bmi<18.5:
    print(f"Your BMI is {bmi} and you are underweight")
elif bmi>=18.5 and bmi<=24.9:
    print(f"Your BMI is {bmi} and you are healthy")
elif bmi>=30 and bmi<=34.9:
    print(f"Your BMI is {bmi} and you are obese")
else:
    print(f"Your BMI is {bmi} and you are over unhealty")        
    
marks=int(input("Enter your marks here: "))
if marks>=80 and marks<=100:
    print("A+")
elif marks>=70 and marks<=79:
    print("A")        
elif marks>=60 and marks<=69:   
    print("A-")
elif marks>=50 and marks<=59:   
    print("B")
elif marks>=40 and marks<=49:  
    print("C")
elif marks>=33 and marks<=39:
    print("D")
else:
    print("You are a failure")

a=abs(int(-210))
print(a)
cnt=0
# displaying number with abs
for i in range(100):
   
    if i%2==0:
        cnt+=1
        continue
    else:
         print(a)
     
print(cnt)

x=input("Enter a value: ")
if type(x) is int:
    print("True")
else:
    print("False")
        

num=[10,20,30,40,50.60]
print(34 not in num)

text="Mam"
print("A" in text)

dic={'Name':"Dip","Age":12}
print('a' in dic)

#preventing duplicates entries in a database
data_base=["ID12","ID01","ID02"]
new_entry="ID01"
if new_entry not in data_base:
    print("Entry added succesfully")
else:
    print("Entry already exist in data_base")    
    
#verifying strong passowrd
new_passoword=["abcd","1234","Adminstrator"]
passoword=input("Enter passowrd")
if passoword not in new_passoword:
    print("Passoword strong enough")
else:
    print("Password is weak.Make it strong")
    
a=5#0101
b=3#0011
print(a&b)
print(a|b)
print(a^b)
print(a*b)  
print(~b)
print(a<<b)
print(a>>b)

markone=int(input("Enter mark: "))
mark2=int(input("Enter mark 2:"))
mark3=int(input("Enter mark 3: "))
marks=markone+mark2+mark3
marks=marks/3
if marks>=80 and marks<=100:
    print("A+")
elif marks>=70 and marks<=79:
    print("A")        
elif marks>=60 and marks<=69:   
    print("A-")
elif marks>=50 and marks<=59:   
    print("B")
elif marks>=40 and marks<=49:  
    print("C")
elif marks>=33 and marks<=39:
    print("D")
else:
    print("You are a failure")  
    '''  
a=5
print(a<<1)
print(a>>1)
          