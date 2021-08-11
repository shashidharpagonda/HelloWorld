'''
Read json from a file
'''
import json

with open('codebasics_files\\book_json.txt','r') as f:
    str1= f.read()
    print('str1',str1) #It is JSON of string
    print(type(str1))

    str2 =json.loads(str1)
    print('str2', str2) #It is of dict
    print(type(str2))

