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

while cetnost_bull < 4:                              # cyklus hádání čísla, běží dokud se neuhodne 
    hadane_cislice = list()
    cow_nahodne_cislice = list()
    cow_hadane_cislice = list()
    cetnost_bull = 0
    cetnost_cow = 0
    hadane_cislo = input(">>>  ")
    pocet_pokusu += 1
    for num in range(4):                             # cyklus pro porovnání jednotlivých cifer
        hadane_cislice.append(hadane_cislo[num])
        if hadane_cislice[num] == nahodne_cislo[num]:
            cetnost_bull += 1
            if cetnost_bull == 4:                    # výstup při uhodnotí čísla
                print(f"""Correct, you´ve guessed the right number\nin {pocet_pokusu} guesses!\n{"-" * 47}""" )
                if pocet_pokusu <= 5:
                    pocet = "amazing"
                elif pocet_pokusu <=10:
                    pocet = "average" 
                else:
                    pocet = "not so good"
                print(f"That´s {pocet}")
                quit()
        else:                                        # tvorba redukovaných seznamů bez čísel trefených na pozici
            cow_nahodne_cislice.append((nahodne_cislo)[num])
            cow_hadane_cislice.append((hadane_cislo)[num])
    for cislo in range(10):                          # cyklus pro četnost trefených čísel mimo pozici
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
    





