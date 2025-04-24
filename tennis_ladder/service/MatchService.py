import random

from sqlalchemy.orm import Session

from entity.Match import Match
from entity.Player import Player
from repository.MatchRepository import MatchRepository
from repository.PlayerRepository import PlayerRepository

class MatchService:
    def __init__(self, session: Session, match_repository: MatchRepository, player_repository: PlayerRepository):
        self.session = session
        self.match_repository = match_repository
        self.player_repository = player_repository

    def get_all_matches(self):
        return self.match_repository.get_all()

    def create_match(self, challenger_id: int, opponent_id: int):
        challenger = self.player_repository.get_by_id(challenger_id)
        opponent = self.player_repository.get_by_id(opponent_id)

        if not challenger or not opponent:
            print("One or both players not found.")
            return

        if abs(challenger.rank - opponent.rank) > 3:  # assuming N=3
            print("Challenge is invalid: Player is too far above to challenge.")
            return

        challenger_sets_won = random.randint(0, 2)
        opponent_sets_won = random.randint(0, 2)

        while challenger_sets_won == opponent_sets_won:
            challenger_sets_won = random.randint(0, 2)
            opponent_sets_won = random.randint(0, 2)

        if challenger_sets_won > opponent_sets_won:
            winner = challenger
            loser = opponent
        else:
            winner = opponent
            loser = challenger

        winner.total_wins += 1
        loser.total_losses += 1

        if winner == challenger:
            self.update_ranks_after_challenge(winner, loser)

        set_scores = f"{challenger_sets_won}-{opponent_sets_won}"

        match = Match(
            player1=challenger,
            player2=opponent,
            set_scores=set_scores,
            winner=winner,
        )

        self.match_repository.create(match)
        print(f"Match created: {challenger.name} vs {opponent.name}, Winner: {winner.name}, Score: {set_scores}")

    def update_ranks_after_challenge(self, winner: Player, loser: Player):
        winner_rank = winner.rank
        loser_rank = loser.rank

        if winner_rank > loser_rank:
            players_to_shift = (
                self.session.query(Player)
                .filter(Player.rank >= loser_rank, Player.rank < winner_rank)
                .order_by(Player.rank.asc())
                .all()
            )

            for player in players_to_shift:
                player.rank += 1

            winner.rank = loser_rank
            self.session.commit()