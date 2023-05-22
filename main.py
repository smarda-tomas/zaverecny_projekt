from pojistenci import Pojistenci
import chybove_hlasky


def pridat_noveho_pojistence():
    pojistenec = Pojistenci.pridat_pojistence()
    if isinstance(pojistenec, Pojistenci):
        seznam_pojistencu.append(pojistenec)
    else:
        return


def vypis_pojistencu():
    if len(seznam_pojistencu) == 0:
        print("\nZadny pojistenec neevidován!\n")
        return
    print()
    print("{0:<10} {1:<15} {2:<10} {3:<10}\n".format("Jmeno", "Prijmeni", "Vek", "Telefon"))
    for osoba in seznam_pojistencu:
        print(Pojistenci.__str__(osoba))
    print()


def vyhledat_pojistence():
    print("Zajdete jmeno pojisteneho:")
    jmeno = input().lower()
    print("Zadejte prijmeni:")
    prijmeni = input().lower()
    print()

    for osoba in seznam_pojistencu:
        if osoba.jmeno.lower() == jmeno and osoba.prijmeni.lower() == prijmeni:
            print(Pojistenci.__str__(osoba))
            print()
            return

    chybove_hlasky.pojisteny_nenalezen()


def editace_pojisteneho():
    print("Zajdete telefonni cislo pojisteneho:")
    tel_cislo = input()
    if not tel_cislo.isnumeric():
        chybove_hlasky.neplatna_hodnota()
        return

    for osoba in seznam_pojistencu:
        if osoba.tel_cislo == tel_cislo:
            print("Co si prejete upravit? 1 - Jmeno, 2 - Prijmeni, 3 - Vek, 4 - Telefonni cislo")
            index = input()

            #overeni spravnosti inputu
            if index.isnumeric():
                if int(index) > 4 or int(index) < 0:
                    chybove_hlasky.neplatna_hodnota()
                    return
            else:
                chybove_hlasky.neplatna_hodnota()
                return

            print("Nova hodnota:")
            nova_hodnota = input()
            Pojistenci.editace_pojisteneho(osoba, index, nova_hodnota)
            print("\nZmena ulozena!\n")
            return

    chybove_hlasky.pojisteny_nenalezen()


"""
===============================
PRINTY
===============================
"""


def print_uvod():
    print("--------------------------------")
    print("Evidence pojistených")
    print("--------------------------------")


def print_akce():
    print("Vyberte si akci:")
    print("1 - Pridat nového pojisteného")
    print("2 - Vypsat vsechny pojistené")
    print("3 - Vyhledat pojisteného")
    print("4 - Editovat pojisteného")
    print("5 - Konec")

    return input("Akce: ")


print_uvod()
seznam_pojistencu = []

while True:

    akce = print_akce()

    match akce:
        case "1":
            pridat_noveho_pojistence()
        case "2":
            vypis_pojistencu()
        case "3":
            vyhledat_pojistence()
        case "4":
            editace_pojisteneho()
        case "5":
            print("Aplikace ukoncena")
            break
        case other:
            chybove_hlasky.neplatna_hodnota()
