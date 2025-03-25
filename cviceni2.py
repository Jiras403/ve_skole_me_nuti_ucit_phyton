import random

# Tento kód zůstává jak je
zvirata = [
    "kočka", "pes", "slon", "žirafa", "lev", "tygr", "sova",
    "tučňák", "ježek", "králík", "myš", "medvěd", "vlk", "liška",
    "klokan", "chameleon", "opice", "panda", "lenochod", "velbloud"
]

nahodne_zvire = random.choice(zvirata)
print(f'Náhodné zvíře: {nahodne_zvire}')

# Po dokončení programu se zeptáme, zda chce uživatel celý program opakovat
opakovani = input("Chcete celý program zopakovat? (ano/ne): ").lower()

if opakovani == "ano":
    # Pznovuzapnuti programu
    exec(open(__file__).read())
else:
    # konecc
    print("Program byl ukončen.")
