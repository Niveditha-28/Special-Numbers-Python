# To reverse a number
def reverse_number(num):
    rev = 0
    temp = num

    while temp > 0:
        digit = temp % 10       # Get last digit
        rev = rev * 10 + digit  # Append digit to reversed
        temp = temp // 10       # Remove last digit
    return rev

#1. To check Palindrome
def Palindrome():
    print("To check Palindrome :")
    num = int(input("Enter a number: "))
    if num == reverse_number(num):
        print(num, "is a Palindrome Number")
    else:
        print(num, "is not a Palindrome Number")

#2. To check Armstrong
def Armstrong():
    print("To check Armstrong : ")
    num = int(input("Enter a number: "))
    n = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum = sum + (digit**n)
        temp = temp // 10
    if num == sum:
        print(num, "is Armstrong number")
    else:
        print(num, "is not Armstrong number")

#3. To check Perfect Number
def Perfect():
    print("To check Perfect Number:")
    num = int(input("Enter the number : "))
    sum = 0
    for i in range(1, num // 2 - 1):
        if num % i == 0:
            sum = sum + i
    if sum == num:
        print(num, "is a Perfect Number")
    else:
        print(num, "is not a Perfect Number")  

#4. To check Strong Number   
def Strong():
    print("To check Strong Number :")
    num = int(input("Enter a number: "))
    temp = num
    sum = 0
    def factorial(n):
        fact = 1
        for i in range(1, n+1):
            fact *= i
        return fact
    while temp > 0:
        digit = temp % 10
        sum += factorial(digit)
        temp //= 10
    if sum == num:
        print(num, "is a Strong Number")
    else:
        print(num, "is not a Strong Number")

#5. To check Automorphic Number
def Automorphic():
    print("To check Automorphic Number :")
    num = int(input("Enter a number: "))
    square = num * num
    n = len(str(num))
    if (square % 10**n) == num:
        print(num, "is an Automorphic Number")
    else:
        print(num, "is not an Automorphic Number")  

 #6. To check Harshad (Niven) Number
def Harshad():
    print("To check Harshad (Niven) Number :")
    num = int(input("Enter a number: "))
    sum = 0
    temp = num
    while temp > 0:
        sum = sum + (temp % 10)
        temp = temp // 10
    if num % sum == 0:
        print(num, "is a Harshad (Niven) Number")
    else:
        print(num, "is not a Harshad (Niven) Number") 

#7. To check Neon Number
def Neon():
    print("To check Neon Number :")
    num = int(input("Enter a number: "))
    square = num * num
    sum = 0
    while square > 0:
        sum = sum + (square % 10)
        square = square // 10
    if sum == num:
        print(num, "is a Neon Number")
    else:
        print(num, "is NOT a Neon Number")


#8. To check Spy Number 
def Spy():
    print("To check Spy Number :")
    num = int(input("Enter a number: "))
    sum = 0
    product = 1
    while num > 0:
        digit = num % 10
        sum = sum + digit
        product = product * digit
        num = num // 10
    if sum == product:
        print(num, "is a Spy Number")
    else:
        print(num, "is NOT a Spy Number")

#9. To check Kaprekar Number
def kaprekar():
    num = int(input("Enter the number : "))
    square = num * num
    n = len(str(num))
    divisor = 10**n
    right = square % divisor
    left = square // divisor
    if left+right == num:
        print(num, "is Kaprekar Number")
    else:
        print(num, "is not Karpekar Number")
        

#10. To check Magic Number
def Magic():
    num = int(input("Enter the number : "))
    temp = num
    while temp > 9:
       sum =0
       while temp > 0:
           sum = sum + (temp %10)
           temp = temp // 10
       temp = sum
    if temp == 1:
        print(num, "is a Magic Number")
    else:
        print(num, "is not a Magic Number")    

# Main Program
# To print the special number options
print("Special Numbers")
print("Select the below options to verify the special numbers")
print("Palindrome Number [1]")
print("Armstrong [2]")
print("Perfect Number [3]")
print("Strong Number [4]")
print("Automorphic Number [5]")
print("Harshad (Niven) Number [6]")
print("Neon Number [7]")
print("Spy Number [8]")
print("Kaprekar Number [9]")
print("Magic Number [10]")
choice=int(input("Enter your choice : "))
match choice:
    case 1:
        Palindrome()
    case 2:
        Armstrong()
    case 3:
        Perfect()
    case 4:
        Strong()
    case 5:
        Automorphic()
    case 6:
        Harshad()
    case 7:
        Neon()
    case 8:
        Spy()
    case 9:
        kaprekar()
    case 10:
        Magic()
    case _:
        print("Invalid Choice")