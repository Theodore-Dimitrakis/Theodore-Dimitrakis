class PlayerService:
    def __init__(self, player_dao):
        self.player_dao = player_dao

    def add_player(self, name: str, rank: int):
        return self.player_dao.create(name, rank)
