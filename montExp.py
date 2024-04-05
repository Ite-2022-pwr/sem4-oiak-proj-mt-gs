# most of the below code is created from:
#https://link-1springer-1com-19pdzi9l600b7.han.bg.pwr.edu.pl/content/pdf/10.1007/978-1-4419-5906-5_38.pdf?pdf=core

 
def modInverse(A, M):
 
    for X in range(1, M):
        if (((A % M) * (X % M)) % M == 1):
            return X
    return -1


# This is a naive way 
def MonProNaive(ap, bp, n, r, np):
    t = ap * bp # we still have to comput np and r
    m = t * np % r
    u = (t + m * n) // r
    if u >= n:
        return u - n
    return u


def MonProBitWise(a, b, n, r, k):
    a = bin(a)[2:] # convert to binary, because we will want to access specific bits
    u = 0
    for i in range(k):
        u = u + int(a[i]) * b
        u = u + bin(u)[2:][0] * n
        u = u >> 1
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
    k, r, np = PrepareMontgomery(n)
    ap = a * r % n # because MonPro uses ab and bp not a and b

    # u = MonProNaive(ap, b, n, r, np)
    u = MonProBitWise(ap, b, n, r, k)
    return u



def MonExp(a,e,n): # a^e mod n
    k, r, np = PrepareMontgomery(n)
    ap = (a * r) % n
    up = (1 * r) % n
    for i in range(k-1, -1, -1):
        up = MonProNaive(up, up, n, r, np)
        if (e >> i) & 1: # if e_i is 1
            up = MonProNaive(up, ap, n, r, np)
    u = MonProNaive(up, 1, n, r, np)
    return u


 
if __name__ == "__main__":
    A =  16 # this is the number for which we want to find the modular inverse
    M = 13  # this is the modulo value
 
    print(modInverse(A, M))
    #Before calling MonExp / MonPro, we have to compute np and r 

    print(MonExp(7, 10, 13)) #
