"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Magdalena Kreckova
email: kreckova.majda@gmail.com
discord: Majda_247
"""

#registrovaní uživatelé - kombinace uživatelských jmen a hesel 
registrovani ={
    "bob" : "123",
    "ann" : "pass123",
    "mike" : "password123",
    "liz" : "pass123"
}

#zadání přihlašovacích údajů - kombinace uživatelského jméne a hesla
uzivatelske_jmeno = input("Zadej uživatelské jméno:")
heslo = input("Zadej heslo:")
print("-"*50)

#kontrola, jestli se přihlásil správný uživatel (tzn. správná kombinace jména a hesla)
if uzivatelske_jmeno in registrovani and registrovani[uzivatelske_jmeno] == heslo:
    print("Vítej", uzivatelske_jmeno, "! Můžeš analyzovat svůj text!")
else:
    print("Nejsi registrovaný!", "Ukončuji program", sep="\n" )
    exit()

#zadané texty
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
long = len(TEXTS)

print(f'{"Můžete analyzovat celkem"} {long} {"texty."}',  "-" * 50, sep="\n")

#vybrání textu k analýze
cislo_text = input(f'{"Zadejte číslo od 1 do"} {long} {":"}')

#výpis vybraného textu
while True:
    if cislo_text.isdigit() and 1 <= int(cislo_text) <= long:
        print("Váš vybraný text je: ", TEXTS[int(cislo_text) - 1], "-" * 50, sep="\n")
        break
    else:
        print(f"Nebyla zadána hodnota od 1 do {long}, zkuste to znovu.")
        cislo_text = input(f"Zadejte číslo od 1 do {long}: ")

#STATISTIKY TEXTU
#rozdělení textu na slova
vsechna_slova = TEXTS[int(cislo_text) - 1].split()
#odstranění speciálních znaků 
slova = []
for slovo in vsechna_slova:
    cista_slova = slovo.strip('.,?!;:_-"')
    slova.append(cista_slova)

pocet_titulnich_slov = 0
pocet_velkych_slov = 0
pocet_malych_slov = 0
pocet_cisel = 0
cislelne_hodnoty = []
delky_slov = []
cetnost_slov = dict ()

for vsechna_slova in slova:
# Slova s velkým počátečním písmenem
  if (vsechna_slova.isupper() == True or vsechna_slova.istitle() == True) and vsechna_slova.isalpha() == True:
    pocet_titulnich_slov += 1
# Jen VELKÁ písmena
  if vsechna_slova.isupper() == True and vsechna_slova.isalpha() == True:
    pocet_velkych_slov += 1
# Pouze malá písmena
  if vsechna_slova.islower() == True and vsechna_slova.isalpha() == True:
    pocet_malych_slov += 1
# Počet číselných stringů v textu a vypsání jejich součtu
  if vsechna_slova.isdigit() == True:
    pocet_cisel += 1
    cislelne_hodnoty.append(int(vsechna_slova))
# délky jednotlivých slov
  delky_slov.append(len(vsechna_slova))

  # souhrn výsledků
print("V textu se nachází", len(slova), "slov")
print("V textu se nachází", pocet_titulnich_slov, "titulních slov")
print("V textu se nachází", pocet_velkych_slov, "slovo/a s velkými písmeny")
print("V textu se nachází", pocet_malych_slov, "slovo/a s malými písmeny")
print("V textu se nachází", pocet_cisel, "čísla")
print("Součet všech čísel je:", sum(cislelne_hodnoty))

#četnost slov
for pocty in delky_slov:
    if pocty not in cetnost_slov:
        cetnost_slov[pocty] = 1
    else:
        cetnost_slov[pocty] += 1

#vytvoření grafu 
print("-" * 50,
      f"{'DÉLKA':<6}|{'ČETNOST GRAF.':<20}|{'ČETNOST':>6}",
      "-" * 50,
      sep = "\n")

for index, (delka, pocet) in enumerate(sorted(cetnost_slov.items()), start = 1):
    print(
        f"{index:<6}|{'*' * int(pocet):<20}|{pocet}",
        sep="\n")
