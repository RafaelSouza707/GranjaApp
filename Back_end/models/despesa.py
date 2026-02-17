from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Date, Numeric, ForeignKey, BigInteger
from decimal import Decimal
from helpers.database import db


class Despesa(db.Model):
    __tablename__ = "despesa"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)

    id_tipo_despesa: Mapped[int] = mapped_column(BigInteger, ForeignKey("tipo_despesa.id", ondelete="RESTRICT"), nullable=False)
    
    data: Mapped[Date] = mapped_column(Date, nullable=False)

    valor: Mapped[Decimal] = mapped_column(Numeric(15, 2), nullable=False)
    
    tipo_despesa: Mapped["TipoDespesa"] = relationship("TipoDespesa", back_populates="despesa")