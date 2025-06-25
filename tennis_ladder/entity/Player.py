from sqlalchemy import Column, Integer, String , Float

from db_utils.DBUtils import Base

class Player(Base):
    __tablename__ = 'players'


    player_id = Column(Integer, primary_key=True, autoincrement=True)  # Ensure autoincrement
    name = Column(String, nullable=False)
    rank = Column(Integer, nullable=False)
    country = Column(String,nullable=False)
    age = Column(Integer,nullable=False)
    hand = Column(String,nullable=False)
    win_percentage = Column(Float,nullable=False)
    lost_pecentage = Column(Float,nullable=False)
    height = Column(Float,nullable=False)
    weight = Column(Float,nullable=False)
    total_wins = Column(Integer, default=0)
    total_losses = Column(Integer, default=0)

    def __init__(self, name: str, rank: int, country:str,age: int,hand: str,win_percentage: float,lost_pecentage: float,height: float,weight: float, total_wins: int = 0, total_losses: int = 0):
        self.name = name
        self.rank = rank
        self.country = country
        self.age = age
        self.hand = hand
        self.win_percentage = win_percentage
        self.lost_pecentage = lost_pecentage
        self.height = height
        self.weight = weight
        self.total_wins = total_wins
        self.total_losses = total_losses

    def __repr__(self):
        return (f"Player(ID : {self.player_id}, Name : {self.name}, Rank: {self.rank}, Country : {self.country}, Age : {self.age}, Hand : {self.hand}, Win Percentage : {self.win_percentage}, Lost Percentage : {self.lost_percentage}, Victories : {self.total_wins} , Defeats : {self.total_losses}")
