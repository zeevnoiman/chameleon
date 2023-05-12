from sqlalchemy import Column, Integer, String, DateTime, Text, Boolean, ForeignKey
from datetime import datetime
from chameleon.db.base_model import Base

class Groups(Base):
    __tablename__ = 'groups'

    id = Column(Integer(), primary_key=True)
    code = Column(String(100), nullable=False, unique=True)
    active = Column(Boolean(), nullable=False)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)