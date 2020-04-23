from todos.domain.task import Task
import uuid


class TaskUC:
    def __init__(self, task_repo):
        self._task_repo = task_repo

    def create_task(self, username, desc):
        tid = str(uuid.uuid4())
        new_task = Task(tid, desc)
        self._task_repo.create_task_for_user(username, new_task)
        return new_task

    def get_task_list(self, username):
        return self._task_repo.get_tasks_by_username(username)
