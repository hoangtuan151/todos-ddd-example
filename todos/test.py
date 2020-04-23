from todos.domain.task import Task
from todos.repos.mem_repos import MemRepos
from todos.usecases.task_uc import TaskUC


def test1():
    t = Task('123', 'new task')
    print(t)


def test2():
    repo = MemRepos()
    task_uc = TaskUC(repo)
    task_uc.create_task('john', 'new task')
    task_uc.create_task('john', 'second task')
    task_list = task_uc.get_task_list('john')
    print('task_list:', [str(task) for task in task_list])
