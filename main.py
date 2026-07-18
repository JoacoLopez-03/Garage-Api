from fastapi import FastAPI
from app.routers import marcas, modelos, auth, vehiculos, mantenimiento

app = FastAPI(title="Garage API")

app.include_router(auth.router)
app.include_router(marcas.router)
app.include_router(modelos.router)
app.include_router(vehiculos.router)
app.include_router(mantenimiento.router)

@app.get("/")
def read_root():
    return {"message": "Garage API funcionando 🚗"}