#6.11 Exercises
#Exercises 1
def	b(z):
    prod	=	a(z,	z)
    print(z,	prod)
    return	prod
def	a(x,	y):
    x	=	x	+	1
    return	x	*	y
def	c(x,	y,	z):
    total	=	x	+	y	+	z
    square	=	b(total)**2
    return	square
x	=	1
y	=	x	+	1
print(c(x,	y+3,	x+y))


__main__
X -> x = 1
Y -> y + 3 = x + 1 + 3 = x + 4 = 5
Z -> x + y = 1 + 2 = 3

c()
c(1, 5, 3)
total = 1 + 5 + 3 = 9
square = b(9)**2

b()
b(9)
prob = a(9, 9)

a()
a(9, 9)
x= 9+ 1 = 10
x*y = 9*10= 90
prod = 90


#Exercises 2

def ack(m,n):
    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return ack(m-1,1)
    elif m > 0 and n > 0:
        return ack(m-1,ack(m, n-1))
    else:
        print('The input value is invalid.')

print('ack(0,0): ',ack(0,0))
print('ack(0,1): ',ack(0,1))
print('ack(1,0):',ack(1,0))
print('ack(2,2): ',ack(2,2))
print('ack(3,4):',ack(3,4))
print('ack(3,5):',ack(3,7))

#Exercises 3
def is_palindrome():
    test_word = input('To enter a word to check for palindrome: ')
    transfered = test_word[::-1]
    if len(test_word) <= 1 :
        return True
    if test_word == transfered:
        return True
    else:
        return False

print(is_palindrome())

#Exercises 4
def is_power(a,b):
    if b == 0:
        return 'Invalid value for b.'
    if b != 0 and a % b ==0:
        return True

print(is_power(a=6,b=0))
'''

#Exercises 5
def gcd(a, b):
    """Finds greatest common divisor for a and b;
    a, b - integers.
    """
    if b == 0:
        return a
    return gcd(b, a % b)

print(gcd(8, 16))
