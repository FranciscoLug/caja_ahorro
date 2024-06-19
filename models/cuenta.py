from pydantic import BaseModel

class Cuenta_Ahorro(BaseModel):
    num_cuenta: int
    saldo: float
    id_cliente: int