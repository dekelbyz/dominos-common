from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Mapped
from .database import Base

class Restaurant(Base):
    ''' db schema '''
    __tablename__ = 'restaurants'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = Column(String(50), unique=True, nullable=False)
    address_id = mapped_column(ForeignKey('addresses.id'), nullable=False)
