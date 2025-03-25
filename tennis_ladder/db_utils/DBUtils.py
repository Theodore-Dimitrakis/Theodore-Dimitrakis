from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# base class for the entities
Base = declarative_base()

class DBUtils:
    @staticmethod
    def create_engine_and_session(db_url="sqlite:///tennis_ladder.db"):
        """
        Create an engine and session to interact with the database.
        :param db_url: The URL of the database to connect to.
        :return: A tuple containing the engine and the session.
        """
        engine = create_engine(db_url, echo=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        return engine, session

    @staticmethod
    def create_tables(engine):
        """
        Create tables in the database based on the models that inherit from Base.
        :param engine: The engine to use for creating tables.
        """
        Base.metadata.create_all(engine)