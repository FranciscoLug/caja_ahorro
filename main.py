from fastapi import FastAPI
from vistas.cliente_vista import router as cliente_router
from database.engine import engine
from vistas.cuenta_vista import router as cuenta_router
from vistas.transaccion_vista import router as transaccion_router

app = FastAPI()

def open_database_connection_pools():
    engine.connect()

app.add_event_handler("startup", open_database_connection_pools)
app.include_router(cliente_router)
app.include_router(cuenta_router)
app.include_router(transaccion_router)


@app.get("/")
def read_root():
    return {"Hello":"World"}