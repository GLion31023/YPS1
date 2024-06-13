from task_board.board_items.board_item import BoardItem


class CanRemoveItem:
    def remove_item(self, item: BoardItem):
        items = [i.title for i in self._items]
        if item.title not in items:
            raise ValueError(f'Item does not exists')

        idx = items.index(item.title)
        self._items.pop(idx)
