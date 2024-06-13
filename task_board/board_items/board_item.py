from datetime import date

from task_board.board_items.item_status import ItemStatus
from task_board.event_logging.event_log import EventLog


def check_valid_title(title):
    if len(title) < 5 or len(title) > 30:
        raise ValueError('Allowed title range 5-30 symbols')
    return title


def check_valid_due_date(due_date):
    if due_date < date.today():
        raise ValueError('Due date cannot be in the past.')


class BoardItem:
    def __init__(self, title: str, due_date: date, status: ItemStatus.OPEN):
        check_valid_title(title)
        check_valid_due_date(due_date)

        self._title = title
        self._due_date = due_date
        self._status = status
        self._history = []

    @property
    def status(self):
        return self._status

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        check_valid_title(value)
        self.log_event(f'Title changed from {self._title} to {value}')
        self._title = value

    @property
    def due_date(self):
        return self._due_date

    @due_date.setter
    def due_date(self, value):
        check_valid_due_date(value)
        self.log_event(f'DueDate changed from {self._due_date} to {value}')
        self._due_date = value

    def revert_status(self):
        prev = self._status
        self._status = ItemStatus.previous(self.status)
        self.log_status_change(prev, self._status)

    def advance_status(self):
        prev = self._status
        self._status = ItemStatus.next(self.status)
        self.log_status_change(prev, self._status)

    def info(self):
        return f'{self.title}, [{self.status} | {self.due_date}]'

    def history(self):
        return f'\n'.join(event.info() for event in self._history)

    def log_event(self, description):
        self._history.append(EventLog(description))

    def log_status_change(self, prev: str, current: str):
        if prev == current:
            self._history.append(EventLog(f"Can't change status, already at {current}"))
        else:
            self._history.append(EventLog(f"Status changed from {prev} to {current}"))
