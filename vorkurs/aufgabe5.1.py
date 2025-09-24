import time

def eingabe() -> list:
    zahlen = []
    while len(zahlen) < 3:
        zahl = int(input("gib mir eine zahl... "))
        zahlen.append(zahl)
        
    return zahlen

def getMinMax(zahlen: list):
    return min(zahlen), max(zahlen)

def main():
    zahlen = eingabe()
    
    start = time.time()

    min, max = getMinMax(zahlen)
    print(f"min: {min}")
    print(f"max: {max}")
    
    end = time.time()
    print(end - start)



if __name__ == "__main__":
    main()