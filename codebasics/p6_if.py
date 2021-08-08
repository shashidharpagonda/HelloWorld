## Exercise: Python If Condition
# 1. Using following list of cities per country,
#     ```
#     india = ["mumbai", "banglore", "chennai", "delhi"]
#     pakistan = ["lahore","karachi","islamabad"]
#     bangladesh = ["dhaka", "khulna", "rangpur"]
#     ```
# Write a program that asks user to enter a city name and it should tell which country the city belongs to

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city=input('enter the city you want to search:')

if city in india:
    print(city,' is in india')
elif city in pakistan:
    print(city,' is in pakistan')
elif city in bangladesh:
    print(city,' is in bangladesh')
else:
    print('Sorry your',city,'is not in our database')

"""
Write a program that asks user to enter two cities and it tells you if they both are in same country or not. 
For example if I enter mumbai and chennai, it will print "Both cities are in India" 
but if I enter mumbai and dhaka it should print "They don't belong to same country"
"""
city1=input('enter the city1 you want to search:')
city2=input('enter the city2 you want to search:')

check=False
country=''
if city1 in india and city2 in india:
    check=True
    country='india'
elif city1 in pakistan and city2 in pakistan:
    check=True
    country='pakistan'
elif city1 in bangladesh and city2 in bangladesh:
    check=True
    country='bangladesh'

if check: print(city1,' and ',city2,' are in ',country)
else: print(city1,' and ',city2,' are not in same country ')