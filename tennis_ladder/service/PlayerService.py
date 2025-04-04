class PlayerService:
    def __init__(self, player_repository):
        self.player_repository = player_repository

    def add_player(self, name: str, rank: int):
        return self.player_repository.create(name, rank)
