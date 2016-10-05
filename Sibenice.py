# coding=UTF-8
# uloha - sibenice
# pri mozne nefunkcnosti zkuste obrátit lomítka
import random


def vyberslovo():
    #Funkce importuje soubor kde jsou slova a vyhodí jedno které pseudonáhodně returnuje
    cesta = str(input('Insert PATH to words:'))
    with open(cesta) as file:
        slova = file.read().splitlines()
    y = random.randrange(0, len(slova)-1, 1)
    return slova_crash[cry]


def hadej(word, uhodl):
    hadal = []
    pokusy = 7
    while not uhodl:
        uhodl = True
        for x in word:
            #Tisknuti uhodlych a neuhodlych pismen
            if x in hadal:
                print(x, end=" ")
            else:
                print("_", end=" ")
                uhodl = False
        if not uhodl:
            print(" Ještě " + str(pokusy) + " Možných chyb")
            #Hadani pokud jeste neuhodl
            vstup = input("\nHadej pismeno:")
            if len(vstup) == 1:
                hadal.append(vstup)
                if vstup not in word:
                    pokusy -= 1
                    sibenice(pokusy)
            else:
                print("Špatný vstup")
                pokusy -= 1
        if pokusy == 0:
            break
    #Zakonceni hry
    if pokusy == 0:
        print("\nSmůla, už visíš")
    elif uhodl:
        print("\nGratulace, zachránil sis hlavu!")
        if input("chceš hrát znovu? (y/n)") == "y":
            main()


def sibenice(chyby):
    #dlouhý kód ale funkční na tisknutí šibenice jako obrázku
    if chyby == 0:
        print("   __________  ")
        print("   | |     |  ")
        print("   | |     O  ")
        print("   | |    /I\ ")
        print("   | |     I  ")
        print("   | |    / \ ")
        print("  .---.       ")
        print(" /     \      ")
    if chyby == 1:
        print("   __________  ")
        print("   | |     I  ")
        print("   | |     O  ")
        print("   | |    /I\ ")
        print("   | |     I  ")
        print("   | |        ")
        print("  .---.       ")
        print(" /     \      ")
    if chyby == 2:
        print("   __________  ")
        print("   | |     I  ")
        print("   | |     O  ")
        print("   | |    /I\ ")
        print("   | |        ")
        print("   | |        ")
        print("  .---.       ")
        print(" /     \      ")
    if chyby == 3:
        print("   __________  ")
        print("   | |     I  ")
        print("   | |     O  ")
        print("   | |        ")
        print("   | |        ")
        print("   | |        ")
        print("  .---.       ")
        print(" /     \      ")
    if chyby == 4:
        print("   __________  ")
        print("   | |        ")
        print("   | |        ")
        print("   | |        ")
        print("   | |        ")
        print("   | |        ")
        print("  .---.       ")
        print(" /     \      ")
    if chyby == 5:
        print("              ")
        print("   | |        ")
        print("   | |        ")
        print("   | |        ")
        print("   | |        ")
        print("   | |        ")
        print("  .---.       ")
        print(" /     \      ")
    if chyby == 6:
        print("              ")
        print("              ")
        print("              ")
        print("              ")
        print("              ")
        print("              ")
        print("  .---.       ")
        print(" /     \      ")


def main():
    #funce main, jen pro jednoduché volání funkcí
    slovo = vyberslovo()
    hadej(slovo, False)

main()
