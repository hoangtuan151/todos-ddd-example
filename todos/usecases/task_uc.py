from todos.domain.task import Task
from todos.domain.policy import MaxConcurrencyDoingTaskPolicy
import uuid


class TaskUC:
    def __init__(self, task_repo, user_repo=None):
        self._task_repo = task_repo
        self._user_repo = user_repo

    def create_task(self, username, desc, emergency=0):
        tid = str(uuid.uuid4())
        new_task = Task(tid, desc, emergency=emergency)
        self._task_repo.create_task_for_user(username, new_task)
        return new_task

    def get_task_list(self, username):
        return self._task_repo.get_tasks_by_username(username)

    def mark_task_as_doing(self, username, task_id):
        user = self._user_repo.find_user_by_username(username)
        task = self._task_repo.find_by_id(task_id)
        management_policy = MaxConcurrencyDoingTaskPolicy(user, task)
        if management_policy.allow_next_doing_task():
            self._task_repo.mark_task_as_doing(username, task_id)
        else:
            raise Exception('Over threshold')

    def mark_task_as_done(self, username, task_id):
        self._task_repo.mark_task_as_done(username, task_id)
