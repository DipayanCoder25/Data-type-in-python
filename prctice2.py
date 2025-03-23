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
'''
import math

num = float(input("Enter a number to find its square root: "))


ans = math.sqrt(num)

print(f"The square root of {num} is {ans}")



