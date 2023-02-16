""" Problem 2: Prime Number or Not Check """
class Prime_Checker:

    def prime_Check(number):
        if number <= 1:
            return -1
        for i in range(2, int(number**0.5)+1):
            if number % i == 0:
                return -1
        return 1

    def sum_of_number(number):
        total = 0
        for i in range(number + 1):
            total += i
        return total

    num = int(input("Enter a Number: "))
    if prime_Check(num) == 1 :
        total = sum_of_number(num)
        print("The sum of all numbers from 0 to", num, "=", total)
    else:
        print(prime_Check(num))