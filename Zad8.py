# Zadanie 8

# A.
def wyswietl(*args):
    for x in args:
        print(x)

wyswietl(1, 5, "tekst", 3.14)

# B.
def maksimum(*args):
    if not args:
        return None
    return max(args)

print("Maksimum:", maksimum(4, 9, 2, 15, 3))
