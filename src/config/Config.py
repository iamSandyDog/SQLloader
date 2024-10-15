import os
from dotenv import load_dotenv

class Config:
    def __init__(self):
        load_dotenv()
        self.dbdsn = os.getenv('DSN')
        self.csvdir = 'runtime'