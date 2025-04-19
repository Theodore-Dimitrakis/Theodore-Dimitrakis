from DBInit import DBInit
from repository.PlayerRepository import PlayerRepository
from service.PlayerService import PlayerService
from controller.PlayerController import PlayerController

db_init = DBInit()
session = db_init.session

player_repository = PlayerRepository(session)
player_service = PlayerService(player_repository)
player_controller = PlayerController(player_service)

if __name__ == "__main__":
    player_controller.create_player("Novak Djokovic", 0)
    player_controller.create_player("Stefanos Tsitsipas",0)
    player_controller.create_player("Margaret Court",0)
    player_controller.create_player("Rafael Nadal",0)
    player_controller.create_player("Seren Williams",0)
    player_controller.create_player("Steffi Graf",0)
    player_controller.create_player("Roger Federer",0)
    player_controller.create_player("Helen Wills",0)
    player_controller.create_player("Martina Navratilova",0)
    player_controller.create_player("Chris Evert",0)
    player_controller.create_player("Billie Jean King",0)
    player_controller.create_player("Roy Emerson",0)
    player_controller.create_player("Rod Laver",0)
    player_controller.create_player("Bill Tilden",0)
    player_controller.create_player("Suzanne Lenglen",0)
    player_controller.create_player("Ken Rosewall",0)
    player_controller.create_player("Maria Sakkari",0)
    player_controller.create_player("Naomi Osaka",0)
    player_controller.create_player("Andre Agassi",0)
    player_controller.create_player("Bjorn Borg",0)
    player_controller.create_player("Rod Laver",0)
    player_controller.create_player("Pete Sampras",0)
