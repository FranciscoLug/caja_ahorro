from fastapi import APIRouter, Depends, HTTPException
from models.transaccion import Transaccion
from controladores.transaccion_control import get_transacciones, create_transaccion

router = APIRouter()

@router.post("/transacciones/")
async def create_transaccion_endpoint(transaccion: Transaccion):
    result = create_transaccion(transaccion)
    return {"mensaje": result["mensaje"], "transaccion": result["transaccion"]}

@router.get("/transacciones/{id_cuenta}")
async def get_transacciones_por_cuenta_endpoint(id_cuenta: int):
    try:
        transacciones = get_transacciones(id_cuenta)
        return {"mensaje": "Transacciones obtenidas correctamente", "transacciones": transacciones}
    except HTTPException as e:
        return {"mensaje": "Error al procesar la solicitud", "detalle": e.detail}