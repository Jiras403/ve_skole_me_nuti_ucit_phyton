# Zeptame se uzivatele, kolik pacientu chce pridat
pocet_pacientu = int(input("Kolik pacientu chcete pridat? "))

# Tento kousek kódu se bude opakovat podle počtu pacientů
for i in range(pocet_pacientu):
    jmeno = input("Zadejte jméno pacienta, kterého chcete přidat: ")
    prijmeni = input("Zadejte příjmení pacienta, kterého chcete přidat: ")
    rok = int(input("Zadejte rok narození pacienta, kterého chcete přidat: "))
    print(f"Pacient {jmeno} {prijmeni} rok narození {rok} byl přidán.")
