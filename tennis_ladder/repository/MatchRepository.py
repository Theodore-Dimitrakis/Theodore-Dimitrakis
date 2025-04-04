from sqlalchemy.orm import Session
from entity.Match import Match
from entity.Player import Player


class MatchRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, player1: Player, player2: Player, set_scores: str, winner: Player, date_played: str) -> Match:
        new_match = Match(player1=player1, player2=player2, set_scores=set_scores, winner=winner, date_played=date_played)
        self.session.add(new_match)
        self.session.commit()
        return new_match

    def read(self, match_id: int) -> Match:
        return self.session.query(Match).filter_by(match_id=match_id).first()

    def update(self, match_id: int, player1: Player, player2: Player, set_scores: str, winner: Player, date_played: str) -> Match:
        match = self.read(match_id)
        if match:
            match.player1 = player1
            match.player2 = player2
            match.set_scores = set_scores
            match.winner = winner
            match.date_played = date_played
            self.session.commit()
        return match

    def delete(self, match_id: int) -> bool:
        match = self.read(match_id)
        if match:
            self.session.delete(match)
            self.session.commit()
            return True
        return False

    def list_all(self) -> list[Match]:
        return self.session.query(Match).all()
