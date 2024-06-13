from datetime import datetime


class EventLog:
    def __init__(self, description: str):
        if not description or description.isspace():
            raise ValueError('Description cannot be empty')

        self._description = description
        self._timestamp = datetime.now()

    @property
    def description(self):
        return self._description

    @property
    def timestamp(self):
        return self._timestamp

    def info(self):
        return f'[{self._timestamp.strftime("%d/%m/%Y, %H:%M:%S")}] {self._description}'
