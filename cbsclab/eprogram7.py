"""Input a number and check if the number is a prime or composite number.

    https://en.wikipedia.org/wiki/List_of_prime_numbers
"""
def isPrimeorComposite(num):
    count =0
    for i in range(2,num):
        if num%i == 0:
            count +=1
            break
    if count >=1:
        print(num,' is a composite number')
    else:
        print(num, ' is a prime number')

num = int(input('enter a integer number:'))
isPrimeorComposite(num)