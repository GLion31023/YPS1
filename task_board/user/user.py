from task_board.event_logging.event_log import EventLog
from task_board.board_items.item_status import ItemStatus


def check_valid_email(email):
    if '@' not in email:
        raise ValueError("Invalid email address")


class User:
    def __init__(self, username: str, email: str):
        check_valid_email(email)
        self._username = username
        self._email = email
        self._assigned_tasks = []
        self._history = []

        self.log_event(f'User created: Username: {self._username}, email: {self._email}')

    @property
    def username(self):
        return self._username

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        check_valid_email(value)
        self.log_event(f'Email changed from {self.email} to {value}')

        self._email = value

    @property
    def assigned_tasks(self):
        return tuple(self._assigned_tasks)

    @property
    def capacity(self):
        return 3 - len(self._assigned_tasks)

    def advance_task_status(self, task):
        prev = task.status
        if task.assignee.username != self._username:
            raise ValueError(f'Task is not assigned to user {self._username}, therefore cannot advance status')

        task.advance_status()
        self.log_event(f"User {self._username} advanced task's ({task.title}) status from -{prev}- to -{task.status}-")

        if task.status == ItemStatus.DONE:
            self._assigned_tasks.remove(task)
        self.log_event(f"User {self._username} completed task ({task.title}). Available capacity: {self.capacity}")

    def receive_task(self, task):
        if self.capacity == 0:
            raise ValueError(f'Unable to assign task. User {self._username} has reached their max capacity')

        if task.status not in [ItemStatus.TODO, ItemStatus.IN_PROGRESS]:
            raise ValueError(f'Only tasks on status -Todo- or -In progress- can be assigned to users')

        self._assigned_tasks.append(task)
        self.log_event(f"User {self._username} received task: '{task.title}' on status -{task.status}-."
                       f" {self._username}'s available capacity {self.capacity}")

    def remove_task(self, task):
        tasks = [t.title for t in self._assigned_tasks]

        if task.title not in tasks:
            raise ValueError(f'Task {task.title} not assigned to user {self._username}')

        idx = tasks.index(task.title)
        self._assigned_tasks.pop(idx)
        self.log_event(f'Task {task.title} removed from user {self._username} on status {task.status}.'
                       f' Available capacity {self.capacity}')

    def info(self):
        tasks = "\n".join(t.title for t in self._assigned_tasks)
        return f'Username: {self._username}, email: {self._email}, tasks:{tasks}'

    def history(self):
        return f'\n'.join(e.info() for e in self._history)

    def log_event(self, description):
        self._history.append(EventLog(description))
