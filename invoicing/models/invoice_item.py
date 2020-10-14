from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    Numeric,
    ForeignKey
)
from .base_model import BaseModel
from .meta import Base


class InvoiceItem(Base, BaseModel):
    __tablename__ = 'invoice_item'
    invoice_id = Column(Integer, ForeignKey('invoice.id'))
    id = Column(Integer, primary_key=True)
    description = Column(Text)
    units = Column(Integer)
    amount = Column(Numeric)


Index('InvoiceItemIdIndx', InvoiceItem.id, unique=True)
