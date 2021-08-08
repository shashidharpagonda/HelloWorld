"""
1. Create 3 variables to store street, city and country, now create address variable to store entire address.
   Use two ways of creating this variable, one using + operator and the other using f-string.
   Now Print the address in such a way that the street, city and country prints in a separate line
"""
street='streetName'
city='cityName'
country='countryName'
address ="street + '\n' + city + '\n' + country"
print("Address using plus operator: ",address)
address =f'{street}\n{city}\n{country}\n'
print("Address using f-string: ",address)

"""
2. Create a variable to store the string "Earth revolves around the sun"
   Print "revolves" using slice operator
   Print "sun" using negative index
"""
str="Earth revolves around the sun"
print(str[6:14])
print(str[-3:],'\n')

"""
3. Create two variables to store how many fruits and vegetables you eat in a day. 
   Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday. 
   Use python f string for this.
"""
fruits=3
vegs=2
print(f'3 I eat {vegs} veggies and {fruits} fruits daily \n')

"""
4. I have a string variable called s='maine 200 banana khaye'. 
   This of course is a wrong statement, the correct statement is 'maine 10 samosa khaye'. 
   Replace incorrect words in original strong with new ones and print the new string. Also try to do this in one line.
"""
s='maine 200 banana khaye'
print('4 original str:  ',s)
s=s.replace("banana","samosa")
s=s.replace("200","10")
print('4 after replace:  ',s)