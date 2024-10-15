from datetime import datetime
import csv
from src.model.BigKoop import BigKoop
from src.repository.BigKoopRepository import BigKoopRepository

class FilldbCommand:
    FILE_NAME = 'big_koop.csv'

    def __init__(self, repository: BigKoopRepository, directory: str):
        self.__repo = repository
        self.__dir = directory

    def run(self):
        rows = []
        with open(self.__dir + '/' + self.FILE_NAME, 'r', encoding='UTF-8') as file:
            reader = csv.reader(file, delimiter=";")
            for i, line in enumerate(reader):
                amount = None
                if line[10] != '':
                    amount = float(line[10])
                rows.append(BigKoop(
                    material_group=line[0],
                    material_name=line[1],
                    region=line[2],
                    customer=line[3],
                    receiver=line[4],
                    contract_type=line[5],
                    warehouse=line[6],
                    shipment_type=line[7],
                    delivery_date=datetime.strptime(line[8], "%d.%m.%Y"),
                    department=line[9],
                    amount=amount
                ))

        self.__repo.deleteAll()
        self.__repo.save(rows)