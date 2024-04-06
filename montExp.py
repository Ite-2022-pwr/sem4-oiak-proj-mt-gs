# most of the below code is created from:
#https://link-1springer-1com-19pdzi9l600b7.han.bg.pwr.edu.pl/content/pdf/10.1007/978-1-4419-5906-5_38.pdf?pdf=core
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
 
 
def modInverse(A, M):
 
    g = gcdExtended(A, M)
    if (g != 1):
        print("Inverse doesn't exist")
        return 0

    else:
 
        # m is added to handle negative x
        res = (x % M + M) % M
        return res



# This is a naive way 
def MonProNaive(ap, bp, n, r, np):
    t = ap * bp # we still have to comput np and r
    print ('t = ',t,' = ',ap,' * ',bp)
    m = t * np % r
    print('m = ',m,' = ', t,' * ',np,' % ',r)
    u = (t + m * n) // r
    print('u = ',u,' = ',t,' + ', m,' * ',n,' // ',r)
    if u >= n:
        print('t: ',t,'m: ',m,'u: ',u,'n: ',n,'ap: ',ap,'bp: ',bp)
        return u - n
    print('t: ',t,'m: ',m,'u: ',u,'n: ',n,'ap: ',ap,'bp: ',bp)
    return u


# def MonProBitWise(a, b, n, k):
#     a = bin(a)[2:] # convert to binary, because we will want to access specific bits
#     u = 0
#     for i in range(k-1):
#         u = u + int(a[i]) * b
#         u = u + int(bin(u)[2:][0]) * n
#         u = u >> 1
#     if u >= n:
#         return u - n
#     return u


# def MonProWordWise(a, b, n, r, s, w = 32): # assume our word is 32 by default
    a = bin(a)[2:] # convert to binary, because we will want to access specific bits
    u = 0
    #calculate -n_0^-1
    n_0 = bin(n)[2:][-w:] # get the last bit // this may actually be wrong XD
    n_0_inv = modInverse(int(n_0, 2), 2 ** w) * (-1) # we have to compute -n_0^-1

    print(s,w)
    for i in range(s-1):
        u = u + int(a[i]) * b
        # we have to calc -n_0^-1
        u = u + n_0_inv * int(bin(u)[2:][0]) * n
        u = u >> w

    if u >= n:
        return u - n
    return u



def PrepareMontgomery(n):
    #compute np and r
    #but first we have to compute k, which is number of bits in n
    n_bin = bin(n)[2:] # because we have to trim '0b'
    k = len(n_bin) #simply get the length to know num of bits
    r = 2 ** k # r is 2^k

    r_inv = modInverse(r, n) 
    np = -(1 - r * r_inv) // n # this is the value of np
    return k, r, np



def MonMul(a, b, n):
    k, r, _= PrepareMontgomery(n)
    ap = a * r % n # because MonPro uses ab and bp not a and b

    # u = MonProNaive(ap, b, n, r, np)
    u = MonProBitWise(ap, b, n,k)
    return u



# def MonExpByWord(a,e,n, w): # a^e mod n
    k, r, np = PrepareMontgomery(n)
    s = k // w
    ap = (a * r) % n
    up = (1 * r) % n
    for i in range(k-1, -1, -1):
        up = MonProWordWise(up, up, n, r, s, w)
        if (e >> i) & 1: # if e_i is 1
            up = MonProWordWise(up, ap, n, r, s, w)
    u = MonProWordWise(up, 1, n, r, s,w)
    return u




def MonExpNaive(a,e,n): # a^e mod n
    k, r, np = PrepareMontgomery(n)
    ap = (a * r) % n
    up = (1 * r) % n
    for i in range(k-1, -1, -1):
        up = MonProNaive(up, up, n, r, np)
        if (e >> i) & 1: # if e_i is 1
            up = MonProNaive(up, ap, n, r, np)
    u = MonProNaive(up, 1, n, r, np)
    return u


# def MonExpBit(a,e,n): # a^e mod n
    k, r, np = PrepareMontgomery(n)
    ap = (a * r) % n
    up = (1 * r) % n
    for i in range(k-1, -1, -1):
        up = MonProBitWise(up, up, n, k)
        if (e >> i) & 1: # if e_i is 1
            up = MonProBitWise(up, ap, n,k)
    u = MonProBitWise(up, 1, n, k)
    return uws


 
if __name__ == "__main__":
    print(MonExpNaive(8, 11, 13)) # 7^10 mod 13 = 4
