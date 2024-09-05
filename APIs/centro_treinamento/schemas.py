from typing import Annotated

from pydantic import Field
from APIs.contrib.schemas import BaseSchema


class CentroTreinamento(BaseSchema):
    nome: Annotated[str, Field(description='Nome do Centro de Treinamento', example="CT King", max_lenght=20)]
    endereco: Annotated[str, Field(description='Endereço do Centro de Treinamento', example="Rua X, B02", max_lenght=60)]
    proprietario: Annotated[str, Field(description='Proprietario do Centro de Treinamento', example="Marcos", max_lenght=30)]