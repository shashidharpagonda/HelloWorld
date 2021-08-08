"""Compute the greatest common divisor and least common multiple of two integers.
    lcm(a, b) = ab/gcd(a,b)
"""
def gcdAndlcm(num1, num2):
    num1list=[]
    num2list=[]
    # Find the factors for num1
    for i in range(2,num1-1):
        if num1%i ==0:
            num1list.append(i)
    # Find the factors for num2
    for i in range(2,num2-1):
        if num2%i ==0:
            num2list.append(i)

    print(num1,' factors are: ',num1list)
    print(num2,' factors are: ',num2list)
    #Iterate num1list and num2list to know the GCD
    #To iterate, we should know till what value in the list you should iterate

    size=0
    iteratelist=[]
    largelist=[]
    if len(num1list) < len(num2list):
        size=len(num1list)
        iteratelist.extend(num1list)
        largelist.extend(num2list)
    else:
        size=len(num2list)
        iteratelist.extend(num2list)
        largelist.extend(num1list)

    print('iterate list:',iteratelist)
    print('large list',largelist)

    gcd=1
    for i in range(0,size):
        temp=iteratelist[i]
        if largelist.count(temp)>0:
            if gcd < iteratelist[i]:
                gcd=iteratelist[i]
    print('gcd of ',num1,' and ',num2,' are:',gcd)

    lcm=num1*num2/gcd
    print('lcm of ', num1, ' and ', num2, ' are:', str(lcm))

num1 = int(input('enter num1: '))
num2 = int(input('enter num2: '))
gcdAndlcm(num1,num2)
# 300 and 45