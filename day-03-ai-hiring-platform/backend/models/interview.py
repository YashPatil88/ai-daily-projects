from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Interview(Base):
    __tablename__ = 'interviews'
    id = Column(Integer, primary_key=True)
    role = Column(String)
    candidate_id = Column(Integer, ForeignKey('users.id'))
