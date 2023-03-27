"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Martin Brejcha
email: brmast@seznam.cz
discord: Martin B.#5188
"""

print(f"""
Hi there !
{"-" * 47}
I´ve generated a random 4 digit number for you.
Let´s play a bulls and cow game.
{"-" * 47}
Enter a number:
{"-" * 47}""")

import random
nahodne_cislo = list()
nahodne_cislo.append(str(random.randrange(1,9,1)))
while len(nahodne_cislo) < 4:
    nahodna_cifra = str(random.randrange(0,9,1))
    if nahodna_cifra not in nahodne_cislo:
        nahodne_cislo.append(nahodna_cifra)

pocet_pokusu = 0
cetnost_bull = 0
# cyklus hádání čísla, běží dokud se neuhodne 
while cetnost_bull < 4:                                     
    hadane_cislice = list()
    cow_nahodne_cislice = list()
    cow_hadane_cislice = list()
    cetnost_bull = 0
    cetnost_cow = 0
    hadane_cislo = input(">>>  ")
    # ověření vstupu, zda je číslo požadovaného formátu
    while hadane_cislo[0] == "0" or not hadane_cislo.isnumeric() or len(hadane_cislo) != 4: 
        print("error, you can only enter a four-digit number\nthat does not start with zero")
        hadane_cislo = input(">>>  ")
    pocet_pokusu += 1
    # cyklus pro porovnání jednotlivých cifer
    for num in range(4):                                    
        hadane_cislice.append(hadane_cislo[num])
        # výstup při uhodnotí čísla
        if hadane_cislice[num] == nahodne_cislo[num]:
            cetnost_bull += 1
            if cetnost_bull == 4:                           
                print(f"""Correct, you´ve guessed the right number\nin {pocet_pokusu} guesses!\n{"-" * 47}""" )
                if pocet_pokusu <= 5:
                    pocet = "amazing"
                elif pocet_pokusu <=10:
                    pocet = "average" 
                else:
                    pocet = "not so good"
                print(f"That´s {pocet}")
                quit()
        # tvorba redukovaných seznamů bez čísel uhodnutých na pozici
        else:                                           
            cow_nahodne_cislice.append((nahodne_cislo)[num])
            cow_hadane_cislice.append((hadane_cislo)[num])
    # cyklus pro četnost uhodnutých čísel mimo pozici
    for cislo in range(10):                                
        cetnost_cow = cetnost_cow + min(cow_nahodne_cislice.count(str(cislo)),cow_hadane_cislice.count(str(cislo)))
    if cetnost_bull == 1:
        bull = " bull"
    else: 
        bull = " bulls"
    if cetnost_cow == 1:
        cow = " cow"
    else: 
        cow = " cows"
    print(f"""{cetnost_bull}{bull}, {cetnost_cow}{cow}\n{"-" * 47}""")
    