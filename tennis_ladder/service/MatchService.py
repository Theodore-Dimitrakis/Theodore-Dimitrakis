import random

from sqlalchemy.orm import Session

from entity.LeagueRound import LeagueRound
from entity.Match import Match
from entity.Player import Player
from repository.MatchRepository import MatchRepository
from repository.PlayerRepository import PlayerRepository
from repository.LeagueRoundRepository import LeagueRoundRepository

class MatchService:
    def __init__(self, session: Session, match_repository: MatchRepository, player_repository: PlayerRepository, league_round_repository: LeagueRoundRepository):
        self.session = session
        self.match_repository = match_repository
        self.player_repository = player_repository
        self.league_round_repository = league_round_repository

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

        return {
            "challenger": challenger.name,
            "opponent": opponent.name,
            "score": set_scores,
            "winner": winner.name
        }

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

    def _get_players_ordered_by_rank(self) -> list[Player]:
        return self.session.query(Player).order_by(Player.rank).all()

    def _pair_remaining_players(self, players: list[Player], ranks: dict[int, int]) -> list[tuple[Player, Player]]:
        pairs = []
        players.sort(key=lambda p: ranks[p.player_id], reverse=True)

        while players:
            challenger = players.pop(0)
            challenger_rank = ranks[challenger.player_id]

            valid_opponents = [
                p for p in players
                if 0 < (challenger_rank - ranks[p.player_id]) <= 3
            ]

            if not valid_opponents:
                print(f"{challenger.name} could not find a valid opponent and skips the round.")
                continue

            opponent = min(valid_opponents, key=lambda p: ranks[p.player_id])
            pairs.append((challenger, opponent))
            players.remove(opponent)

        return pairs

    def _simulate_and_record_match(self, player1: Player, player2: Player):
        s1, s2 = random.randint(0, 2), random.randint(0, 2)
        while s1 == s2:
            s1, s2 = random.randint(0, 2), random.randint(0, 2)

        winner, loser = (player1, player2) if s1 > s2 else (player2, player1)
        winner.total_wins += 1
        loser.total_losses += 1

        if winner.rank > loser.rank:
            self.update_ranks_after_challenge(winner, loser)

        set_scores = f"{s1}-{s2}"
        match = Match(player1=player1, player2=player2, set_scores=set_scores, winner=winner)
        self.match_repository.create(match)

        return {
            "challenger": player1.name,
            "opponent": player2.name,
            "score": set_scores,
            "winner": winner.name
        }

    def _record_new_round(self, round_number: int):
        new_round = LeagueRound(round_number=round_number)
        self.session.add(new_round)
        self.session.commit()
        print(f"Round {round_number} completed.")

    def _announce_tournament_winner(self):
        top_player = (
            self.session.query(Player)
            .filter(Player.rank == 1)
            .one_or_none()
        )
        if top_player:
            print(f" The tournament winner is {top_player.name}!")

    def simulate_round(self, challenger_id: int, opponent_id: int):
        rounds_played = self.league_round_repository.get_total_rounds()
        print(f"Rounds played so far: {rounds_played}")

        if rounds_played >= 20:
            print("20 rounds have been played. No more challenges can be issued.")
            return

        players = self._get_players_ordered_by_rank()
        initial_ranks = {p.player_id: p.rank for p in players}

        challenge_result = self.create_match(challenger_id, opponent_id)

        match_results = []
        if challenge_result and "error" not in challenge_result:
            match_results.append(challenge_result)

        played_ids = {challenger_id, opponent_id}
        remaining_players = [p for p in players if p.player_id not in played_ids]

        matches_to_simulate = self._pair_remaining_players(remaining_players, initial_ranks)

        for player1, player2 in matches_to_simulate:
            result = self._simulate_and_record_match(player1, player2)
            if result:
                match_results.append(result)

        new_round_number = rounds_played + 1
        self._record_new_round(new_round_number)

        if new_round_number == 20:
            return self._announce_tournament_winner()

        print(f"\n--- Round {new_round_number} Match Results ---")
        for match in match_results:
            print(f"{match['challenger']} vs {match['opponent']} — Winner: {match['winner']} | Score: {match['score']}")

        return match_results