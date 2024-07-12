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

# CIOS ALGORITHM
def cios(a,b,n,r,k, np):
    print('We are in "cios" function')

    s = max(len(a), len(b))
    w = k//s
    n_0_p = np % (2 ** w)

    t = [0]*(s+2)
    print(t)

    for i in range(s):
        c = 0

        print('\npetla j - wejscie')
        for j in range(s):
            sum, c = addc(int(t[-1-j]), int(a[-1-j]) * int(b[-1-i]), int(c))
            print(sum, c)
            t[-1-j] = sum
            print(t)
        print('petla j - wyjscie\n')

        sum, c = addc(int(t[-1-s]), int(c))
        print(sum, c)
        t[-1-s] = sum
        t[-1-(s+1)] = c
        print(t)

        np_arr = list(map(int,str(np)))
        n_arr = list(map(int,str(n)))
        u = t
        
        c = 0
        m = int(t[-1-0]) * np_arr[0] % (2 ** 4)
        print(t[0], m)
        sum, c = addc(int(t[-1-0]), int(np_arr[0]))

        for j in range(s):
            print(t[-1-j], m, n_arr[-1-j])
            sum, c = addc(int(t[-1-j]), int(m) * int(n_arr[-1-j]), int(c))
            t[-1-(j)] = sum

        print(sum, c)
        sum, c = addc(int(t[-1-s]), int(c))
        t[-1-(s-1)] = sum
        t[-1-s] = t[-s] + c
    
        
        for j in range(s+1):
            t[-1-j] = t[-j]
        
        u = int(''.join(map(str,u)))
        u = u // r

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
    k, r, np = PrepareMontgomery(n)
    ap = (a * r) % n
    up = (1 * r) % n
    print('ap:', ap, '   up:', up)
    print('\nWe are now calling "sos" function with followint parameters: 3, 3 and n =', n)
    print(cios('3','3',n, r, k, np))


# CARRY
def PropagateCarry(t, start, c):
    for i in range(start,len(t),1):
        sum,c = addc(int(t[-1-i]),0,int(c))
        t[-1-i] = sum
        if c == 0:
            break
    return t

# MAIN
if __name__ == "__main__":
    MonExp(7,10,13)