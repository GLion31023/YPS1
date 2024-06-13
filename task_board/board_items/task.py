from datetime import date

from task_board.board_items.board_item import BoardItem
from task_board.board_items.item_status import ItemStatus
from task_board.user.user import User


def check_valid_assignee_username(user):
    if len(user.username) < 5 or len(user.username) > 30 or user.username.isspace():
        raise ValueError("Allowed assignee length is 5 - 30 symbols")


class Task(BoardItem):
    def __init__(self, title: str, assignee: User, due_date: date):
        super().__init__(title, due_date, ItemStatus.TODO)
        check_valid_assignee_username(assignee)
        self._assignee = assignee

        self.log_event(f'Task created: {self.title}')

    @property
    def assignee(self):
        return self._assignee

    @assignee.setter
    def assignee(self, value):
        check_valid_assignee_username(value)
        self.log_event(f"Assignee changed from {self._assignee.username} to {value.username}")
        self._assignee = value

    def info(self):
        return f'Task (assigned to: {self._assignee.username}) {super().info()}'
