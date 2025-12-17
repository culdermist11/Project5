# Zadanie 7

def potega(a, n):
    if n == 0:
        return 1
    return a * potega(a, n - 1)


a = int(input("Podaj liczbę a: "))
n = int(input("Podaj potęgę n: "))

print("Wynik:", potega(a, n))
