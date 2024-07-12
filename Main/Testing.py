from MonExp_basic import MonExpNaive
from SOS_binary import MonExp
from CIOS_binary import MonExpCIOS
from random import getrandbits
import time

# generating random a, e and n (binary)
def random_bits(bits):
    n = getrandbits(bits)
    while n % 2 == 0 or n == 0:
        n = getrandbits(bits)
    
    a = getrandbits(bits)
    while a > n:
        a = getrandbits(bits)

    e = getrandbits(bits)
    
    return a, e, n


# funkcja do testowania czasu wykonywania danych algorytmow dla roznej ilosci bitow
def testing(bits, times):

    # srednie czasy wykonania
    MonExp_avg = 0
    SOS_avg = 0
    CIOS_avg = 0

    # petla liczaca sredni czas dla zadanej ilosc powtorzen
    for i in range(times):
        print(f'Loop {i+1}/{times}')
        a, e, n = random_bits(bits)

        # czas dla zwyklego monexp
        start_time = time.time()
        MonExpNaive(a,e,n)
        stop_time = time.time()
        exec_time = (stop_time - start_time)*1000

        MonExp_avg += exec_time

        print(f'MonExp:   {str(exec_time)[:6]} milisekund(y)')


        # czas dla sos
        start_time = time.time()
        MonExp(a,e,n)
        stop_time = time.time()
        exec_time = (stop_time - start_time)*1000

        SOS_avg += exec_time

        print(f'SOS:   {str(exec_time)[:6]} milisekund(y)')


        # czas dla fios
        start_time = time.time()
        MonExpCIOS(a,e,n)
        stop_time = time.time()
        exec_time = (stop_time - start_time)*1000 

        CIOS_avg += exec_time

        print(f'CIOS:   {str(exec_time)[:6]} milisecond(y)\n')
    

    # wypisanie sredniego czasu
    print('\n\n\n ----- SREDNI CZAS -----')
    print('sredni czas zwyklego MonExp: ', str(MonExp_avg / times)[:6], ' miliseconds')
    print('sredni czas SOS: ', str(SOS_avg / times)[:6], ' miliseconds')
    print('sredni czas CIOS: ', str(CIOS_avg / times)[:6], ' miliseconds')
    
    return 0