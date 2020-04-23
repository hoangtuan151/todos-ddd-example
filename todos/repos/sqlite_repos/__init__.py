from todos.domain.user import User
import sqlite3
from sqlite3 import Error


class SQLiteRepos:
    def __init__(self, db_file_path):
        try:
            self._db_conn = sqlite3.connect(db_file_path)
        except Error as e:
            print(e)

    def create_task_for_user(self, username, new_task):
        sql = '''
            INSERT INTO
                Task (id, username, desc, state)
            VALUES(?, ?, ?, ?)
        '''
        param = (new_task.tid, username, new_task.desc, new_task.state)
        cur = self._db_conn.cursor()
        cur.execute(sql, param)
        self._db_conn.commit()
        print('debug sql:', cur.rowcount)

    def get_tasks_by_username(self, username):
        sql = '''SELECT * FROM Task WHERE username = ?'''

        cur = self._db_conn.cursor()
        cur.execute(sql, (username,))

        return cur.fetchall()

    def find_user_by_username(self, username):
        sql = '''
            SELECT
                state, count(id) as num
            FROM
                Task
            WHERE
                username = ?
            GROUP BY
                state
        '''

        cur = self._db_conn.cursor()
        cur.execute(sql, (username,))

        user = User(username)
        for row in cur.fetchall():
            if row[0] == 'DONE':
                user.done_task = row[1]
            elif row[0] == 'DOING':
                user.doing_task = row[1]

        return user

    def mark_task_as_doing(self, username, task_id):
        self._set_task_state(username, task_id, 'DOING')

    def mark_task_as_done(self, username, task_id):
        self._set_task_state(username, task_id, 'DONE')

    def _set_task_state(self, username, task_id, new_state):
        sql = '''UPDATE Task SET state = ? WHERE username = ? and id = ?'''

        cur = self._db_conn.cursor()
        cur.execute(sql, (new_state, username, task_id))

        self._db_conn.commit()
