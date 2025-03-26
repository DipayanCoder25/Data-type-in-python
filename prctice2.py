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
'''
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


