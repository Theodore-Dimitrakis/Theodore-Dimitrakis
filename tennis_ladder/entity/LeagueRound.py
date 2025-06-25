from sqlalchemy import Column, Integer , Table , ForeignKey
from sqlalchemy.orm import relationship
from entity.Match import Match
from db_utils.DBUtils import Base

# Πίνακας Συσχέτισης μεταξύ LeagueRound και Match Οντοτητες  .
match_round_association = Table(
    'match_round_association',
    Base.metadata,
    Column('round_id', Integer, ForeignKey('league_round.id')),
    Column('match_id', Integer, ForeignKey('match.id'))
)

matches = relationship("Match", secondary=match_round_association, back_populates="rounds")

class LeagueRound(Base):
    __tablename__ = 'league_rounds'

    round_id = Column(Integer, primary_key=True, autoincrement=True)
    round_number = Column(Integer, nullable=False, unique=True)

    def __repr__(self):
        details_of_match = "\n".join(
            [f"Match ID : {match_info.match_id}, Player 1 : {match_info.player_1.name}, Player 2 : {match_info.player_2.name}, Score Set : {match_info.set_scores}, Total Sets Played : {match_info.total_of_score} , Winner : {match_info.winner}" for match_info in matches])
        return f"Round Number : {self.round_number}, Match : {details_of_match}"