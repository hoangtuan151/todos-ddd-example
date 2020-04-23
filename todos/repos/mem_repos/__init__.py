class MemRepos:
    def __init__(self):
        self._memory = {}

    def create_task_for_user(self, username, new_task):
        if username not in self._memory:
            self._memory[username] = []
        self._memory[username].append(new_task)

    def get_tasks_by_username(self, username):
        if username not in self._memory:
            return []
        else:
            return self._memory[username]
