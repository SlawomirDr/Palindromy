def palindrom(wyraz):
    lista_liter = list(wyraz)
    
    wynik = (bool(lista_liter[0]==lista_liter[-1])) 

    if wynik == True:
        print("To jest palindrom")
    else:
        print("To nie jest palindrom")

palindrom("saghj")

