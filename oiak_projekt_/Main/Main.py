import MonExp_basic
import SOS_binary
import CIOS_binary
import NumberGenerator
from Testing import testing
import os

# menu
def main():
    while True:
        print("\nmenu:")
        print("1. stworz plik z wygenerowanymi liczbami")
        print("2. wywolaj funkcje podstawowa MonExp")
        print("3. wywolaj funkcje SOS")
        print("4. wywolaj funkcje CIOS")
        print("5. testowanie")
        print("6. zamknij program")
        
        choice = input("wybierz opcje: ")

        if choice == "1":
            filename = input("podaj nazwe pliku do zapisu: ")
            try:
                with open(filename, 'w') as file:
                    a, e, n = NumberGenerator.GenerateNumbers()
                    file.write(f"{a}\n{e}\n{n}\n")
                print("wygenerowane liczby zostaly zapisane do pliku", filename)
            except FileNotFoundError:
                print("blad: podany plik nie istnieje")
        
        elif choice == "2":
            print("\nmenu - podstawowe MonExp:")
            print("1. wczytaj dane z pliku")
            print("2. wprowadz dane z klawiatury")
            sub_choice = input("wybierz opcje: ")
            
            if sub_choice == "1":
                filename = input("podaj nazwe pliku w biezacym katalogu: ")
                filepath = os.path.join(os.path.dirname(__file__), filename)
                try:
                    with open(filepath, 'r') as file:
                        print("\n")
                        data = file.readlines()
                        if len(data) != 3:
                            print("blad - plik musi zawierac dokladnie trzy linie")
                            continue
                        a, e, n = map(int, map(str.strip, data))
                        result = MonExp_basic.MonExpNaive(a, e, n)
                        print("\nwynik funkcji podstawowej MonExp:", result)
                except FileNotFoundError:
                    print("plik nie istnieje")
                except ValueError:
                    print("blad danych w pliku")
            elif sub_choice == "2":
                a = int(input("podaj a: "))
                e = int(input("podaj e: "))
                n = int(input("podaj n: "))
                result = MonExp_basic.MonExpNaive(a, e, n)
                print("wynik funkcji podstwowej MonExp:", result)
            else:
                print("nieprawidlowy wybor opcji - sprobuj ponownie")

        elif choice == "3":
            print("\nmenu - SOS:")
            print("1. wczytaj dane z pliku")
            print("2. wprowadz dane z klawiatury")
            sub_choice = input("wybierz opcje: ")
            
            if sub_choice == "1":
                filename = input("podaj nazwe pliku w biezacym katalogu: ")
                filepath = os.path.join(os.path.dirname(__file__), filename)
                try:
                    with open(filepath, 'r') as file:
                        print("\n")
                        data = file.readlines()
                        if len(data) != 3:
                            print("blad - plik musi zawierac dokladnie trzy linie")
                            continue
                        a, e, n = map(int, map(str.strip, data))
                        result = SOS_binary.MonExp(a, e, n)
                        print("\nwynik funkcji SOS:", result)
                except FileNotFoundError:
                    print("plik nie istnieje")
                except ValueError:
                    print("blad danych w pliku")
            elif sub_choice == "2":
                a = int(input("podaj a: "))
                e = int(input("podaj e: "))
                n = int(input("podaj n: "))
                result = SOS_binary.MonExp(a, e, n)
                print("wynik funkcji SOS:", result)
            else:
                print("nieprawidlowy wybor opcji - sprobuj ponownie")

        elif choice == "4":
            print("\nmenu - CIOS:")
            print("1. wczytaj dane z pliku")
            print("2. wprowadz dane z klawiatury")
            sub_choice = input("wybierz opcje: ")
            
            if sub_choice == "1":
                filename = input("podaj nazwe pliku w biezacym katalogu: ")
                filepath = os.path.join(os.path.dirname(__file__), filename)
                try:
                    with open(filepath, 'r') as file:
                        print("\n")
                        data = file.readlines()
                        if len(data) != 3:
                            print("blad - plik musi zawierac dokladnie trzy linie")
                            continue
                        a, e, n = map(int, map(str.strip, data))
                        result = CIOS_binary.MonExpCIOS(a, e, n)
                        print("\nwynik funkcji CIOS:", result)
                except FileNotFoundError:
                    print("plik nie istnieje")
                except ValueError:
                    print("blad danych w pliku")
            elif sub_choice == "2":
                a = int(input("podaj a: "))
                e = int(input("podaj e: "))
                n = int(input("podaj n: "))
                result = CIOS_binary.MonExpCIOS(a, e, n)
                print("wynik funkcji CIOS:", result)
            else:
                print("nieprawidlowy wybor opcji - sprobuj ponownie")

        elif choice == "5":
            ok = input("podaj ilosc bitow: ")
            ok2 = input("podaj ilosc powtorzen: ")
            os.system('cls' if os.name == 'nt' else 'clear')
            testing(int(ok), int(ok2))

        elif choice == "6":
            print("\nzakonczono program")
            return 0
        
        else:
            print("nieprawidlowy wybor opcji - sprobuj ponownie")

                
#main
if __name__ == "__main__":
    main()
