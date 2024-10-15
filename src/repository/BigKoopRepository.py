import sqlalchemy
from sqlalchemy.orm import Session
from src.repository.BaseRepository import BaseRepository
from sqlalchemy import select
from src.model.BigKoop import BigKoop

class BigKoopRepository(BaseRepository):
    def __init__(self, dsn: str):
        super().__init__(dsn)

    def getRow(self, id: int):
        session = Session(self._engine)
        stmt = select(BigKoop).where(BigKoop.id==id)
        return session.scalars(stmt).one()

    def deleteAll(self):
        """
        Удаляет все из БД таблицы
        """
        with Session(self._engine) as session:
            session.execute(sqlalchemy.text("TRUNCATE TABLE " + BigKoop.__tablename__ + " RESTART IDENTITY CASCADE;"))
            session.commit()

    def save(self, models: list[BigKoop]):
        """
        Получает массив классов BigKoop и сохраняет их в БД
        """
        with Session(self._engine) as session:
            session.add_all(models)
            session.commit()

    def dataSelector(self):
        """
        Выбирает данные для построения отчета, SQL запрос хранится здесь же
        """
        with Session(self._engine) as session:
            query = sqlalchemy.text("""SELECT * FROM public.big_koop  
                                            WHERE big_koop.shipment_type = 'Самовывоз'""")
            result = session.execute(query)
        return result.all()
