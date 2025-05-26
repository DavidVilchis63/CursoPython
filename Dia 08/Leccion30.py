"""
Continuacion de Leccion 29, probar codigo con unittest
"""

import unittest
import Leccion29 

class ProbarCambiaTexto(unittest.TestCase):

    def test_cambioTxt(self):
        palabra = "palabra ejemplo"
        resultado = Leccion29.cambiaTexto(palabra)
        self.assertEqual(resultado, "PALABRA EJEMPLO")

    
if __name__ == "__main__":
    unittest.main()

