from controladores.transaccion_control import create_transaccion, get_transacciones

def test_create_transaccion():
    """
    Test para la función create_transaccion.

    >>> from models.transaccion import Transaccion
    >>> transaccion_data = {"id_transaccion": 1, "id_cuenta": 1, "tipo_transaccion": 1, "monto": 100.0, "fecha_transaccion": "2023-01-01T00:00:00"}
    >>> transaccion = Transaccion(**transaccion_data)
    >>> result = create_transaccion(transaccion)
    >>> "mensaje" in result
    True
    >>> "transaccion" in result
    True

    """

def test_get_transacciones():
    """
    Test para la función get_transacciones.

    >>> from models.transaccion import Transaccion
    >>> transaccion_data = {"id_transaccion": 1, "id_cuenta": 1, "tipo_transaccion": 1, "monto": 100.0, "fecha_transaccion": "2023-01-01T00:00:00"}
    >>> transaccion = Transaccion(**transaccion_data)
    >>> create_transaccion(transaccion)  # Crear una transacción para la cuenta
    >>> result = get_transacciones(1)
    >>> isinstance(result, list)
    True

    """
if __name__ == "_main_":
    import doctest
    doctest.testmod()