# GCD
x, y = 0, 1
def gcdExtended(a, b):
    global x, y
    
    # Base Case
    if (a == 0):
        x = 0
        y = 1
        return b
 
    # To store results of recursive call
    gcd = gcdExtended(b % a, a)
    x1 = x
    y1 = y
 
    # Update x and y using results of recursive
    # call
    x = y1 - (b // a) * x1
    y = x1
 
    return gcd
 

# MOD INVERSE 
def modInverse(A, M):
 
    g = gcdExtended(A, M)
    if (g != 1):
        print("Inverse doesn't exist")
        return 0

    else:
        # m is added to handle negative x
        res = (x % M + M) % M
        return res


# PREPARING VARIABLES
def PrepareMontgomery(n):
    #compute np and r
    #but first we have to compute k, which is number of bits in n
    n_bin = bin(n)[2:] # because we have to trim '0b'
    k = len(n_bin) #simply get the length to know num of bits
    r = 2 ** k # r is 2^k

    r_inv = modInverse(r, n) 
    np = -(1 - r * r_inv) // n # this is the value of np
    return k, r, np


# ADD WITH CARRY
def addc(a,b,c=0):
    c=0
    ab = a+b+c
    ab_arr = list(map(int,str(ab)))
    s = ab_arr[-1]
    if len(ab_arr) > 1:
        c = ab_arr[0]
    return s,c


#  --------------------------------------------------- SOS ALGORITHM ---------------------------------------------------
def sos(a,b,n,r,k, np):
    print('We are in "sos" function')

    s = max(len(a),len(b))
    w = k//s    
    n_0_p = np % (2 ** w)


    t=[0]*(2*s)  # multiplying 2 s-bit numbers results in a 2s-bit number but it is true for bits, not decimals xD
    for i in range(s):
        c = 0
        for j in range(s):
            sum,c = addc(int(t[-1-(i+j)]),int(a[-1-j]) * int(b[-1-i]), int(c))
            t[-1-(i+j)] = sum
        t[-1-(i+s)] = c

#in order to compute u, we first take u = t, and then add m n to it using the standard
# multiplication routine, and finally divide it by r = 25" which is accomplished by ignoring
# the lower s words of u
  
    np_arr = list(map(int,str(np)))
    n_arr = list(map(int,str(n)))

    print(t)
    u = t 
    for i in range(s):
        c = 0
        m = int(t[-1-i]) * np_arr[0] % (2 ** 4)
        print(t[-1-i],m)
        for j in range(s):
            print(t[-1-(i+j)],m,n_arr[-1-j])
            sum, c = addc(int(t[-1-(i+j)]), int(m) * int(n_arr[-1-j]), int(c))
            print(sum,c)
            t[-1-(i+j)] = sum
        PropagateCarry(t, i+s,c)

# The computed value of t is then divided by r which is realized by simply ignoring the lower s words of t
    u = int(''.join(map(str,u)))
    u = u // r

# The multi-precision subtraction in Step 3
# of MonPro is then performed to reduce u if necessary 

    if u >= n:
        return u - n
    return u

    if (b == 0 ):
        return t
    else:
        return u
    
# MON EXP
def MonExp(a,e,n): # a^e mod n
    print('We are in "MonExp" function')

    # Wywołanie funkcji PrepareMontgomery od parametru n
    k, r, np = PrepareMontgomery(n)
    ap = (a * r) % n
    up = (1 * r) % n
    print('ap:', ap, '   up:', up)
    print('\nWe are now calling "sos" function with followint parameters: 3, 3 and n =', n)
    print(sos('3','3',n, r, k, np))
