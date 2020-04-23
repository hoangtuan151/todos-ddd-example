import sys
import traceback
from todos.domain.task import Task
from todos.repos.mem_repos import MemRepos
from todos.repos.sqlite_repos import SQLiteRepos
from todos.usecases.task_uc import TaskUC

# REPO = MemRepos()
REPO = SQLiteRepos('./sqlitedb/sqlite.db')
USER = None


class BCOLORS:
    PURPLE = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def login_handler():
    global USER
    print('Enter username:')
    USER = sys.stdin.readline()
    USER = USER.strip()
    print(BCOLORS.PURPLE + 'WELCOME', USER)


def list_tasks():
    task_uc = TaskUC(REPO)
    task_list = task_uc.get_task_list(USER)
    print(BCOLORS.PURPLE + USER + '\'s task list:')
    for task in task_list:
        print(BCOLORS.PURPLE + '- ' + str(task))


def add_task():
    print('Enter task\'s description:')
    desc = sys.stdin.readline()
    desc = desc.strip()

    task_uc = TaskUC(REPO)
    result = task_uc.create_task(USER, desc)
    print(BCOLORS.PURPLE + 'created:', result)


def mark_doing():
    print('Enter task id:')
    task_id = sys.stdin.readline()
    task_id = task_id.strip()

    task_uc = TaskUC(REPO, REPO)
    try:
        task_uc.mark_task_as_doing(USER, task_id)
        print(BCOLORS.PURPLE + 'SUCCESS')
    except Exception as e:
        print(BCOLORS.FAIL + 'Exception:', str(e))


def mark_done():
    print('Enter task id:')
    task_id = sys.stdin.readline()
    task_id = task_id.strip()

    task_uc = TaskUC(REPO)
    task_uc.mark_task_as_done(USER, task_id)
    print(BCOLORS.PURPLE + 'SUCCESS')


def print_command_list():
    print(BCOLORS.BOLD + '+' * 25 + BCOLORS.ENDC)
    print(BCOLORS.BOLD + '+++ TODOS CLI Program'.ljust(25-4, ' '), '+++' + BCOLORS.ENDC)
    if USER:
        print('Welcome', USER)
    print(BCOLORS.BOLD + '+' * 25 + BCOLORS.ENDC)

    print(BCOLORS.OKGREEN + 'Command list:' + BCOLORS.ENDC)
    print('0. Exit')
    print('1. Login by username')
    print('2. List all your tasks')
    print('3. Add task')
    print('4. Mark task doing')
    print('5. Mark task done')

    print('-' * 25)


def get_command():
    print(BCOLORS.OKGREEN + '\n#Enter next command:' + BCOLORS.ENDC)
    cmd = sys.stdin.readline()
    try:
        return int(cmd)
    except:
        return -1


if __name__ == '__main__':
    print_command_list()
    cmd = -1
    while cmd != 0:
        cmd = get_command()
        print('Processing command [%s]' % cmd)
        try:
            if cmd == 1:
                login_handler()
            elif cmd == 2:
                list_tasks()
            elif cmd == 3:
                add_task()
            elif cmd == 4:
                mark_doing()
            elif cmd == 5:
                mark_done()
        except:
            print('>>>>>>>>> Exception <<<<<<<<<')
            traceback.print_exc()
