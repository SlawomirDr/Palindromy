def palindrom(wyraz):
    
    lista_liter = list(wyraz)
    ile_liter = len(lista_liter)
    if (ile_liter) % 2 == 0:
        print("To nie jest palindrom1")
            
        
    else:
        wynik = (bool(lista_liter[0]==lista_liter[-1])) 
        if wynik == True:
           print("To jest palindrom")
        else:
           print("To nie jest palindrom2")

    
    

palindrom("kajtr")

