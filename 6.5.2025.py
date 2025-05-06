cisla = [5, 21, 12, 8, 9, 10]
hledane_cislo = int(input("jaky cislo chces najit: "))
nasel = False
for i in range(len(cisla)):
if cisla[i] == hledane_cislo:
print("Našel jsem jeeej", i+1, "!")
nasel = True
break
if not nasel:
print("nic.")
 