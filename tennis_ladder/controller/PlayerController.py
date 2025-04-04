class PlayerController:
    def __init__(self, player_service):
        self.player_service = player_service

    def create_player(self, name: str, rank: int):
        player = self.player_service.add_player(name, rank)
        print(f"Player created: {player.name}, Rank: {player.rank}")
