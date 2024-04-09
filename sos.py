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


def addc(a,b,c=0):
    c=0
    ab = a+b+c
    ab_arr = list(map(int,str(ab)))
    s = ab_arr[-1]
    if len(ab_arr) > 1:
        c = ab_arr[0]
    # print (s,c)
    return s,c


def sos(a,b,n):
    ## Not quite sure If i will need this.
    n_bin = bin(n)[2:] # because we have to trim '0b'
    k = len(n_bin) #simply get the length to know num of bits
    
    r = 2 ** k # r is 2^k
    #########################################################

    r_inv = modInverse(r, n) 

    s = max(len(a),len(b))
    w = k//s    
    np = -(1 - r * r_inv) // n # this is the value of np
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
    n_arr = list(map(int,str(n)))# But after this point sometihng fcks up :) 


# till now it looks good :) 
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
    # print('t+mn',t)
    # for j in range(s):
    #     print(u[-1-j],t[-1-(j+s)],(j+s))
    #     u[-1-j] = t[-1-(j+s)]  
    #     #TODO : this is only temp, I gues we are just shiftin it to the right, but I am not quite sure yet
    #     t[-1-(j+s)]=0

# The multi-precision subtraction in Step 3
# of MonPro is then performed to reduce u if necessary 


    if u >= n:
        return u - n
    return u
    # b = 0
    # for i in range(s):
    #     print (u[-1-i],n_arr[-1-i],b)
    #     b, d = subc(int(u[-1-i]), int(n_arr[-1-i]), int(b))
    #     t[-1-i] = d
    #     if (b == 1):
    #         t[-2-i] -= 1

    # b, d = subc(int(u[-1-s]), b, 0)
    # t[-1-s] = d

    if (b == 0 ):
        return t
    else:
        return u



def subc(a,b,borrow=0):
    borrow=0
    ab = a-b-borrow
    if (ab < 0):
        borrow = 1
    return borrow, abs(ab)
    
def MonExp(a,e,n): # a^e mod n
    k, r, np = PrepareMontgomery(n)
    ap = (a * r) % n
    up = (1 * r) % n
    print(ap,up)
    print(sos('3','3',n))

def PrepareMontgomery(n):
    #compute np and r
    #but first we have to compute k, which is number of bits in n
    n_bin = bin(n)[2:] # because we have to trim '0b'
    k = len(n_bin) #simply get the length to know num of bits
    r = 2 ** k # r is 2^k

    r_inv = modInverse(r, n) 
    np = -(1 - r * r_inv) // n # this is the value of np
    return k, r, np


def PropagateCarry(t, start, c):
    for i in range(start,len(t),1):
        sum,c = addc(int(t[-1-i]),0,int(c))
        t[-1-i] = sum
        if c == 0:
            break
    return t

if __name__ == "__main__":
    MonExp(7,10,13)