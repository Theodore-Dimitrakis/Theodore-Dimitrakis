from DBInit import DBInit
from dao.PlayerDAO import PlayerDAO
from service.PlayerService import PlayerService
from controller.PlayerController import PlayerController

# Initialize DB session using existing DBInit logic
db_init = DBInit()
session = db_init.session  # Reuse the session

# Instantiate layers
player_dao = PlayerDAO(session)
player_service = PlayerService(player_dao)
player_controller = PlayerController(player_service)

if __name__ == "__main__":
    player_controller.create_player("Novak Djokovic", 1)
