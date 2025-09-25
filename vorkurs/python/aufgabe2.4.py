# Taschenrechner

zahl1 = float(input("gib mir eine zahl\n> "))

operator = input("gib einen rechenoperator ein\nValide sind: +, -, *, /, %\n> ")

zahl2 = float(input("gib noch eine zahl\n> "))


ergebnis = 0.00

match operator:
    case "+":
        ergebnis = zahl1 + zahl2
    case "-":
        ergebnis = zahl1 - zahl2
    case "*":
        ergebnis = zahl1 * zahl2
    case "/":
        ergebnis = zahl1 / zahl2
    case "%":
        ergebnis = zahl1 % zahl2
        
print(f"{zahl1} {operator} {zahl2} = {ergebnis}")

