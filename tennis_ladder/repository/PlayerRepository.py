from sqlalchemy.orm import Session
from entity.Player import Player


class PlayerRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, name: str, rank: int) -> Player:
        new_player = Player(name=name, rank=rank)
        self.session.add(new_player)
        self.session.commit()
        return new_player

    def read(self, player_id: int) -> Player:
        return self.session.query(Player).filter_by(player_id=player_id).first()

    def update(self, player_id: int, name: str, rank: int) -> Player:
        player = self.read(player_id)
        if player:
            player.name = name
            player.rank = rank
            self.session.commit()
        return player

    def delete(self, player_id: int) -> bool:
        player = self.read(player_id)
        if player:
            self.session.delete(player)
            self.session.commit()
            return True
        return False

    def list_all(self) -> list[Player]:
        return self.session.query(Player).all()
