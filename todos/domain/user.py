class User:
    def __init__(self, username):
        self._username = username
        self._total_done_task = 0
        self._total_doing_task = 0

    @property
    def done_task(self):
        return self._total_done_task

    @done_task.setter
    def done_task(self, num):
        self._total_done_task = num

    @property
    def doing_task(self):
        return self._total_doing_task

    @doing_task.setter
    def doing_task(self, num):
        self._total_doing_task = num

    def __str__(self):
        return 'Task(User: {0}, done: {1}, doing: {2})'.format(
            self._username,
            self._total_done_task,
            self._total_doing_task
        )
