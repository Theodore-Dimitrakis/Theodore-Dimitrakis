from datetime import datetime, timezone

from sqlalchemy import Column, Integer, ForeignKey, String, DateTime
from sqlalchemy.orm import relationship

from db_utils.DBUtils import Base

class Match(Base):
    __tablename__ = 'matches'

    match_id = Column(Integer, primary_key=True, autoincrement=True)
    player1_id = Column(Integer, ForeignKey('players.player_id'), nullable=False)
    player2_id = Column(Integer, ForeignKey('players.player_id'), nullable=False)
    set_scores = Column(String)
    total_of_score = Column(Integer,nullable=False)
    winner_id = Column(Integer, ForeignKey('players.player_id'))
    date_played = Column(DateTime, default=datetime.now(timezone.utc))


    player1 = relationship("Player", foreign_keys=[player1_id])
    player2 = relationship("Player", foreign_keys=[player2_id])
    winner = relationship("Player", foreign_keys=[winner_id])

    def __init__(self, player1, player2 , set_scores: str,total_of_score: int, winner):
        self.player1 = player1
        self.player2 = player2
        self.set_scores = set_scores
        self.total_of_score = total_of_score
        self.winner = winner

    def __repr__(self):
        return (f"Match(ID : {self.match_id}, Player 1 : {self.player1.name}, Player 2 : {self.player2.name}, "
                f"Score Set : {self.set_scores}, Total Sets Played : {self.total_of_score} , Winner : {self.winner.name})")
