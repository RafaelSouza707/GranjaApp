from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Date, ForeignKey, BigInteger, Numeric
from decimal import Decimal
from helpers.database import db


class Corte(db.Model):
    __tablename__ = "corte"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)

    id_lote_frango: Mapped[int] = mapped_column(BigInteger, ForeignKey("lote_frango.id", ondelete="RESTRICT"), nullable=False)

    data: Mapped[Date] = mapped_column(Date, nullable=False)

    peso: Mapped[Decimal] = mapped_column(Numeric(10, 3), nullable=False)

    lote_frango: Mapped["LoteFrango"] = relationship("LoteFrango", back_populates="corte")