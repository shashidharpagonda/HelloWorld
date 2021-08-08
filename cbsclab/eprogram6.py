"""Determine whether a number is a perfect number, an armstrong number or a
palindrome."""

"""
What is perfect num:
    A number is a perfect number if is equal to sum of its proper divisors, 
    that is, sum of its positive divisors excluding the number itself.
    
    Eg1: 18
        proper factors of 18 are 1, 2, 3, 6, and 9
            If sum of the factors is equal to 18, then 18 is a perfect number.
            1 + 2 + 3 + 6 + 9 = 6 + 6 + 9 = 12 + 9 = 21
        Therefore, 18 is not perfect.
        
    Eg2: 28
        proper factors of 28 are 1,2,4,7,14
            1+2+4+7+14 =28
        Therefore, 28 is perfect.
        
    First 5 perfect numbers are 6, 28, 496, 8128, 33550336
    
What is Armstrong num:
    An Armstrong number of three digits is an integer such that,
    sum of the cubes of its digits is equal to the number itself.
    Eg:
        153=1^3 + 5^3 + 3^3= 1 + 125 + 27
    
    3 digit Armstrong numbers of the first kind; they are 153, 370, 371, 407.
    
    Eg: 4 digit armstrong number
        1634 = 1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256
         
    4 digit Armstrong numbers are 1634, 8208, 9474 
"""

# First 5 perfect numbers are 6, 28, 496, 8128, 33550336
def isPerfectNum(num):
    sum = 1
    if num % 2 == 0:  # We are checking here if we get odd num then it is not a perfact number
        for i in range(2, num - 1):
            if num % i == 0:
                sum = sum + int(num / i)
    if sum == num:
        print(f'{str(num)}  is perfect number.')
    else:
        print(f'{str(num)}  is not perfect number.')

# 3 digit Armstrong numbers of the first kind; they are 153, 370, 371, 407.
# 4 digit Armstrong numbers are 1634, 8208, 9474
def isArmstrongNum(num):
    powerNum = len(str(num))
    sum = 0
    num2 = num
    i = 1
    while (i <= len(str(num))):
        if num2 % 10 != 0:
            temp = num2 % 10
            sum = sum + temp ** powerNum
            num2 = int(num2 / 10)
        i += 1

    if sum == num:
        print(num,' is armstrong number')
    else:
        print(num,' is not an armstrong number')


def isPalindrome(num):
    num1=num
    revNum=0
    i=1
    while i<=len(str(num)):
        temp = num1 % 10
        revNum = revNum * 10 + temp
        num1 = int(num1 / 10)
        i += 1
    if revNum == num:
        print(num,' is a palindrome')
    else:
        print(num, ' is not a palindrome')

num = int(input('enter a integer number:'))
isPerfectNum(num)
isArmstrongNum(num)
isPalindrome(num)