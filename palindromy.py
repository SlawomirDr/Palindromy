def palindrom(wyraz):

    """
        Analize if word is a palindrome
        First counts if number of letters are odd or even
        then compares first with last letter in 3 letter words
        first two with last two in 5 letters words
        and first three with last three in 7 letters words
    """

    lista_liter = list(wyraz)
    ile_liter = len(lista_liter)
    if (ile_liter) % 2 == 0:
        print("To nie jest palindrom")
        
    else:
        if (ile_liter) <= 4:
           wynik = (bool(lista_liter[0]==lista_liter[-1])) 
           if wynik == True:
              print("To jest palindrom")
        elif 4 <= (ile_liter) <=6:
            wynik = (bool(lista_liter[0]==lista_liter[-1]))  
            wynik2 = (bool(lista_liter[1]==lista_liter[-2]))
            if wynik == True and wynik2 == True:
              print("To jest palindrom")
        elif 6 <= (ile_liter) <=8:
            wynik = (bool(lista_liter[0]==lista_liter[-1]))  
            wynik2 = (bool(lista_liter[1]==lista_liter[-2]))
            wynik2 = (bool(lista_liter[2]==lista_liter[-3]))
            if wynik == True and wynik2 == True:
              print("To jest palindrom")
        else:
           print("To nie jest palindrom")

    
    



