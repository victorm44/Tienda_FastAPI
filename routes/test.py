# routes/test.py
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from database.database import app

router = APIRouter()

@router.get("/test-db-connection")
async def test_db_connection():
    try:
        # Realiza una operación de prueba en la base de datos
        test_result = await app.state.db.command("ping")
        return JSONResponse(content={"message": "Conexión exitosa a la base de datos.", "test_result": test_result})
    except Exception as e:
        return HTTPException(status_code=500, detail=f"Error de conexión a la base de datos: {str(e)}")
