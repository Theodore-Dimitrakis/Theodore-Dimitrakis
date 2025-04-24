from sqlalchemy.orm import  Session

from Example import player_repository
from repository.PlayerRepository import PlayerRepository
from entity.Player import  Player


    def __init__(self,session:Session,player_repository:PlayerRepository):
        self.session=session
        self.player_repository=player_repository

    def add_player(self,name:str) -> Player:
        max_rank=self.player_repository.get_max_rank()
        new_rank=max_rank+1
        new_player=Player(name=name,rank=new_rank)
        self.player_repository.create(new_player)
        return new_player

    def delete_player(self,player_id:int):#Deletes a player and updates the rakings of the remaining players
        player_to_delete=self.session.query(Player).filter(Player.player_id==player_id).one_or_none()

        if player_to_delete:
            deteted_player_rank=player_to_delete.rank
            self.session.delete(player_to_delete)
            self.session.commit()
            player_to_update=self.session.query(Player).filter(Player.rank>deteted_player_rank).all()
            for player in player_to_update:
                player.rank-=1
                self.session.commit()
        else:
            print(f"{player_id}not fount","\U0001F605")


    def update_ranking_after_deletion(self,deleted_player_rank:int):
        players = self.player_repository.get_all()
        for player in players:
             if player.rank>deleted_player_rank:
                player.rank-=1
                self.player_repository.update(player)

    def get_player_by_id(self, player_id: int) -> Player:
        return self.player_repository.get_by_id(player_id)

    def get_all_players(self ) -> list[Player]:
        players = self.player_repository.get_all()
        return players ###




