#Q.1

# year = int(input("Enter a year:"))

# if (year % 400 == 0) and (year % 100 == 0):
#     print(year,"is a leap year")

# elif (year % 4 == 0) and (year % 100 != 0):
#     print(year,"is a leap year")

# else:
#     print(year,"is not a leap year")
  
#Q.2

# num = float(input("Enter a no.:"))

# if (num > 0):
#     print(num,"is a positive number")

# elif (num < 0):
#     print(num,"is a nagetive number")

# else:
#     print("this is zero") 

#Q.3

# a = float(input("Enter value of a:"))
# b = float(input("Enter value of b:"))
# (a, b) = (b, a)
# print("After swap a =",a,"b =",b)

#Q.4

# a = float(input("Enter value of a:"))
# b = float(input("Enter value of b:"))
# c = float(input("Enter value of c:"))

# if (a > b) and (a > c):
#     print("a is grestest")
# elif (b > c):
#     print("b is greater")
# else:
#     print("c is greater") 
       
#Q.5
    
# import random

# num = random.randint(0,10)
# print(num)

#Q.6

# for num in range (1, 100+1):
#     if (num > 1):
#         for i in range (2, num):
#             if (num % i == 0):
#                 break
#         else:
#              print(num)

#Q.7

# f = c * 9/5 + 32

# celsius = float(input("Enter temperature:"))

# fahrenheit = celsius * 9/5 + 32

# print(celsius,"c =",fahrenheit,"f")

#Q.8

# num  = int(input("Enter a number:"))
# fact = 1

# if (num < 0):
#     print("factorial not exists")
# elif (num == 0):
#     print("factorial of 0 is",1)
# elif (num > 0):
#     for i in range(1, num + 1):
#         fact = fact * i
#     print("factorial of",num,"is",fact)            

# def fact(n):
#     if(n == 0 or n == 1):
#         return 1
#     return fact(n-1) * n

# print(fact(2))

#Q.9

# n = int(input("Enetr a no.:"))
# for i in range (1, 11):
#     print(n,"*",i,"=",n * i) 

#Q.10

# a = 0
# b = 1

# num = int(input("enter a number for fibonacci sequance:"))

# if (num == 1):
#     print(a)
# else:
#     print(a)
#     print(b)

#     for i in range(2, num):
#         c = a + b
#         a = b
#         b = c
#         print(c) 

#Q.11

# lower = int(input("Enter lower limit:"))
# upper = int(input("Enter upper limit:"))

# for num in range (lower, upper + 1):
#     order = len(str(num))
#     sum =0
#     tem = num 

#     while (tem > 0):
#      digit = tem % 10
#      cube = digit ** order
#      sum = sum + cube
#      tem //= 10

#     if (sum == num):
#        print(num)      
 
#Q.12

# n = int(input("Enter limit: "))
# sum = 0
# for num in range (1, n + 1):
#        sum = sum + num
# print("the sum of",n,"natural numbers is",sum)


#Q.13

# a = int(input("Enter a number:"))
# for i in range(1, 101):
#     if (i % a == 0):
#         print(i)
    
#Q.14

# decimal = int(input("Enter a decimal no. to covert:"))

# print(bin(decimal), "in binary")
# print(oct(decimal),"in octal")
# print(hex(decimal),"in binary")

#Q.15

# char = "p"
# print("The ASCII value of",char,"is",ord(char))

#Q.16

# num = int(input("ENter a no.:"))
# for i in range(1, 101):
#     if (i % num == 0):
#         print(i)

#Q.17

a = int(input("Enter first digit:"))
b = int(input("Enter second digit:"))

print("Available choices are:\nchoice1: +\nchoice2: -\nchoice3: *\nchoice4: /")

choice = int(input("Enetr your choice:"))

if (choice == 1):
    print(a+b)
elif (choice == 2):
    print(a-b)
elif (choice == 3):
    print(a*b)
elif (choice == 4):
    print(a/b)

