import unittest
import prueba_del_9


class TestStringMethods(unittest.TestCase):
    def test_ejemplo(self):
        numero1 = 123
        numero2 = 12
        resultado = numero1 * numero2

        token1 = prueba_del_9.generar_token(
            prueba_del_9.obtener_digitos(numero1)
        )
        token2 = prueba_del_9.generar_token(
            prueba_del_9.obtener_digitos(numero2)
        )

        tokenResultado = prueba_del_9.generar_token(
            prueba_del_9.obtener_digitos(resultado)
        )
        tokenMultiplication = prueba_del_9.generar_token(
            prueba_del_9.obtener_digitos(token1 * token2)
        )

        self.assertEqual(
            first=tokenResultado,
            second=tokenMultiplication,
            msg="Fallo ejemplo"
        )

    def test_obtener_digitos(self):
        self.assertEqual(
            first=prueba_del_9.obtener_digitos(124),
            second=[4, 2, 1],
            msg="Obtener digitos fallo"
        )

    def test_generar_token(self):
        self.assertEqual(
            first=prueba_del_9.generar_token(digitos=[1, 2, 3]),
            second=6,
            msg="Obtener un token fallo"
        )
        self.assertEqual(
            first=prueba_del_9.generar_token(digitos=[5, 8, 9]),
            second=4,
            msg="Obtener un token fallo"
        )


if __name__ == '__main__':
    unittest.main()
