import uuid
from todos.domain.task import Task


def test_task__model_init():
    tid = uuid.uuid4()
    desc = 'A new task'
    task = Task(tid, desc)

    assert task.tid == tid
    assert task.desc == desc
