"""
Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out,

"""
exp1=[2200,2350,2600,2130,2190]
print('Your list has\n',exp1)
#1. In Feb, how many dollars you spent extra compare to January?
print('1.1 No of dollars you spent more in Feb compare to Jan:',exp1[1]-exp1[0],'$')

#2. Find out your total expense in first quarter (first three months) of the year.
print('\n1.2 Total expenses in first quarter:',exp1[0]+exp1[1]+exp1[2])

#3. Find out if you spent exactly 2000 dollars in any month
spent=2000
try:
    result=exp1.index(2000)
except ValueError as e:
    result=-1
if result ==-1:
    print('\n1.3 No match found with ',spent,'$ in the list')
else:
    print('\n1.3 Match found with ',spent,'$ in the list')

print('\n1.3 Smart Solution is ')
print('Did i spend 2000$ in any month?',2000 in exp1)

#4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
exp1.append(1980)  #Append will add at end of ur list
print('\n1.4 After june month expenses, ur list has\n',exp1)

#5. U returnd an item that u bought in April and got refund of 200$. Make correction to ur monthly expense list based on this
exp1[3]=exp1[3]-200
print('\n1.5 After April month refund, your list has\n',exp1)
"""
You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']
Using this find out below,
"""

heros=['spider man','thor','hulk','iron man','captain america']
print('\n#### 2 Qos')
print('List has',heros)

#1. Length of the list
len1= len(heros)
print('2.1 Length of the list',str(len(heros)))

#2. Add 'black panther' at the end of this list
heros.append('black panther')
print('\n2.2 After adding BLACK PANTHER to list',heros)

#3. You realize that you need to add 'black panther' after 'hulk',so remove it from the list first and then add it after 'hulk'
hulk_index=heros.index('hulk')
heros.remove('black panther')
heros.insert(hulk_index+1,'black panther')
print('\n2.3. After updating BLACK PANTHER position in a list',heros)

#4. Now you don't like thor and hulk because they get angry easily :)
   # So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   # Do that with one line of code.
heros[1:3]=['doctor strange']
print('\n2.4 thor and hulk to doctor strange\n',heros)

#5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heros.sort()
print('\n2.5 sorted',heros)