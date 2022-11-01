def main():
    multiplicando = 589
    multiplicador = 12
    producto = multiplicando * multiplicador

    token_multiplicando = generar_token(obtener_digitos(multiplicando))
    token_multiplicador = generar_token(obtener_digitos(multiplicador))
    token_producto = generar_token(obtener_digitos(producto))
    token_producto_tokens_1_2 = generar_token(
        obtener_digitos(token_multiplicando * token_multiplicador))

    print(
        f'''Multiplicacion
        {multiplicando:5} x {multiplicador:5} = {producto}'''
    )
    print(
        f'''Multiplicacion de los tokens
        token<{token_multiplicando}> x token<{token_multiplicador}> = token<{token_producto_tokens_1_2}>'''
    )
    print(f'token de {producto} = token<{token_producto}>')

    prueba = f"Fallo: token<{token_producto_tokens_1_2}> != token<{token_producto}>" if token_producto_tokens_1_2 != token_producto else "Respuesta correcta"

    print('\n', prueba)


def obtener_digitos(numero: int) -> list:
    """Obtiene los digitos de un número dado y los retorna
    en forma de una lista."""
    digitos = []
    base = 10
    resto = numero
    while resto != 0:
        resto, digito = divmod(resto, base)
        digitos.append(digito)

    return digitos


def generar_token(digitos: list) -> int:
    """Obtiene un token entre 0 y 9 de una lista de digitos dada."""
    result = sum(digitos)
    while result > 9:
        result -= 9
    return result


if __name__ == '__main__':
    main()
