class MaxConcurrencyDoingTaskPolicy:
    def __init__(self, user, task):
        self._current_doing_task = user.doing_task

        self._threshold = 3 if not task.is_emergency() else 4
        if user.done_task >= 3:
            self._threshold = 5

    def allow_next_doing_task(self):
        return self._current_doing_task < self._threshold
