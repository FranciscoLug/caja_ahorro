from pydantic import BaseModel

class Cliente(BaseModel):
    id_cliente: int
    usuario: str
    email: str
    password: str