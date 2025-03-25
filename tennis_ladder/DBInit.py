import os
from db_utils.DBUtils import DBUtils

# We need the Match and Player imports, otherwise the db schema will not create the matches and players tables
from entity.Match import Match
from entity.Player import Player

class DBInit:
    def __init__(self):
        project_root = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(project_root, 'tennis_ladder.db')
        self.db_url = f"sqlite:///{db_path}"
        self.engine, self.session = DBUtils.create_engine_and_session(self.db_url)

    def create_db(self):
        DBUtils.create_tables(self.engine)
        print("Database and tables created successfully")


if __name__ == "__main__":
    db_init = DBInit()
    db_init.create_db()