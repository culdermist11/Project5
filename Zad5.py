# Zadanie 5

def bmi(waga, wzrost):
    wartosc = waga / (wzrost ** 2)

    if wartosc < 18.5:
        zakres = "niedowaga"
    elif wartosc < 25:
        zakres = "pożądana masa ciała"
    elif wartosc < 30:
        zakres = "nadwaga"
    elif wartosc < 35:
        zakres = "otyłość I stopnia"
    elif wartosc < 40:
        zakres = "otyłość II stopnia"
    else:
        zakres = "otyłość III stopnia"

    return wartosc, zakres


waga = float(input("Podaj wagę (kg): "))
wzrost = float(input("Podaj wzrost (m): "))

bmi_wartosc, kategoria = bmi(waga, wzrost)
print(f"BMI: {bmi_wartosc:.2f} — {kategoria}")
