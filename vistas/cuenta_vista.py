from fastapi import APIRouter, Depends, HTTPException, Query
from models.cuenta import Cuenta_Ahorro
from controladores.cuenta_control import create_cuenta, delete_cuenta, get_cuentas_usuario

router = APIRouter()

@router.post("/cuentas/")
async def create_cuenta_endpoint(cuenta: Cuenta_Ahorro):
    result = create_cuenta(cuenta)
    return {"mensaje": "Cuenta creada exitosamente", "cuenta": result["cuenta"]}


@router.delete("/cuentas/")
async def delete_cuenta_endpoint(cuenta: Cuenta_Ahorro):
    result = delete_cuenta(cuenta)
    return {"mensaje": "Cliente eliminado correctamente"}

@router.get("/cuentas/")
async def get_cuentas_usuario_endpoint(
    correo: str = Query(..., description="Correo electrónico del usuario"),
    contrasena: str = Query(..., description="Contraseña del usuario")
):
    try:
        cuentas = get_cuentas_usuario(correo, contrasena)
        return {"mensaje": "Cuentas obtenidas correctamente", "cuentas": cuentas}
    except HTTPException as e:
        return {"mensaje": "Error al procesar la solicitud", "detalle": e.detail}