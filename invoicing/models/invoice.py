from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    DateTime
)

from .base_model import BaseModel
from .meta import Base


class Invoice(Base, BaseModel):
    __tablename__ = 'invoice'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime)

Index('Invoice_id_indx', Invoice.id, unique=True)
