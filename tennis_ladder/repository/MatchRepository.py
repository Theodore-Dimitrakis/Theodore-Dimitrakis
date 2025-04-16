from sqlalchemy.orm import Session
from entity.Match import Match
from entity.Player import Player


class MatchRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, match: Match) -> Match:
        self.session.add(match)
        self.session.commit()
        return match

    def get_by_id(self, match_id: int) -> Match:
        return self.session.query(Match).filter_by(match_id=match_id).first()

    def get_by_player(self, player: Player) -> list[Match]:
        return self.session.query(Match).filter(
            (Match.player1 == player) | (Match.player2 == player)
        ).all()

    def get_all(self) -> list[Match]:
        return self.session.query(Match).all()

    def get_by_date(self, date_played: str) -> list[Match]:
        return self.session.query(Match).filter_by(date_played=date_played).all()

    def get_by_winner(self, winner: Player) -> list[Match]:
        return self.session.query(Match).filter_by(winner=winner).all()

    def delete(self, match: Match) -> bool:
        self.session.delete(match)
        self.session.commit()
        return True

    def update(self, match: Match) -> Match:
        self.session.merge(match)
        self.session.commit()
        return match

    def bulk_update(self, matches: list[Match]) -> None:
        for match in matches:
            self.session.merge(match)
        self.session.commit()
