import csv

def get_books(imya_faila):
    with open(imya_faila) as f:
        return list(csv.reader(f, delimiter='|'))

def filtered_books(vse_knigi, zapros):
    zapros_dlya_poiska = zapros.lower()
    return list(filter(
        lambda stroka: zapros_dlya_poiska in stroka[1].lower(),vse_knigi))

def calculate_total_value(vse_knigi):
    return list(map(
        lambda stroka: (stroka[0], float(stroka[3]) * float(stroka[4])),vse_knigi))

polychit_vse_knigi = get_books("book.csv")
knigi_po_pithony = filtered_books(polychit_vse_knigi, "python")
itog = calculate_total_value(knigi_po_pithony)

print(itog)