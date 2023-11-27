from fastapi import APIRouter, Body
from models.UsuarioModel import UsuarioModel

router = APIRouter()

@router.post("/", response_description="Rota para criar um novo Usuário.")
async def rota_criar_usuario(usuario: UsuarioModel = Body(...)):
    return {
        "mensagem" : "Usuário cadastrado com sucesso."
    }