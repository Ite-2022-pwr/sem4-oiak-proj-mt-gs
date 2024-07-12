# modInverse take from internet
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
####################################################################



def PrepareMontgomery(n):
    #compute np and r
    #but first we have to compute k, which is number of bits in n
    n_bin = bin(n)[2:] # because we have to trim '0b'
    k = len(n_bin) #simply get the length to know num of bits
    r = 2 ** k # r is 2^k

    r_inv = modInverse(r, n) 
    np = -(1 - r * r_inv) // n # this is the value of np
    return k, r, np


def MonExp(a,e,n,w=1): # a^e mod n
    k, r, np = PrepareMontgomery(n)
    s = k // w
    ap = (a * r) % n
    ap = bin(ap)[2:].zfill(s)
    up = (1 * r) % n
    up = bin(up)[2:].zfill(s)
    for i in range(k-1, -1, -1):
        up = FIOS(up, up, n)
        if (e >> i) & 1: # if e_i is 1
            up = FIOS(up, ap, n,)
    tab_1 = [0]*s
    tab_1[-1] = 1
    u = FIOS(up, tab_1, n)
    return u

def addc(a,b,c=0):
    ab = a+b+c

    if ab >= 2:
        c = 1 
        ab = ab%2
    else:
        c = 0

    return c,ab


def propagate_carry(bits, start, carry):
    i = start
    while carry > 0 and i < len(bits):
        carry, bits[-1-i] = addc(bits[-1-i], carry, 0)
        i += 1
    return bits





def FIOS(ap_bin, bp_bin, n, w=1):
    k, _, np = PrepareMontgomery(n)
    np = bin(np)[2:]
    n_bin = bin(n)[2:]

    # Convert a and b to binary
    s = k // w
    print(ap_bin, bp_bin)

    # Initialize t to 0
    t = [0] * (s+3)
    u=t.copy()

    for i in range(s):
        print(t[-1],ap_bin[-1],bp_bin[-1-i])
        carry,sum = addc(int(t[-1]) , int(ap_bin[-1])*int(bp_bin[-1-i]))
        print(t[-1],ap_bin[-1],bp_bin[-1-i],carry,sum)

        t = propagate_carry(t, 1, carry) # ADD(t[1],carry)
        m = (sum*int(np[-1])) % (2 ** w)
        carry,sum = addc(sum, int(m)*int(n_bin[-1]))

        for j in range(1,s,1):
            print(t[-1-j],ap_bin[-1-j],bp_bin[-1-i],carry)
            carry,sum = addc(int(t[-1-j]) , int(ap_bin[-1-j])*int(bp_bin[-1-i]) ,carry)
            print(t[-1-j],ap_bin[-1-j],bp_bin[-1-i],carry,sum)
            t = propagate_carry(t, j+1, carry)
            carry,sum = addc(sum, int(m)*int(n_bin[-1-j]))
            t[-1-(j-1)] = sum
        
        carry,sum = addc(int(t[-1-s]) , carry)
        t[-1-(s-1)] = sum
        t[-1-s], _ = addc(int(t[-1-(s+1)]), carry)
        t[-1-(s+1)] = 0

    
        for j in range(s+1):
            t[-1-j] = t[-1-(j+1)]
            u[-1-j] = t[-1-(j+1)]

    print(t)




    borrow=0
    for i in range (s):
        borrow, diff = subc(u[-1-i],int(n_bin[-1-i]),borrow)
        t[-1-i] = diff
    borrow, diff = subc(u[-1-s],0,borrow)
    t[-1-s] = diff

    if borrow == 0:
        return t
    else:
        return u








def subc(x, y, borrow):
    # Perform subtraction and borrow
    diff = x - y - borrow

    # If diff is negative, set borrow to 1 and add 2 to diff to get a positive result
    if diff < 0:
        borrow = 1
        diff += 2
    else:
        borrow = 0

    return borrow, diff
    






if __name__ == "__main__":
    n = 13
    k, r, np = PrepareMontgomery(n)
    s = k // 1
    ap = 10
    bp = 11
    ap = bin(ap)[2:].zfill(s)
    bp = bin(bp)[2:].zfill(s)
    # print(FIOS(ap,bp,13))
    print(MonExp(11,4,13))