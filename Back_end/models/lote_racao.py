from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Date, BigInteger, Numeric
from decimal import Decimal
from helpers.database import db


class LoteRacao(db.Model):
    __tablename__ = "lote_racao"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)

    tipo_racao: Mapped[str] = mapped_column(String(30), nullable=False)
    fornecedor: Mapped[str] = mapped_column(String(100), nullable=False)

    data_compra: Mapped[Date] = mapped_column(Date, nullable=False)

    quilos: Mapped[Decimal] = mapped_column(Numeric(12, 3), nullable=False)

    valor: Mapped[Decimal] = mapped_column(Numeric(15, 2), nullable=False)