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


def PropagateCarry(t, start, c):
    for i in range(start,len(t),1):
        sum,c = addc(int(t[-1-i]),0,int(c))
        t[-1-i] = sum
        if c == 0:
            break
    return t


def MonExp(a,e,n): # a^e mod n
    # ap = (a * r) % n
    # up = (1 * r) % n
    # print(ap,up)
    print(sos(3,3,n))

def addc(a,b,c=0):
    ab = a+b+c

    if ab >= 2:
        c = 1 
        ab = ab%2
    else:
        c = 0

    return c,ab


# def PropagateCarry(t, start, c):
#     for i in range(start,len(t),1):
#         sum,c = addc(int(t[-1-i]),0,int(c))
#         t[-1-i] = sum
#         if c == 0:
#             break
#     return t
def propagate_carry(bits, start, carry):
    i = start
    while carry > 0 and i < len(bits):
        carry, bits[-1-i] = addc(bits[-1-i], carry, 0)
        i += 1
    return bits





def sos(ap,bp,n, w=1):
    k, r, np = PrepareMontgomery(n)
    np = bin(np)[2:]
    n_bin = bin(n)[2:]
    #convert a and b to binary
    a_bin = bin(ap)[2:]
    b_bin = bin(bp)[2:]
    s = max(len(a_bin), len(b_bin))
    print(a_bin,b_bin)
    #make sure that they are both exact length
    a_bin = a_bin.zfill(s)
    b_bin = b_bin.zfill(s)
    print(a_bin,b_bin)

    #initialize t to 0
    t = [0]*(2*s+1)
    u=t.copy()
    #Step 1. Compute t = a*b

    for i in range(s):
        carry =  0
        for j in range (s):
            print(t[-1-(i+j)],a_bin[-1-j],b_bin[-1-i],carry)
            carry,sum = addc(int(t[-1-(i+j)]) , int(a_bin[-1-j])*int(b_bin[-1-i]) ,carry)
            print(t[-1-(i+j)],a_bin[-1-j],b_bin[-1-i],carry,sum)
            t[-1-(i+j)] = sum
        t[-1-(i+s)]=carry
    print(t)
    # Lovely, t is computed correctly and stored as an array of bits
    # now we have to calc u = (t+mn)/r
    # first we take u=t, then we are adding mn to it and then divide by r = 2^sw (our w is 1, because we are doing bit by bit, not word by word)
    

    # Step 2. Compute u = (t + mn)/r
    # 2.1 t = t + mn    
    for i in range(s):
        carry = 0
        m = (int(t[-1-i])*int(np[-1])) % (2 ** w)
        for j in range(s):
            print(t[-1-(i+j)],m,n_bin[-1-j],carry)
            carry,sum = addc(int(t[-1-(i+j)]),int(m)*int(n_bin[-1-j]),carry)
            t[-1-(i+j)] = sum
        # PropagateCarry(t,i+s,carry) # this does not work ;/// I do not know how to propagate carry correctly
            # t = propagate_carry(t, 1+i+j, carry)
        t = propagate_carry(t, i+s, carry)
        
    print(t)

    # u = t.copy() # We have to make a deep copy, so modifiyig u does not change t

    # 2.2 u = u/r , so we just ignore lower s words of t

    for j in range(s+1):
        u[-1-j] = t[-1-(j+s)]
    # u >> s
    print(u)
        
    # Step 3. The multi-precision subtraction in Step 3 of MonPro is then performed to reduce u if necessary
    # But I still do not know how to do it correctly
    # TODO: Till now it is good (at least for 3^11 mod 13)

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
    MonExp(8,11,13)