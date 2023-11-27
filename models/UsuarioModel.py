from pydantic import BaseModel, Field

class UsuarioModel(BaseModel):
    id: str = Field(...)
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

class UsuarioCriarModel(BaseModel):
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

class UsuarioLoginModel(BaseModel):
    email: str = Field(...)
    senha: str = Field(...)

    class Config:
        schema_extra = {
            "usuario": {
                "email": "fulano@gmail.com",
                "senha": "Senha123"
            }
        }