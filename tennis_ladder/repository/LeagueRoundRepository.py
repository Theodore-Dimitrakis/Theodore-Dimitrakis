from entity.LeagueRound import LeagueRound

class LeagueRoundRepository:
    def __init__(self, session):
        self.session = session

    def create(self, league_round: LeagueRound):
        self.session.add(league_round)
        self.session.commit()

    def get_last_round(self):
        return self.session.query(LeagueRound).order_by(LeagueRound.round_number.desc()).first()

    def get_total_rounds(self):
        return self.session.query(LeagueRound).count()
