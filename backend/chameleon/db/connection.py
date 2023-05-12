from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from chameleon.db.base_model import Base
from chameleon.db.groups_model import Groups


class dbConnector:
    def __init__(self):
        my_url = "postgresql://postgresUser:postgresPass@localhost:5432/chameleon"
        self.engine = create_engine(my_url)

    def connect(self):
        return self.engine.connect()
    
    def create_tables(self):
        Base.metadata.create_all(self.engine)