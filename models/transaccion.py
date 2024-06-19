from datetime import datetime
from pydantic import BaseModel

class Transaccion(BaseModel):
    id_transaccion: int
    num_cuenta: int
    tipo_transaccion: int
    monto_transacciion: float
    fecha: datetime