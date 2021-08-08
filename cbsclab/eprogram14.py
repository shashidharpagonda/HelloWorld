"""● Input a list/tuple of elements, search for a given element in the list/tuple.
"""

list=[1,2,3,4,5,6,7,8,9]
searchVal=3
if list.count(searchVal)>0:
    print(searchVal,' is found in',list)
else:
    print(searchVal, ' is Not found in', list)