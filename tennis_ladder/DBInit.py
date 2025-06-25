import os
from sqlalchemy import text
from db_utils.DBUtils import DBUtils, Base, DB_FILE_PATH

from entity.Match import Match
from entity.Player import Player
from entity.LeagueRound import LeagueRound

class DBInit:
    def __init__(self):
        self.engine, self.session = DBUtils.create_engine_and_session()

    def database_exists(self):
        return os.path.exists(DB_FILE_PATH)

    def create_db(self):
        DBUtils.create_tables(self.engine)
        print("Database and tables created successfully")

    def delete_database(self):
        if self.database_exists():
            os.remove(DB_FILE_PATH)
            print("Existing database deleted.")

    def insert_initial_players(self):
        players = [
            "Novak Djokovic", "Jannik Sinner", "Rafael Nadal", "Carlos Alcaraz",
            "Alexander Zverev", "Roger Federer", "Jack Dreper", "Taylor Fritz", "Lorenzo Musetti", "Holger Rune",
            "Ben Shelton", "Alex De Minaur", "Frances Tiafoe", "Jakub Mensik", "Fransisco Cerundolo", "Steffanos Tsitsipas",
            "Sebastian Korda", "Nuno Borges", "Gabriel Diallo", "Gael Monfils"
        ]
        player_objects = [Player(name=player_name, rank=i + 1) for i, player_name in enumerate(players)]
        self.session.add_all(player_objects)
        self.session.commit()

    def initialize_db(self):
        if self.session.query(Player).first():
            raise RuntimeError("Database already initialized. Cannot re-initialize.")
        self.insert_initial_players()

    def restart_db(self):
        try:
            self.session.execute(text("PRAGMA foreign_keys = OFF"))
            Base.metadata.reflect(bind=self.engine)
            for table in reversed(Base.metadata.sorted_tables):
                self.session.execute(table.delete())
            self.session.commit()
            self.session.execute(text("PRAGMA foreign_keys = ON"))
            print("Database restarted successfully.")
        except Exception as e:
            self.session.rollback()
            print(f"Error when restarting database: {e}")

if __name__ == "__main__":
    db_init = DBInit()
    db_init.initialize_db()

