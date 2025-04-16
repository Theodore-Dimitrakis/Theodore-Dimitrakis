from sqlalchemy import Column, Integer, String

from db_utils.DBUtils import Base

class Player(Base):
    __tablename__ = 'players'

    player_id = Column(Integer, primary_key=True, autoincrement=True)  # Ensure autoincrement
    name = Column(String, nullable=False)
    rank = Column(Integer, nullable=False)
    total_wins = Column(Integer, default=0)
    total_losses = Column(Integer, default=0)

    def __init__(self, name: str, rank: int, total_wins: int = 0, total_losses: int = 0):
        self.name = name
        self.rank = rank
        self.total_wins = total_wins
        self.total_losses = total_losses

    def __repr__(self):
        return f"Player(id={self.player_id}, name={self.name}, rank={self.rank})"
