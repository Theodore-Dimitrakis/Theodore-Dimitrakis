import os
import sys
import shutil
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

DB_FILE_NAME = "tennis_ladder.db"
DB_FILE_PATH = os.path.join(os.getcwd(), DB_FILE_NAME)
DB_URL = f"sqlite:///{DB_FILE_PATH}"

class DBUtils:
    @staticmethod
    def create_engine_and_session():
        """
        Ensure the DB exists at runtime. If bundled, copy it from inside the bundle.
        """
        # If not already there, try copying it
        if not os.path.exists(DB_FILE_PATH):
            if getattr(sys, 'frozen', False):
                # Running from PyInstaller bundle
                base_path = sys._MEIPASS
            else:
                base_path = os.path.dirname(os.path.abspath(__file__))

            bundled_db_path = os.path.join(base_path, DB_FILE_NAME)
            if os.path.exists(bundled_db_path):
                shutil.copy2(bundled_db_path, DB_FILE_PATH)

        engine = create_engine(DB_URL, echo=True)
        Session = sessionmaker(bind=engine)
        session = Session()
        return engine, session

    @staticmethod
    def create_tables(engine):
        Base.metadata.create_all(engine)


