from datetime import datetime
from sqlalchemy import Datetime, Float, ForeignKey, Integer, String
from sqlalchemy import Mapped, mapped_column, relationship
from APIs.contrib.models import BaseModel

class AtletaModel(BaseModel):
    __tablename__ = "atletas"

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(50), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), nullable=False)
    idade: Mapped[int] = mapped_column(Integer, nullable=False)
    peso: Mapped[float] = mapped_column(Float, nullable=False)
    altura: Mapped[float] = mapped_column(Float, nullable=False)
    sexo: Mapped[str] = mapped_column(String(1), nullable=False)
    created_it: Mapped[datetime] = mapped_column(Datetime, nullable=False)
    categoria: Mapped['CategoriaModel'] = relationship(back_populates='atleta')
    categoria_id: Mapped[int] = mapped_column(ForeignKey('categoria.pk_id')) 
    centro_treinamento: Mapped['CentroTreinamentoModel'] = relationship(back_populates='atleta')
    centro_treinamento_id: Mapped[int] = mapped_column(ForeignKey('centros_treinamento.pk_id')) 