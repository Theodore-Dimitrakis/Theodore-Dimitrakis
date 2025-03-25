from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from db_utils.DBUtils import Base

class Match(Base):
    __tablename__ = 'matches'

    match_id = Column(Integer, primary_key=True)
    player1_id = Column(Integer, ForeignKey('players.player_id'))
    player2_id = Column(Integer, ForeignKey('players.player_id'))
    set_scores = Column(String)
    winner_id = Column(Integer, ForeignKey('players.player_id'))
    date_played = Column(String, nullable=True)

    player1 = relationship("Player", foreign_keys=[player1_id])
    player2 = relationship("Player", foreign_keys=[player2_id])
    winner = relationship("Player", foreign_keys=[winner_id])

    def __init__(self, match_id, player1, player2, set_scores, winner):
        self.match_id = match_id
        self.player1 = player1
        self.player2 = player2
        self.set_scores = set_scores
        self.winner = winner

    def __repr__(self):
        return (f"Match(id={self.match_id}, player1={self.player1.name}, player2={self.player2.name}, "
                f"set_scores={self.set_scores}, winner={self.winner.name})")
