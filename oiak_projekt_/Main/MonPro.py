# mnozenie montgomery'ego
def MonProNaive(ap, bp, n, r, np):
    t = ap * bp # obliczenie t
    #print ('t = ',t,' = ',ap,' * ',bp)

    m = t * np % r # obliczenie m
    #print('m = ',m,' = ', t,' * ',np,' % ',r)

    u = (t + m * n) // r # obliczenie u
    #print('u = ',u,' = ',t,' + ', m,' * ',n,' // ',r)

    # sprawdzenie czy u >=n
    if u >= n:
        #print('t: ',t,'m: ',m,'u: ',u,'n: ',n,'ap: ',ap,'bp: ',bp)
        return u - n
    
    #print('t: ',t,'m: ',m,'u: ',u,'n: ',n,'ap: ',ap,'bp: ',bp)
    return u

