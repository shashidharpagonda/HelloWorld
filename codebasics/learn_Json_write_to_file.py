'''
Create address book and write some records in it.
'''

book={}
book['Tom'] = {
    'name':'tom',
    'address':'1 red street NY',
    'phone':908989
}
book['Bob'] = {
    'name':'bob',
    'address':'1 green street NY',
    'phone':87076
}
print('Book type:',type(book))  # To know book is what
import json
s=json.dumps(book)
print(s)
print('s type:',type(s)) # To know s is what

with open('codebasics_files\\book_json.txt','w') as f:
    f.write(s)