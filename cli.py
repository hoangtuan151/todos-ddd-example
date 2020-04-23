import sys
import traceback
from todos.domain.task import Task
from todos.repos.mem_repos import MemRepos
from todos.usecases.task_uc import TaskUC

REPO = MemRepos()
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
    print(BCOLORS.PURPLE + USER + '\'s task_list:')
    for task in task_list:
        print(BCOLORS.PURPLE + '- ' + str(task))


def add_task():
    print('Enter task\'s description:')
    desc = sys.stdin.readline()
    desc = desc.strip()

    task_uc = TaskUC(REPO)
    result = task_uc.create_task(USER, desc)
    print(BCOLORS.PURPLE + 'created:', result)


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

    print('-' * 25)


def get_command():
    print(BCOLORS.OKGREEN + '\n#Your next CMD:' + BCOLORS.ENDC)
    cmd = sys.stdin.readline()
    try:
        return int(cmd)
    except:
        return 0


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
            # elif cmd == 4:
            #     testKeepaliveRequest()
            # elif cmd == 5:
            #     Conn.close()
            #     print 'Connection CLOSED'
            # elif cmd == 6:
            #     testDisplayRequest()
            # elif cmd == 7:
            #     startKeepAliveThread()
        except:
            print('>>>>>>>>> Exception <<<<<<<<<')
            traceback.print_exc()
