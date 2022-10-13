def demande():
    while True:
        try:
            N = int(input("Veuillez saisir un nombre:  "))

        except:
            print("erreur entre un nombre : ")
            return demande()
        return N

nombre  = demande()
for i in range(nombre+1,nombre+11):
    print(i,end=" ")