"""● Input a list of numbers and test if a number is equal to the sum of the cubes of
its digits. Find the smallest and largest such number from the given list of
numbers."""

list =[153,2,33,121,422,13,16]
smallest=0
largest=0
print('list has:',list)
for i in range(0,len(list)):
    cubesum = 0
    num=list[i]
    print(i,": ",num)
    j=1
    while(j <= len(str(list[i]))):
        if num % 10 != 0:
            #print('num',num)
            temp = num % 10
            #print('temp',temp)
            cubesum = cubesum + temp**3
            #print('cubesum',cubesum)
            num = int( num / 10 )
            #print('num/10',num)
        j+=1

    print('cubesum of',list[i],':',cubesum)

    if list[i] == cubesum:
        if smallest < cubesum:
            smallest = cubesum
        if largest < smallest:
            largest =smallest

print('smallest: ',smallest)
print('largest: ',largest)
