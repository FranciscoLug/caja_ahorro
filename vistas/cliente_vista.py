from fastapi import APIRouter, Depends, HTTPException
from models.cliente import Cliente
from controladores.cliente_control import get_cliente, create_cliente, delete_cliente

router = APIRouter()

@router.get("/clientes/")
async def get_cliente_endpoint(correo: str, password: str):
    try:
        cliente = get_cliente(correo, password)
        return {"mensaje": "Cliente obtenido correctamente", "cliente": cliente}
    except HTTPException as e:
        return {"mensaje": "Error al procesar la solicitud", "detalle": e.detail}
    
@router.post("/clientes/")
async def create_cliente_endpoint(cliente: Cliente):
    result = create_cliente(cliente)
    return {"mensaje": "Cliente creado exitosamente", "cliente": result["cliente"]}


@router.delete("/clientes/")
async def delete_cliente_endpoint(cliente: Cliente):
    result = delete_cliente(cliente)
    return {"mensaje": "Cliente eliminado correctamente"}