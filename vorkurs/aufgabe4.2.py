"""
Erzeugen Sie eine Liste von 1 bis 15. Gehen Sie die Liste anschließend iterativ durch, und geben Sie jede
dritte Zahl aus.
"""

list = (range(1, 16))

print(list)

for i in list:
    if i % 3 ==0:
        print(i)