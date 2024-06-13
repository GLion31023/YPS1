from task_board.board_items.board_item import BoardItem
from task_board.board_items.item_status import ItemStatus
from task_board.user.user import User


class Board:
    def __init__(self):
        self._items = []
        self._users = []

    @property
    def items(self):
        return tuple(self._items)

    @property
    def users(self):
        return tuple(u.username for u in self._users)

    @property
    def count_items(self):
        return len(self._items)

    @property
    def team_capacity(self):
        return sum(u.capacity for u in self._users)

    def add_item(self, item: BoardItem):
        if item in self._items:
            raise ValueError('Item has already been added to the Board')

        self._items.append(item)

    def add_user(self, username, email):
        usernames = [u.username for u in self._users]

        if username in usernames:
            raise ValueError(f'User with username {username} already exists')

        user = User(username, email)
        self._users.append(user)
        return user

    def reassign_task(self, task, user):
        tasks = [t.title for t in self._items]
        current_assignee = task.assignee

        if task.title not in tasks:
            raise ValueError(f'Task {task.title} does not exist')

        if task.assignee.username == user.username:
            raise ValueError(f'Cannot assign tasks to yourself')

        current_assignee.remove_task(task)
        if task.status == ItemStatus.IN_PROGRESS:
            task.revert_status()

        user.receive_task(task)
        task.assignee = user
