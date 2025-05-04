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

        if abs(challenger.rank - opponent.rank) > 3:
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

    def simulate_round(self, challenger_id: int, opponent_id: int):
        players = (
            self.session.query(Player)
            .order_by(Player.rank)
            .all()
        )
        player_by_id = {player.player_id: player for player in players}
        initial_ranks = {player.player_id: player.rank for player in players}
        played_ids = set()

        self.create_match(challenger_id, opponent_id)
        played_ids.update({challenger_id, opponent_id})

        remaining_players = [p for p in players if p.player_id not in played_ids]

        matches_to_simulate = []

        remaining_players.sort(key=lambda p: initial_ranks[p.player_id], reverse=True)

        while remaining_players:
            challenger = remaining_players.pop(0)
            challenger_rank = initial_ranks[challenger.player_id]

            possible_opponents = [
                p for p in remaining_players
                if 0 < (challenger_rank - initial_ranks[p.player_id]) <= 3
            ]

            if not possible_opponents:
                print(f"{challenger.name} could not find a valid opponent and skips the round.")
                continue

            opponent = min(possible_opponents, key=lambda p: initial_ranks[p.player_id])

            matches_to_simulate.append((challenger, opponent))

            remaining_players.remove(opponent)

        for player1, player2 in matches_to_simulate:
            challenger_sets_won = random.randint(0, 2)
            opponent_sets_won = random.randint(0, 2)

            while challenger_sets_won == opponent_sets_won:
                challenger_sets_won = random.randint(0, 2)
                opponent_sets_won = random.randint(0, 2)

            if challenger_sets_won > opponent_sets_won:
                winner = player1
                loser = player2
            else:
                winner = player2
                loser = player1

            winner.total_wins += 1
            loser.total_losses += 1

            if winner.rank > loser.rank:
                self.update_ranks_after_challenge(winner, loser)

            set_scores = f"{challenger_sets_won}-{opponent_sets_won}"

            match = Match(
                player1=player1,
                player2=player2,
                set_scores=set_scores,
                winner=winner,
            )

            self.match_repository.create(match)

            print(f"Auto Match: {player1.name} vs {player2.name}, Winner: {winner.name}, Score: {set_scores}")

        self.session.commit()
