class Task:
    def __init__(self, tid, desc, state=None):
        self._tid = tid
        self._desc = desc
        self._state = state if state is not None else 'NEW'

    def __str__(self):
        return 'Task(tid: {0}, state: {1}, desc: {2})'.format(
            self._tid,
            self._state,
            self._desc
        )
