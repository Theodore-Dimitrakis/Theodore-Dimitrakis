from sqlalchemy import Column, Integer, String

from db_utils.DBUtils import Base

class Player(Base):
    __tablename__ = 'players'

    player_id = Column(Integer, primary_key=True)
    name = Column(String)
    rank = Column(Integer)
    total_wins = Column(Integer, default=0)
    total_losses = Column(Integer, default=0)

    def __init__(self, player_id, name, rank, total_wins=0, total_losses=0):
        self.player_id = player_id
        self.name = name
        self.rank = rank
        self.total_wins = total_wins
        self.total_losses = total_losses
        self.matches_played = []

    def __repr__(self):
        return f"Player(id={self.player_id}, name={self.name}, rank={self.rank})"
