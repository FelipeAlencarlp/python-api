from pydantic import BaseModel, Field

class UsuarioModel(BaseModel):
    nome: str = Field(...)
    email: str = Field(...)
    senha: str = Field(...)
    foto: str = Field(...)

    class Config:
        schema_extra = {
            "usuario": {
                "nome": "fulano",
                "email": "fulano@gmail.com",
                "senha": "Senha123",
                "foto": "fulano.png"
            }
        }