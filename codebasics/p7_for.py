# ## Exercise: Python for loop
# 1. After flipping a coin 10 times you got this result,
# ```
# result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
# ```
# Using for loop figure out how many times you got heads
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
heads=0
for res in result:
    if res=='heads': heads +=1
print(f'total heads in a result {heads}')

# 2. Print square of all numbers between 1 to 10 except even numbers
print('2 Print square of all numbers between 1 to 10 except even numbers')
for i in range(1,11,1):
    if i%2 ==0:
        continue
    print(f'{i} square: {i**2}')

# 3. Your monthly expense list (from Jan to May) looks like this,
# ```
# expense_list = [2340, 2500, 2100, 3100, 2980]
# ```
# Write a program that asks you to enter an expense amount and program
# should tell you in which month that expense occurred. If expense is not
# found then it should print that as well.
print('\nExercise 3')
expense_list = [2340, 2500, 2100, 3100, 2980]
month_list= ['January','February','March','April','May']
exp= int(input('Enter the expense value to check:'))

result3= exp in expense_list
if not result3:
    print('Not found')
else:
    indexVal= expense_list.index(exp)
    print(f'{exp} occured in {month_list[indexVal]}')

print('\nExercise3 solution2')
month = -1
for i in range(len(expense_list)):
    if exp == expense_list[i]:
        month = i
        break
if month != -1:
    print(f'You spent {exp} in {month_list[month]}')
else:
    print(f'You didn\'t spend {exp} in any month')

# 4. Lets say you are running a 5 km race. Write a program that,
#    1. Upon completing each 1 km asks you "are you tired?"
#    2. If you reply "yes" then it should break and print "you didn't finish the race"
#    3. If you reply "no" then it should continue and ask "are you tired" on every km
#    4. If you finish all 5 km then it should print congratulations message
print('\nExercise4 ')
counter=0
for i in range(5):
    print(f'You ran{i+1} kms')
    tired=input("Are you tired? Say Y/N:")
    if tired == 'Y':
        break;
if i ==4: # 4 because the index starts from 0
    print("Hurray! You are a rock star! You just finished 5 km race!")
else:
    print("You didn't finish 5 km race but hey congrats anyways! You still ran {i+1} miles")

# 5. Write a program that prints following shape
# ```
# *
# **
# ***
# ****
# *****
# ```

for i in range(1,6):
    s=''
    for j in range(i):
       s+='*'
    print(s)