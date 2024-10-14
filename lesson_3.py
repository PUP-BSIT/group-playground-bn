choice = input("Enter your choice: ")

switch choice:

case "1":
    # TODO(Ynion): Do item 1.

case "2":
#(Relente) Write a program that takes a number and tell whether the number is odd, even, or zero.

num = int(input("Enter a number: "))

if num == 0:
    print("Zero")
elif num % 2 != 0:
    print("Odd number.")
elif num % 2 == 0:
    print("Even number.") 

case "3":
# TODO(Delima): Do item 3.

case "4":
# TODO(Quiambao): Do item 4.

case "5":
# TODO(Citron): Do item 5.

case "6":
# (Relente) Write a program that takes a 2 digit number and returns the sum of the 2 digits. Ex. 24 -> 6

num = int(input("Enter a 2-digit number: "))

digit1 = num // 10
digit2 = num % 10

sum_of_digits = digit1 + digit2

print(f"The sum of the digits is: {sum_of_digits}")
