zahl = int(input("gib eine zahl ein "))


for i in range(1, 11):
    ergebnis = (i * zahl) / (11 - i)

    print(f"{i} * {zahl} = {ergebnis} * {i}")