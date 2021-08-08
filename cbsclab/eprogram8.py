"""Display the terms of a Fibonacci series."""

def fibSeries(num):
    fiblist=[0,1]
    num1=0
    num2=1

    if num ==0:
        print('fib series till ',num,' are: ',num1)
    elif num ==1:
        print('fib series till ', num, ' are: ', num2)
    else:
        for i in range(2,num):
            sum=num1+num2
            fiblist.append(sum)
            #Now swap num1 and num2 to get last previous 2 nums
            num1=num2
            num2=sum
        print('fib series till ', num, ' are: ', fiblist)

num= int(input('enter a number to list fib series: '))
fibSeries(num)