from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship

from db_utils.DBUtils import Base

class LeagueRound(Base):
    __tablename__ = 'league_rounds'

    id = Column(Integer, primary_key=True, autoincrement=True)
    round_number = Column(Integer, nullable=False, unique=True)
    #matches = relationship("Match", back_populates="league_round")