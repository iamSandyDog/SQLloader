from sqlalchemy import create_engine

class BaseRepository(object):
    def __init__(self, dsn: str):
        self._engine = create_engine(dsn, echo=True)

