zahl = int(input("gib eine zahl ein\n> "))

for i in range(1, zahl):
    if zahl % i == 0 and zahl != i:
        continue
    print(i)