# Python Program to Reverse a Number using While loop by using function
def reverse_number(number):
 reverse = 0
 while(number > 0):
     remainder = number %10
     reverse = reverse *10 + remainder
     number = number // 10
     print("Reverse number is ", reverse)
reverse_number(12345)
