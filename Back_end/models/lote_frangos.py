from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, Date, Numeric, BigInteger
from helpers.database import db
from decimal import Decimal


class LoteFrango(db.Model):
    __tablename__ = "lote_frango"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)

    quantidade_inicial: Mapped[int] = mapped_column(BigInteger, nullable=False)
    data_entrada_aves: Mapped[Date] = mapped_column(Date, nullable=False)
    data_ninhada: Mapped[Date] = mapped_column(Date)
    fornecedor: Mapped[str] = mapped_column(String(100))
    tipo_lote: Mapped[str] = mapped_column(String(20))
    galpao: Mapped[int] = mapped_column(Integer)
    status: Mapped[str] = mapped_column(String(50))

    peso_medio: Mapped[Decimal] = mapped_column(Numeric(10, 3))

    mortalidade: Mapped[list["Mortalidade"]] = relationship("Mortalidade", back_populates="lote_frango", cascade="all, delete-orphan")
    postura: Mapped[list["Postura"]] = relationship("Postura", back_populates="lote_frango", cascade="all, delete-orphan")
    corte: Mapped[list["Corte"]] = relationship("Corte", back_populates="lote_frango", cascade="all, delete-orphan")
    venda_corte: Mapped[list["VendaCorte"]] = relationship("VendaCorte", back_populates="lote_frango", cascade="all, delete-orphan")
    venda_ovos: Mapped[list["VendaOvos"]] = relationship("VendaOvos", back_populates="lote_frango", cascade="all, delete-orphan")
    controle_vacina: Mapped[list["ControleVacina"]] = relationship("ControleVacina", back_populates="lote_frango", cascade="all, delete-orphan")
    consumo_lote_diaria: Mapped[list["ConsumoLoteDiaria"]] = relationship("ConsumoLoteDiaria", back_populates="lote_frango", cascade="all, delete-orphan")