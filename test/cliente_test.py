from controladores.cliente_control import create_cliente, delete_cliente, get_cliente

def test_create_cliente():
    """
    Test para la función create_cliente.

    >>> from models.cliente import Cliente
    >>> cliente_data = {"id_cliente": 1, "nombre": "John", "correo_electronico": "john@example.com", "password": "secret"}
    >>> cliente = Cliente(**cliente_data)
    >>> result = create_cliente(cliente)
    >>> "mensaje" in result
    True
    >>> "cliente" in result
    True

    """


def test_delete_cliente():
    """
    Test para la función delete_cliente.

    >>> from models.cliente import Cliente
    >>> cliente_data = {"id_cliente": 1, "nombre": "John", "correo_electronico": "john@example.com", "password": "secret"}
    >>> cliente = Cliente(**cliente_data)
    >>> delete_cliente(cliente)

    """

def test_get_cliente():
    """
    Test para la función get_cliente.

    >>> correo = "john@example.com"
    >>> contrasena = "secret"
    >>> result = get_cliente(correo, contrasena)
    >>> "id_cliente" in result
    True

    """
if __name__ == "__main__":
    import doctest
    doctest.testmod()