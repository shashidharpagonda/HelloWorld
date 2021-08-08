"""Find the largest/smallest number in a list/tuple"""
size=int(input('How many numbers you want to enter:'))
lst=[]
for i in range(size):
    number=int(input('Enter num :'))
    lst.append(number)

print('Largest number in a list is',max(lst))
print('Smallest number in a list is',min(lst))