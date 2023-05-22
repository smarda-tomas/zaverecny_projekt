import chybove_hlasky


class Pojistenci:

    def __init__(self, jmeno, prijmeni, vek, tel_cislo):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.tel_cislo = tel_cislo

    def pridat_pojistence():
        print("Zadejte jméno pojistejného:")
        jmeno = input()

        print("Zadejte prijmeni:")
        prijmeni = input()

        print("Zadejte telefonni cislo:")
        tel_cislo = input()
        if tel_cislo.isnumeric():

            print("Zadejte vek:")
            vek = input()
            if vek.isnumeric():

                print("\nData byla ulozena!\n")

                novy_pojistenec = Pojistenci(jmeno, prijmeni, vek, tel_cislo)

                return novy_pojistenec
            else:
                chybove_hlasky.neplatna_hodnota()
                return
        else:
            chybove_hlasky.neplatna_hodnota()
            return

    def __str__(self):
        return "{0:<10} {1:<15} {2:<10} {3:<10}".format(self.jmeno, self.prijmeni, self.vek, self.tel_cislo)

    def editace_pojisteneho(self, index, nova_hodnota):
        match index:
            case "1":
                self.jmeno = nova_hodnota
            case "2":
                self.prijmeni = nova_hodnota
            case "3":
                self.vek = nova_hodnota
            case "4":
                self.tel_cislo = nova_hodnota
            case "other":
                chybove_hlasky.neplatna_hodnota()
