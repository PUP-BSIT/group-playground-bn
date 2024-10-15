choice = input("Enter your choice: ")

match choice:

    case "1":
        # (Ynion): Write a program that takes 2 numbers and tell whether the numbers are equal or not.
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        if num1 == num2:
            print("The numbers are equal.")
        else:
            print("The numbers are not equal.")

    case "2":
        # (Relente) Write a program that takes a number and tell whether the number is odd, even, or zero.
        num = int(input("Enter a number: "))

        if num == 0:
            print("Zero")
        elif num % 2 != 0:
            print("Odd number.")
        else:
            print("Even number.")

    case "3":
        # TODO (Delima): Do item 3.
        pass

    case "4":
        # TODO (Quiambao): Do item 4.
        pass

    case "5":
        # TODO (Citron): Do item 5.
        pass

    case "6":
        # (Relente) Write a program that takes a 2-digit number and returns the sum of the 2 digits. Ex. 24 -> 6
        num = int(input("Enter a 2-digit number: "))

        digit1 = num // 10
        digit2 = num % 10

        sum_of_digits = digit1 + digit2

        print(f"The sum of the digits is: {sum_of_digits}")