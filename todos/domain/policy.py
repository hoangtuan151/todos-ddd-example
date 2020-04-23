class MaxConcurrencyDoingTaskPolicy:
    def __init__(self, user):
        self._threshold = 3
        self._current_doing_task = user.doing_task
        if user.done_task >= 3:
            self._threshold = 5

    def allow_next_doing_task(self):
        return self._current_doing_task < self._threshold
