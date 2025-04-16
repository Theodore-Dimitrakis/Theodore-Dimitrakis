from sqlalchemy.orm import Session
from entity.Player import Player


class PlayerRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, player: Player):
        self.session.add(player)
        self.session.commit()

    def get_by_id(self, player_id: int) -> Player:
        return self.session.query(Player).filter_by(player_id=player_id).first()

    def get_all(self) -> list[Player]:
        return self.session.query(Player).order_by(Player.rank).all()

    def get_max_rank(self) -> int:
        return self.session.query(Player.rank).order_by(Player.rank.desc()).first()[0]

    def delete(self, player: Player):
        self.session.delete(player)
        self.session.commit()

    def update(self, player: Player):
        self.session.merge(player)
        self.session.commit()

    def bulk_update(self, players: list[Player]):
        for player in players:
            self.session.merge(player)
        self.session.commit()

    def update_player_rank(self, player: Player, new_rank: int) -> None:
        player.rank = new_rank
        self.session.commit()

    def update_players_between_ranks(self, start_rank: int, end_rank: int) -> None:
        players_to_update = self.session.query(Player).filter(
            Player.rank > start_rank, Player.rank < end_rank
        ).all()
        for player in players_to_update:
            player.rank -= 1
        self.session.commit()
