
"""
New Syllabus
     Pattern-1
        *
        **
        ***
        ****
        *****
"""

size=int(input('enter the size if the pattern: '))

for i in range(0,size):
    for j in range(0,i+1):
        print("*",end=" ")  #end='' means, control remains in the same line
    print()

print()

for i in range(size,0,-1):  #range(start=Initialization, stop=End, increment/decrement=which position to jump in seq)
    for j in range(1,i+1):
        print(j,end=" ")
    print()

print()

ascii_number = 65
for i in range(0,size):
    for j in range(0,i+1):
        ch= chr(ascii_number)
        print(ch,end=" ")
        ascii_number +=1
    print()
    ascii_number = 65