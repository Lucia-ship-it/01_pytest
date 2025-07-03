from contacts import remove_contact
import pytest


@pytest.mark.slow
def test_r():
    with pytest.raises(KeyError) as e:
        name = "Anička"
        remove_contact(name)
        assert str(e) == f"Kontakt '{name}' nebyl nalezen."
