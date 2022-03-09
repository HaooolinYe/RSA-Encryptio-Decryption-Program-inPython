def ifprime(n):
    '''
        ifprime(n) takes an positive integer and returns
        ture if it is a prime and false if it is not
    '''
    result = True
    for x in range(2,int(n**(1/2))+1):
        if not n%x:
            result = False
            break
    return result 

def quotient(a,d):
    '''quotiend(a,d) gives the floor division result
        and the remainder of a divide d.'''
    r = a % d
    q = a//d
    return (q,r)


def euclidean(a,b):
    '''this is the original function I use to compute
    the s,t satisfy the equation gcd(a,b) = as + bt. What
    this would return is a tuple that looks like (gcd(a,b), s, t)'''
    q,r = quotient(a,b)
    if not r: #if r == 0, we find that the gcd is b
        return (b,r,1)
    else:
        d1,s1,t1 = euclidean(b,r)
        d = d1
        s = t1
        t = s1-t1*q
        return (d,s,t)

# As my professor reminds me that a recursive function won't be efficient enough
# especially when p and q are large primes. Therefore, I uses the following function, xgcd(a,b),
# coded by Robert Campbell from the website: https://github.com/Robert-Campbell-256/Number-Theory-Python/blob/master/numbthy.py

def xgcd(a,b):
    """xgcd(a,b) returns a tuple of form (g,x,y), where g is gcd(a,b) and
    x,y satisfy the equation g = ax + by."""
    a1=1; b1=0; a2=0; b2=1; aneg=1; bneg=1
    if(a < 0):
        a = -a; aneg=-1
    if(b < 0):
        b = -b; bneg=-1
    while (1):
        quot = -(a // b)
        a = a % b
        a1 = a1 + quot*a2; b1 = b1 + quot*b2
        if(a == 0):
            return (b, a2*aneg, b2*bneg)
        quot = -(b // a)
        b = b % a;
        a2 = a2 + quot*a1; b2 = b2 + quot*b1
        if(b == 0):
            return (a, a1*aneg, b1*bneg)
    
def find_inverse(s,t,a,b):
    ''' find_inverse returns the inverse of a modulo b.
        The function makes sure that the a,b satisfy gcd(a,b) = as + bt
        also satisfy s > 0 and t < 0 for the convience of doing RSA.'''
    while s < 0 and t > 0:
        s += b
        t -= a
    return (s,t)
    
def decrypt(n,Q,k):
    '''decrypt(n,Q,k) returns the decryped message which is a number
        that represents a letter/punctuation mark in the letter-to-number table.'''
    (x,s,t) = xgcd(k,Q)
    s,t = find_inverse(s,t,k,Q)
    code = (n**s) % (p*q)
    return str(code)

import string

letters = string.ascii_uppercase
d = {}    # a letter-to-number dictionary that its values are letters and keys are numbers
d_r = {}  # a number-to-letter dictionary
n = 12
table_1 = '' # the table that the user is going to see
table_2 = '' # the second row of the table

for l in letters:
    d[l] = n
    d_r[n] = l
    table_1 = table_1 + l + '   '
    table_2 = table_2 + str(n) + '  ' if n >= 10 else table_2 + str(n) + '   ' # format the table a little bit
    n += 1
    
print("Here is the letter-to-number table")
print(table_1)
print(table_2)

for l in [' ','!',',','.',':',';',"'",'"','?']:
    # add all punctuation marks and space to the letter-to-number table, rather, a dictionary
    d[l] = n
    d_r[n] = l
    n += 1

print("Do you want to be Alice or Bob?\nIf you decide to be Alice, this program would decrypt your code for you.\nIf you want to be Bob, you can encrypt your message.")
# The manual of this program

user = None # make sure the while loop can start running

while user != "quit":
    user = input("You want to be (type 'quit' for exiting the program)... ... ")
    if user == "Alice":
        p, q = None,None
        while True: 
            p = int(input("Pick 2 prime numbers p and q please \n You want p to be...")) # ask her for private key
            q = int(input("You want q to be..."))
            k = int(input("What is k?"))
            _q, _p, _k = ifprime(q), ifprime(p), ifprime(k) # check if "Alice" is using prime numbers
            if _q and _p and _k:
                break # break when all p,q and k are prime
            print("Oops! Please only use prime numbers.")
            f3 = "The composite number is  p: {} q:{} k: {}"
            print(f3.format(not _p, not _q, not _k))  # tell the user which one is a composite number
        m = q*p
        Q = (q-1)*(p-1)
        d1,s,t = xgcd(k,Q)
        s,t = find_inverse(s,t,k,Q)
        f0 = "Your private key is p: {:d}, q: {:d}, the inverse of k mod(phi of m): {:d} and phi of m: {:d}."
        # print the public and private key for the user
        f1 = "The public key is k: {:d} and m: {:d}."
        print(f1.format(k,m))
        print(f0.format(p,q,s,Q))
        code = input("What is the code that you want me to decrypt for you?")
        result = '' # the decrypted message that the user is going to see
        code = code.split(' ')
        message = '' # a string that has all the decrypted numbers
        i = 0
        for word in code:
            if code:
                message += decrypt(int(word),Q,k) # decrypt the code
        n = 2 # all numbers in our table are 2-digit integer, so we look at a len-2 string at a time
        while message: # match the number with alphabet letters
            current_m = message[0:2]
            result += d_r.get(int(current_m))
            message = message[n:]
        f4 = "Here you go. The decrypted message says: '{}'."
        print(f4.format(result))
    elif user == "Bob":
        k = int(input("I need the public key to encrypt your message\n what is k?")) # ask Bob for the public key
        m = int(input("what is m?"))
        Message = (input("What is your message?")).upper() # all letters in our table are uppercase
        message = ['']*len(Message) # make sure every elements in 'message' represents one letter of Message
        i = 0
        for l in Message: # turning the letters to numbers using the letter-to-number dictionary
            message[i] += str(d[l])
            i += 1
        result = []
        for letter in message:
            code = (int(letter)**k) % m # encrypt the message use congruence
            c = str(code)
            result.append(str(code))
        result = ' '.join(result)
        f1 = "The encryped code for your message is '{:s}'."
        print(f1.format(result))
                

print("Have a nice day:)")