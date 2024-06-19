# controllers/cuenta_controllers.py
from sqlalchemy import text
from fastapi import HTTPException
from database.engine import engine
from controladores.cliente_control import valor_md5

def create_cuenta(cuenta):
    with engine.connect() as connection:
        query = text("INSERT INTO cuentas_ahorro (id_cuenta, id_usuario, saldo) VALUES (:id_cuenta, :id_usuario, :saldo)")
        connection.execute(query, id_cuenta=cuenta.id_cuenta, id_usuario=cuenta.id_usuario, saldo=cuenta.saldo)
    return {"mensaje": "Cuenta creada exitosamente", "cuenta": cuenta}

def delete_cuenta(cuenta):
    with engine.connect() as connection:
        query = text("DELETE FROM cuentas_ahorro WHERE id_cuenta = :id_cuenta")
        connection.execute(query, id_cuenta=cuenta.id_cuenta)

def get_cuentas_usuario(correo, contrasena):
    try:
        with engine.connect() as connection:
            query = text("SELECT id_cuenta, id_usuario, saldo FROM cuentas_ahorro WHERE id_usuario = ("
                         "SELECT id_cliente FROM clientes WHERE correo_electronico = :correo_electronico AND password = :contra_md5)"
                         )
            result = connection.execute(query, correo_electronico=correo, contra_md5=valor_md5(contrasena)).fetchall()

            cuentas_data = [dict(row) for row in result]
            return {"mensaje": "Cuentas obtenidas correctamente", "cuentas": cuentas_data}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener cuentas del usuario: {str(e)}")