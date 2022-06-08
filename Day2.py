# 1: Adding Two Digits
# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
two_digit_number = input("Type a two digit number: ")
#Get the first and second digits using subscripting then convert string to int.
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
#Add the two digits togeter
two_digit_number = first_digit + second_digit
print(two_digit_number)

#2: BMI Calculator:
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
weight_as_int = int(weight)
height_as_float = float(height)
# Using the exponent operator **
bmi = weight_as_int / height_as_float ** 2
# or using multiplication and PEMDAS
bmi = weight_as_int / (height_as_float * height_as_float)
bmi_as_int = int(bmi)
print(bmi_as_int)

#3: Life in Weeks: https://waitbutwhy.com/2014/05/life-weeks.html
# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
age = input("What is your current age? ")
years = 90 - int(age)
months = round(years * 12)
weeks = round(years * 52)
days = round(years * 365)
print(f"You have {days} days, {weeks} weeks, and {months} months left.")

#4: Tip Calculator
#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places.
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")
print({:.2f}"Each person should pay: ${final_amount}") # this is to get with two decimal points 
