import pytest
from contacts import get_contact

# testovací případ = funkci
@pytest.mark.skip(reason="netreba")
def test_example():
    # jednotlivé kroky testovacího případu
    result = 1 + 1

    # kontrola, jestli reálný výsledek odpovídá očekavánámu
    assert result == 2

                                                    # do terminalu napisat : pytest a enter
                                                    # funguje aj: python3 -m pytest
@pytest.mark.positive
def test_get_contact_positive():
    #zavolame funkci a jako parametr ji dame engeto 
     # dali sme na zaciatok, tam maju byt vsetky importy from contacts import get_contact
    result = get_contact("Engeto")
    #porovname vysledek
    assert result == {"name": "Engeto", "phone": "777777777"}

@pytest.mark.positive
def test_get_contact_positive_2():
    #zavolame funkci a jako parametr ji dame engeto 
     # dali sme na zaciatok, tam maju byt vsetky importy from contacts import get_contact
    result = get_contact("Engeto")
    print(result)
    #porovname vysledek
    assert result == {"name": "Engeto", "phone": "777777777"}

    # treba kazdy test pomenovat inak, pretoze zrovna na macbooku to zahlasi celkovu chybu. 
@pytest.mark.negative
def test_get_contact_negative():
    result = get_contact("akademie")
    assert result == None

# def test_get_contact_negative_chybovy():
#     result = get_contact("akademie")
#     assert result == {"name": "Engeto", "phone": "777777777"}

# roydelenie testov
# 1. rychle
# 2. zatezove

# alebo pozitivni a negativni = @pytest.mark.positive - @ je dekorator

# a vytvorim si novy dokument pytest.ini
# a tam si dam tie znacky
# a vdaka tomu mozem dat do terminalu poziadavku na spustenie len pozitivnych testov
# pytest -m "positive"
# alebo mozem skovat test @pytest.mark.skip(reason="je to zastarale")
# aleboooo s podmienkkou @pytest.mark.skipif(......)
# @pytest.mark.parametrise.......
# este sa da pustit len jeden subor. v terminaly: pytest test_example.py
# mozem pustit len 1 konkretny priklad a to v terminaly: pytest test_example.py::test_get_contact_negative
# pytest default zachyti vsetky print funkcie a nezobrazi ich. iba ked chcem, tak do terminalu nakoniec napisem -s: pytest test_example.py::test_get_contact_positive_2 -s
# pre porovnanie: pytest test_example.py::test_get_contact_positive_2
# ak tam dame -v (v ako verbouse) zacne podrobne vypisovat co sa stalo v testoch: pytest -v
# pri kazdom asserte mozem napisat informacnu hlasku 

def test_get_contact_negative_chybovy():
    result = get_contact("Engeto")
    assert result == None, f"ocekavano None, ve skutecnosti {result}"