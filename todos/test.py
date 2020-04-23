from todos.domain.task import Task
from todos.repos.mem_repos import MemRepos
from todos.usecases.task_uc import TaskUC
from todos.domain.user import User


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


def test3():
    u = User('john')
    print(u)
    u.done_task = 10
    u.doing_task = 20
    print(u.done_task)
    print(u.doing_task)
    print(u)


def test4():
    repo = MemRepos()
    task_uc = TaskUC(repo, repo)

    result = task_uc.create_task('john', 'new task')
    task_uc.mark_task_as_doing('john', result.tid)
    task_list = task_uc.get_task_list('john')
    print('task_list:', [str(task) for task in task_list])

    task2 = task_uc.create_task('john', 'task 2')
    task3 = task_uc.create_task('john', 'task 3')
    task_uc.mark_task_as_doing('john', task2.tid)
    task_uc.mark_task_as_doing('john', task3.tid)
    task_list = task_uc.get_task_list('john')
    print('task_list:', [str(task) for task in task_list])

    task4 = task_uc.create_task('john', 'task 4')
    task_uc.mark_task_as_doing('john', task4.tid)
