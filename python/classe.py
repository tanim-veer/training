notes = {"Tanim": 12, "Marie": 8, "Sofiane": 15, "Lea": 17}
somme = 0

for nom, note in notes.items():
    print(f"{nom} : {note}")
    somme += note

moy = somme / len(notes)
print(f"Moyenne : {moy:.2f}")
