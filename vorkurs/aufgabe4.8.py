import time

start = time.time()

liste = list(range(1, 21))

for id, item in enumerate(liste):
    if item % 3 == 0:
        print(item)
        liste[id] = "*"
        

print(liste)

end = time.time()

print(end - start)