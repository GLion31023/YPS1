from datetime import date

from task_board.board_items.item_status import ItemStatus
from task_board.board_items.board_item import BoardItem


class Issue(BoardItem):
    def __init__(self, title: str, description: str, due_date: date):
        super().__init__(title, due_date, ItemStatus.OPEN)
        self._description = description if description else 'No description'

        self.log_event(f'Issue created: {super().info()}')

    @property
    def description(self):
        return self._description

    def info(self):
        return f'Issue ({self._description}) {super().info()}'
