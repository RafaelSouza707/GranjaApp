from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, BigInteger
from helpers.database import db


class TipoDespesa(db.Model):
    __tablename__ = "tipo_despesa"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    nome: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)

    despesa: Mapped[list["Despesa"]] = relationship("Despesa", back_populates="tipo_despesa")