"""Given two integers x and n, compute 𝑥^n."""

x = input('Enter the value of x: ')
n = input('Enter the value of n: ')

xPowern =pow(int(float(x)),int(float(n)))

print(x,' power ',n,' is:',str(xPowern))

# without using function pow(), we can do like x**n. ** considers as x power n as below
# xPowern =int(float(x))**int(float(n))


