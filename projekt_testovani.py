import sys

ukoly = []


def hlavni_menu():
    while True:  # Hlavní menu se opakuje, dokud uživatel neukončí program
        print("\nSprávce úkolů - Hlavní menu")
        print("1: Přidat úkol")
        print("2: Zobrazit úkoly")
        print("3: Odstranit úkoly")
        print("4: Konec programu")
        volba_fce = input("Zvolte možnost 1 až 4: ")

        if volba_fce.isdigit() and 1 <= int(volba_fce) <= 4:
            volba = int(volba_fce)

            if volba == 1:
                pridat_ukol()
            elif volba == 2:
                zobraz_ukol()
            elif volba == 3:
                odstran_ukol()
            elif volba == 4:
                konec_programu()
                
        else:
            print("Zadejte platné číslo od 1 do 4.")


def pridat_ukol():
    nazev = input("Zadej název úkolu: ").strip()
    if not nazev:
        print("Název nesmí být prázdný.")
        return  # Vrátí se zpět do hlavního menu

    popis = input("Zadej popis úkolu: ").strip()
    if not popis:
        print("Popis nesmí být prázdný.")
        return
    cislo_ukolu = len(ukoly) + 1  # Určení čísla úkolu
    ukoly.append({"číslo": cislo_ukolu, "název": nazev, "popis": popis})
    print("Úkol byl úspěšně přidán!")


def zobraz_ukol():
    if len(ukoly) == 0:
        print("Žádný úkol nebyl vložen")
    else:
        for ukol in ukoly:
            print(f"Číslo: {ukol['číslo']}, Název: {ukol['název']}, Popis: {ukol['popis']}")

def odstran_ukol():
    print(ukoly)
    klic = int(input("Zvolte úkol k odstranění "))
    for x in range(len(ukoly)):
        if ukoly[x]["číslo"] == klic:
            del ukoly[x]
            break
    print(ukoly)
def konec_programu():
    sys.exit()
    


hlavni_menu()
