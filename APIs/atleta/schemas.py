from typing import Annotated
from pydantic import BaseModel, Field, PositiveFloat

class Atleta(BaseModel):
    nome: Annotated[str, Field(description='Nome do Atleta', examples="Joao", max_lenght=50)]
    cpf: Annotated[str, Field(description='CPF do Atleta', examples="11122293810", max_lenght=11)]
    idade: Annotated[int, Field(description='Idade do Atleta', examples=25)]
    peso: Annotated[PositiveFloat, Field(description='Peso do Atleta', examples=50.5)]
    altura: Annotated[PositiveFloat, Field(description='Altura do Atleta', examples=1.70)]
    sexo: Annotated[str, Field(description='Sexo do Atleta', examples="M", max_lenght=1)]
