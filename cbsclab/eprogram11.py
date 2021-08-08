"""Input a string and determine whether it is a palindrome or not;
convert the case of characters in a string."""

"""
It means, "start at the end; count down to the beginning, stepping backwards one step at a time."

    The slice notation has three parts: start, stop, step:
    >>> 'abcdefghijklm'[2:10:3]  # start at 2, go upto 10, count by 3
        'cfi'
    >>> 'abcdefghijklm'[10:2:-1] # start at 10, go downto 2, count down by 1
        'kjihgfed'
        If the start and stop aren't specified, it means to go through the entire sequence:

    >>> 'abcdefghijklm'[::3]  # beginning to end, counting by 3
        'adgjm'
    >>> 'abcdefghijklm'[::-3] # end to beginning, counting down by 3
        'mjgda'
"""

str= input('Enter the string:')
revStr=str[::-1]    #To know how [::-1] works, check above example
if str == revStr:
    print(str,' is a palindrome')
else:
    print(str, ' is not a palindrome')

print(str,'swap to',str.swapcase())