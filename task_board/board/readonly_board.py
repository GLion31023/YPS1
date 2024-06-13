from task_board.board.board import Board
from task_board.board.can_add_item import CanAddItem


class ReadonlyBoard(Board, CanAddItem):
    pass
