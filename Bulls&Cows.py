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
nahodne_cislo = int(random.randrange(1000,9999,1))

pocet_pokusu = 0
cetnost_bull = 0

print(nahodne_cislo)

while cetnost_bull < 4:
    nahodne_cislice = list()
    hadane_cislice = list()
    cow_nahodne_cislice = list()
    cow_hadane_cislice = list()
    cetnost_bull = 0
    cetnost_cow = 0
    hadane_cislo = input(">>>  ")
    pocet_pokusu += 1
    for num in range(4):
        nahodne_cislice.append(str(nahodne_cislo)[num])
        hadane_cislice.append(str(hadane_cislo)[num])
        if hadane_cislice[num] == nahodne_cislice[num]:
            cetnost_bull += 1
            if cetnost_bull == 4:
                print(f"""Correct, you´ve guessed the right number\nin {pocet_pokusu} guesses!\n{"-" * 47}""" )
        else:
            cow_nahodne_cislice.append(str(nahodne_cislo)[num])
            cow_hadane_cislice.append(str(hadane_cislo)[num])
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
    





