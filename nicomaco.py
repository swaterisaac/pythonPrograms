n = int(input("Ingrese un número natural n: "))
i = 1
j = 0

if n == 1:
    print("Cubo número ",i,": 1")
    i = 2


while i <= n:
    num = 0
    mostrar = ""
    while j < i:
        suma = (2*(((((i-1)*((i-1)+1))/2)+ 1)+j)) - 1 #formula los primeros n numeros
        mostrar += str(int(suma)) + " + "
        num += suma
        
        j += 1
    mostrar = mostrar.strip(" +")
    print("Cubo número ",i,": ",int(num),"\nSuma: ",mostrar)
    j = 0
    i += 1
