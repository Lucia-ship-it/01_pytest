from contacts import get_contact
# vyžádá si jméno
name = input("Zadejte jméno: ")
# pokud existuje kontakt s daným jménem -> kontakt vytiskne
result = get_contact(name)
# pokud daný kontakt neexistuje, tak napíše, že neexistuje

if result:
    print(result)
else:
    print("daný uživatel neexistuje")