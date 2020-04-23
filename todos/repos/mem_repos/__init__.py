from todos.domain.user import User


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

    def find_user_by_username(self, username):
        tasks = self.get_tasks_by_username(username)
        done_count = 0
        doing_count = 0
        for task in tasks:
            if task.is_done():
                done_count += 1
            elif task.is_doing():
                doing_count += 1

        user = User(username)
        user.doing_task = doing_count
        user.done_task = done_count
        return user

    def mark_task_as_doing(self, username, task_id):
        tasks = self.get_tasks_by_username(username)
        for task in tasks:
            if task.tid == task_id:
                task.mark_doing()
                break

    def mark_task_as_done(self, username, task_id):
        tasks = self.get_tasks_by_username(username)
        for task in tasks:
            if task.tid == task_id:
                task.mark_done()
                break
