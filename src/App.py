from src.repository.BigKoopRepository import BigKoopRepository
from src.config.Config import Config
from src.command.FilldbCommand import FilldbCommand
from src.command.ReportCommand import ReportCommand

class App:
    """
    1.Создает BigKoopRepository, хранит в своем поле
    2.Имеет 2 метода на обработку команд
    """
    def __init__(self):
        config = Config()
        repo = BigKoopRepository(config.dbdsn)
        self.commands = {
            'filldb': FilldbCommand(repo, config.csvdir),
            'report': ReportCommand(repo)
        }

    def run(self, cmd: str):
        if cmd in self.commands:
            return self.commands[cmd].run()
        else:
            print("unknown command")

