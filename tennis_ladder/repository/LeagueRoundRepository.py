from entity.LeagueRound import LeagueRound


class LeagueRoundRepository:
    def __init__(self, session):
        self.session = session

    def create(self, league_round: LeagueRound):
        """Create a new league round."""
        self.session.add(league_round)
        self.session.commit()

    def get_last_round(self):
        """Get the most recent round."""
        return self.session.query(LeagueRound).order_by(LeagueRound.round_number.desc()).first()

    def get_total_rounds(self):
        """Get the total number of rounds played."""
        return self.session.query(LeagueRound).count()
