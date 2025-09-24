"""
Schreiben Sie ein Programm, das so lange Texteingaben vom Benutzer entgegennimmt, bis der Benutzer
die Eingabe „stopp“ tätigt. Geben Sie dem Benutzer aus, wie viele Texteingaben betätigt wurden und
welche das waren.
"""

user_inputs = []

while True:
    user_input = input("write something... ")
    
    if user_input == "stopp":
        print(len(user_inputs))
        print(user_inputs)
        break
    
    user_inputs.append(user_input)
    