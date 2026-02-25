from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, Date, ForeignKey, BigInteger, Numeric
from decimal import Decimal
from helpers.database import db


class VendaCorte(db.Model):
    __tablename__ = "venda_corte"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    id_lote_frango: Mapped[int] = mapped_column(BigInteger, ForeignKey("lote_frango.id", ondelete="RESTRICT"), nullable=False)

    data: Mapped[Date] = mapped_column(Date, nullable=False)
    valor: Mapped[Decimal] = mapped_column(Numeric(15, 2), nullable=False)

    quilos: Mapped[Decimal] = mapped_column(Numeric(12, 3), nullable=False)
    
    lote_frango: Mapped["LoteFrango"] = relationship("LoteFrango", back_populates="venda_corte")