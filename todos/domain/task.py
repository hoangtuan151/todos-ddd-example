class Task:
    def __init__(self, tid, desc, state=None, emergency=0):
        self._tid = tid
        self._desc = desc
        self._state = state if state is not None else 'NEW'
        self._emergency = emergency

    @property
    def tid(self):
        return self._tid

    @property
    def desc(self):
        return self._desc

    @property
    def state(self):
        return self._state

    @property
    def emergency(self):
        return self._emergency

    def __str__(self):
        return 'Task(tid: {0}, state: {1}, desc: {2}, emergency: {3})'.format(
            self._tid,
            self._state,
            self._desc,
            self._emergency
        )

    def is_done(self):
        return self._state == 'DONE'

    def is_doing(self):
        return self._state == 'DOING'

    def is_emergency(self):
        return self._emergency

    def mark_doing(self):
        self._state = 'DOING'

    def mark_done(self):
        self._state = 'DONE'
