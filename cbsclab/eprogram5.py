"""
Write a program to input the value of x and n and print the sum of the
following series:
 1+x+x2+x3+x4+ ............xn

   Formula: 1+[ x(x^n−1)/x-1] If x>1.

 1-x+x2-x3+x4 + ......... xn

 x/1 + x2/2 - x3/3 + x4/4 + ........... xn/n

 x + x2/2! - x3/3! + x4/4! + ............ xn/n!

"""
import math


def series1(x,n):
    total=1
    for i in range(1,n+1):
        if i<=n:
            #print('i:',i,'pow(x,i):',str(pow(x,i)))
            total= total +pow(x,i)
    return total


def series2(x,n):
    total=1
    for i in range(1,n+1):
        if i<=n:
            if i%2 != 0:
                total= total - pow(x,i)
            elif i%2 == 0:
                total = total + pow(x, i)
    return total


def series3(x,n):
    total=1
    for i in range(1,n+1):
        if i<=n:
            if i%2 != 0:
                total = total - pow(x, i)/i
            else:
                total = total + pow(x, i)/i
    return total


def series4(x,n):
    total=1
    for i in range(1,n+1):
        if i<=n:
            if i % 2 != 0:   # Odd Num in series
                total = total - pow(x, i)/math.factorial(i)
            else:  # Even num in series
                total = total + pow(x, i)/math.factorial(i)
    return total


x=int(input('Series4: Enter the value of x:'))
n=int(input('Series4: Enter the value of n:'))

sum_series1=series1(x,n)
print('Sum of series:',str(sum_series1))
sum_series2=series2(x,n)
print('Sum of series:',str(sum_series2))
sum_series3=series3(x,n)
print('Sum of series:',str(sum_series3))
sum_series4=series4(x,n)
print('Series4: Sum of series:',str(sum_series4))