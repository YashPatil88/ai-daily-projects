from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base

class Result(Base):
    __tablename__ = 'results'
    id = Column(Integer, primary_key=True)
    score = Column(Integer)
    feedback = Column(String)
    interview_id = Column(Integer, ForeignKey('interviews.id'))
