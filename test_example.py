import pytest
from contacts import get_contact

# testovací případ = funkci
def test_example():
    # jednotlivé kroky testovacího případu
    result = 1 + 1

    # kontrola, jestli reálný výsledek odpovídá očekavánámu
    assert result == 2

                                                    # do terminalu napisat : pytest a enter
                                                    # funguje aj: python3 -m pytest

def test_get_contact_positive():
    #zavolame funkci a jako parametr ji dame engeto 
     # dali sme na zaciatok, tam maju byt vsetky importy from contacts import get_contact
    result = get_contact("Engeto")
    #porovname vysledek
    assert result == {"name": "Engeto", "phone": "777777777"}

    # treba kazdy test pomenovat inak, pretoze zrovna na macbooku to zahlasi celkovu chybu. 

