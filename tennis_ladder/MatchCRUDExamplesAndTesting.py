from DBInit import DBInit
from repository.LeagueRoundRepository import LeagueRoundRepository
from repository.MatchRepository import MatchRepository
from repository.PlayerRepository import PlayerRepository
from service.MatchService import MatchService


# Initialize DB session using existing DBInit logic
db_init = DBInit()
session = db_init.session  # Reuse the session

# Instantiate layers for Players
player_dao = PlayerRepository(session)

# Instantiate layers for Matches
match_dao = MatchRepository(session)
league_round_repository = LeagueRoundRepository(session)
match_service = MatchService(session, match_dao, player_dao, league_round_repository)

def test_create_match(challenger_id, opponent_id):
    print(f"\nCreating match between player {challenger_id} and player {opponent_id}:")
    match_service.create_match(challenger_id, opponent_id)

def test_list_all_matches():
    print("\nListing all matches:")

if __name__ == "__main__":


    #match_service.create_match(4,1)
    match_service.simulate_round(4, 3)

    # Test listing all matches after creation
    #test_list_all_matches()
