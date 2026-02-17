from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Date, ForeignKey, BigInteger, String
from helpers.database import db


class ControleVacina(db.Model):
    __tablename__ = "controle_vacina"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    id_lote_frango: Mapped[int] = mapped_column(BigInteger, ForeignKey("lote_frango.id", ondelete="RESTRICT"), nullable=False)

    medicamento_aplicado: Mapped[str] = mapped_column(String(100), nullable=False)
    data: Mapped[Date] = mapped_column(Date, nullable=False)
    responsavel_aplicacao: Mapped[str] = mapped_column(String(100), nullable=False)

    lote_frango: Mapped["LoteFrango"] = relationship("LoteFrango", back_populates="controle_vacina")