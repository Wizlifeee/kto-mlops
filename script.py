import unittest
from typing import List

def compter_prenoms(prenoms: List[str], seuil: int) -> int:
    """
    Parcourt une liste de prénoms et retourne le nombre de prénoms 
    dont le nombre de lettres est supérieur au seuil spécifié.
    
    Paramètres :
    - prenoms : Liste de chaînes représentant les prénoms.
    - seuil : Nombre de caractères à dépasser.
    
    Output :
    - int : Nombre de prénoms ayant un nombre de lettres supérieur au seuil.
    """
    
    nombre_prenoms = 0
    for prenom in prenoms:
        if len(prenom) > seuil:
            nombre_prenoms += 1
    return nombre_prenoms

class TestNamesMethod(unittest.TestCase):
    def test_names(self):
        prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        more_than_seven = compter_prenoms(prenoms=prenoms, seuil=7)
        self.assertEqual(more_than_seven, 4)

if __name__ == '__main__':
    unittest.main()
