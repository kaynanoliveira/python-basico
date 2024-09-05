from typing import Annotated
from pydantic import Field, PositiveFloat

from APIs.contrib.schemas import BaseSchema

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do Atleta', example="Joao", max_lenght=50)]
    cpf: Annotated[str, Field(description='CPF do Atleta', example="11122293810", max_lenght=11)]
    idade: Annotated[int, Field(description='Idade do Atleta', example=25)]
    peso: Annotated[PositiveFloat, Field(description='Peso do Atleta', example=50.5)]
    altura: Annotated[PositiveFloat, Field(description='Altura do Atleta', example=1.70)]
    sexo: Annotated[str, Field(description='Sexo do Atleta', example="M", max_lenght=1)]
