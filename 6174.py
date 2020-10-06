def ordenarA(n):
    n = str(n)
    i = 0
    j = 0
    n = list(n)
    aux = int(n[0])
    m = ""
    xd = len(n)
    while i < xd:
        aux = int(n[0])
        j = 0
        while j < len(n):
            if (int(n[j]) < aux):
                aux = int(n[j])
            j+=1
        n.pop(n.index(str(aux)))
        i+=1
        m += str(aux)
    return m
def ordenarB(n):
    n = str(n)
    i = 0
    j = 0
    n = list(n)
    aux = int(n[0])
    m = ""
    xd = len(n)
    while i < xd:
        aux = int(n[0])
        j = 0
        while j < len(n):
            if int(n[j]) > aux:
                aux = int(n[j])
            j+=1
        n.pop(n.index(str(aux)))
        i+=1
        m += str(aux)
    return m

def comprobar(x):
    x = int(x)
    if x == 82962 or x == 61974 or x == 63954 or x == 75933:
        return True
    return False
while True:
    x = input("Ingresa: ")
    i = 0
    while i > -1:
        #print(ordenarB(x) + "-" + ordenarA(x))
        x = str(int(ordenarB(x)) - int(ordenarA(x)))
        print(x)
        if int(x) == 6174 or int(x) == 495 or comprobar(x):
            i=-2
        i+=1

        
