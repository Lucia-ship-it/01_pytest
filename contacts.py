# Globální seznam kontaktů
contacts = [{"name": "Engeto", "phone": "777777777"}]


def add_contact(name: str, phone: str):
    """
    Přidá nový kontakt do seznamu kontaktů.

    Args:
        name (str): Jméno kontaktu.
        phone (str): Telefonní číslo kontaktu. Musí obsahovat alespoň 6 číslic a žádné jiné znaky.

    Returns:
        None

    Raises:
        ValueError: Pokud jméno nebo telefonní číslo není zadáno, nebo číslo není validní.
        KeyError: Pokud kontakt se stejným jménem již existuje.
    """
    if not name or not phone:
        raise ValueError("Jméno i telefon musí být vyplněny.")

    if not phone.isdigit() or len(phone) < 6:
        raise ValueError("Telefonní číslo musí obsahovat alespoň 6 číslic.")

    for contact in contacts:
        if contact["name"] == name:
            raise KeyError(f"Kontakt se jménem '{name}' už existuje.")

    contacts.append({"name": name, "phone": phone})


def remove_contact(name: str):
    """
    Odstraní kontakt ze seznamu podle jména.

    Args:
        name (str): Jméno kontaktu, který má být odstraněn.

    Returns:
        None

    Raises:
        KeyError: Pokud kontakt s daným jménem nebyl nalezen.
    """
    for contact in contacts:
        if contact["name"] == name:
            contacts.remove(contact)
            return
    raise KeyError(f"Kontakt '{name}' nebyl nalezen.")



def get_contact(name: str) -> str:
    """
    Vrátí telefonní číslo kontaktu podle zadaného jména.

    Args:
        name (str): Jméno kontaktu, jehož telefonní číslo se má vrátit.

    Returns:
        str: Telefonní číslo kontaktu.
    """
    # projdi všechny slovníky uložené v listu contacts
    for contact in contacts:
    # pokud nějaký slovník má klíč "name" s hodnotou name z parametru funkce, pak ho celý vrať
        if contact["name"] == name:
            return contact 
    # poud dojedeš až na konec, vrať None
    return None

def list_contacts() -> list:
    """
    Vrátí kopii seznamu všech kontaktů.

    Returns:
        list: Seznam kontaktů jako seznam slovníků se strukturou {"name": str, "phone": str}.
    """
    return contacts.copy()
