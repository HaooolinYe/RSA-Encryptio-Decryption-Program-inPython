def quotient(a,d):
    r = a % d
    q = a//d
    return q,r

#question 1
def gcd(a,b):
    if not b:
        return a
    else:
        q,r = quotient(a,b)
        g = gcd(b,r)
    return g

#question 2
def euclidean(a,b):
    q,r = quotient(a,b)
    if not r: #if r == 0, we find the gcd which is b
        return (b,r,1)
    else:
        d1,s1,t1 = euclidean(b,r)
        d = d1
        s = t1
        t = s1-t1*q
        return (d,s,t)

#question 3
def euclidean_full(a,b):
    q,r = quotient(a,b)
    if r: # using r == o to determine if we have found the gcd
        print("",a," = " + str(q) +"(" + str(b) + ") +", r,"")
        d,s,t = euclidean_full(b,r) # using euclidean algorithm to find gcd
        if not b + d*t: # if this is equal to 0, this means we just go back
            s1 = 1 # s1 is always 1 when we just go back
            t1 = -q # move t*b to the other side, so t1 = -q
            print("",d,"= " + str(s1) + "(" +str(a)+ ") + " + str(t1) + "(" + str(b) + ")" ) 
            return (d, s1, t1)
        else:
            s1 = t # the s1 of a in this run == t of b from the last run
            t1 = s - t*q # add two 'b's together and t1 is the new coefficient of b
            print("",d,"= " + str(s) + "(" +str(b)+ ") + " + str(t) + "(" + str(a) + str(-q) + "(" + str(b) + ")) =" + str(s1) + "(" + str(a) +") + " + str(t1) + "(" + str(b) + ")")
            return (d, s1, t1)
    else:# if the gcd of a&b is found, go back
        print("",a," = " + str(q) +"(" + str(b) + ") +", r,"")
        print("Now we go back!")
        return (b,1,-q) # return b which is the gcd(a,b), 1 which is always the s for "a" in this run, and -q for t

print(" Hello there. \n Enter 1 to find the gcd of a and b \n Enter 2 to find the gcd of a and b as a linear combination and a and b \n Enter 3 will give you all the steps of the Euclidean algorithm on two integers a and b \n Enter 4 is to find the inverse of an integer modulo n \n Enter 0 to quit the program")
while True:
    x = int(input("You could tell me your option by entering 1,2,3,4 or 0."))
    if not x: #quit
        break
    elif x == 1: # method 1
        a = int(input("You want your a to be ... ...?"))
        b = int(input("You want your b to be ... ...?"))
        d = gcd(a,b)
        print("The gcd of",a,"and",b," is",d,".")
    elif x == 2: # method 2
        a = int(input("You want your a to be ... ...?"))
        b = int(input("You want your b to be ... ...?"))
        d,s,t = euclidean(a,b)
        print( str(d)+" = "+str(s)+"("+str(a)+") + "+str(t)+"("+str(b)+")" )
    elif x == 3: # method 3
        a = int(input("You want your a to be ... ...?"))
        b = int(input("You want your b to be ... ...?"))
        euclidean_full(a,b)
    elif x == 4: # method 4
        a = int(input("You want your a to be ... ...?"))
        n = int(input("You want your n to be ... ...?"))
        d,s,t = euclidean(a,n)
        print("The inverse of",a,"modulo",n,"is",s,".")
    else: # just in case if the user entered something else
        print("Please enter one of the integer among 1,2,3,4 and 0 as your option.")
print("Bye.")