from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, Date, BigInteger, ForeignKey
from helpers.database import db


class Mortalidade(db.Model):
    __tablename__ = "mortalidade"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    id_lote_frango: Mapped[int] = mapped_column(BigInteger, ForeignKey("lote_frango.id", ondelete="RESTRICT"), nullable=False)

    data: Mapped[Date] = mapped_column(Date, nullable=False)

    quantidade_mortes: Mapped[int] = mapped_column(Integer, nullable=False)

    lote_frango: Mapped["LoteFrango"] = relationship("LoteFrango", back_populates="mortalidade")