from sqlalchemy.orm import  Session

from Example import player_repository
from repository.PlayerRepository import PlayerRepository
from entity.Player import  Player

class PlayerService:
    def __init__(self, player_dao):
        self.player_dao = player_dao

    def add_player(self, name: str, rank: int):
        return self.player_dao.create(name, rank)

    def __init__(self,session:Session,player_repository:PlayerRepository):
        self.session=session
        self.player_repository=player_repository

    def add_player(self,name:str) -> Player:#Adds a new player to of the bottom rankings
        max_rank=self.player_repository.get_max_rank()
        new_rank=max_rank+1
        new_player=Player(name=name,rank=new_rank)
        self.player_repository.create(new_player)
        return new_player

    def delete_player(self,player_id:int):#Deletes a player and updates the rakings of the remaining players
        player_to_delete=self.session.query(Player).filter(Player.player_id==player_id).one_or_none()
        delete_rank=player_to_delete.rank
        self.session.delete(player_to_delete)
        self.session.commit()
        players_to_update = self.session.query(Player).filter(Player.rank > delete_rank).all()
        for player in players_to_update:
            player.rank -= 1
        self.session.commit()
        if player_to_delete is None:
            print(f"{player_id}not fount","\U0001F605")
            return

    def update_ranking_after_deletion(self,deleted_player_rank:int):#Update the ranking after player has been deleted
        players = self.player_repository.get_all()
        for player in players:
             if player.rank>deleted_player_rank:
                player.rank-=1
                self.session.commit()

    def get_player_by_id(self, player_id: int) -> Player:#returns a player by their ID
        return self.player_repository.get_by_id(player_id)

    def get_all_players(self ) -> list[Player]:# Returns all players
        players = self.player_repository.get_all()
        return players ###




