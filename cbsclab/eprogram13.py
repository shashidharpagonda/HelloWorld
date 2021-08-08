"""● Input a list of numbers and swap elements at the even location with the
elements at the odd location.
"""
def swap(list):
    # size=len(list)
    # print('Size if the list:',size)
    for i in range(0,len(list),2):
        #print(i,i+1)
        list[i], list[i+1] = list[i+1], list[i]
    return list

size =int(input('Enter the size of the list:'))
list=[]
for i in range(0, size):
    temp=int(input('enter the list element:'))
    list.append(temp)
print('your list has:',list)
print(swap(list))