from task_board.board.board import Board
from task_board.board.can_add_item import CanAddItem
from task_board.board.can_remove_item import CanRemoveItem


class EditableBoard(Board, CanAddItem, CanRemoveItem):
    pass
