from pytest import fixture
from unittest.mock import Mock
import uuid
from todos.domain.task import Task
from todos.usecases.task_uc import TaskUC


@fixture
def domain_task_list():
    return [
        Task(uuid.uuid4(), 'Task 1'),
        Task(uuid.uuid4(), 'Task 2'),
        Task(uuid.uuid4(), 'Task 3')
    ]


@fixture
def current_username():
    return 'johndoe'


def test_task_uc__get_task_list(domain_task_list, current_username):
    task_repo = Mock()
    task_repo.get_tasks_by_username.return_value = domain_task_list

    task_uc = TaskUC(task_repo=task_repo)
    result = task_uc.get_task_list(current_username)

    task_repo.get_tasks_by_username.assert_called_with(current_username)
    assert result == domain_task_list
