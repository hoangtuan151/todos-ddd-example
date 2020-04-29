from pymongo import MongoClient
from todos.domain.task import Task
from todos.domain.user import User


class MongoRepos:
    def __init__(self, connect_uri):
        self._mongo_client = MongoClient(connect_uri)
        self.mongo_col = self._mongo_client.get_database('todos').get_collection('user')

    def create_task_for_user(self, username, new_task):
        task_obj = {
            'id': new_task.tid,
            'desc': new_task.desc,
            'state': new_task.state,
            'emergency': new_task.emergency
        }

        result = self.mongo_col.update_one(
            {
                'username': username
            }, {
                '$setOnInsert': {
                    'username': username
                },
                '$addToSet': {
                    'tasks': task_obj
                }
            },
            upsert=True
        )
        print(
            '[create_task_for_user]',
            'update_one: matched_count', result.matched_count,
            '- modified_count', result.modified_count,
            '- upserted_id', result.upserted_id
        )

    def get_tasks_by_username(self, username):
        doc = self.mongo_col.find_one(
            {
                'username': username
            }, {
                '_id': 0, 'tasks': 1
            }
        )
        task_list = doc.get('tasks', [])

        result = []
        for item in task_list:
            result.append(Task(
                item['id'],
                item['desc'],
                item['state'],
                item['emergency']
            ))
        return result

    def find_by_id(self, task_id):
        doc = self.mongo_col.find_one(
            {
                'tasks.id': task_id
            }, {
                'tasks': {
                    '$elemMatch': {'id': task_id}
                }
            }
        )
        task_obj = doc['tasks'][0]
        return Task(
            task_obj['id'],
            task_obj['desc'],
            task_obj['state'],
            task_obj['emergency']
        )

    def find_user_by_username(self, username):
        doc = self.mongo_col.find_one({'username': username}, {'_id': 0})

        user = User(username)
        user.done_task = doc.get('done', 0)
        user.doing_task = doc.get('doing', 0)
        return user

    def mark_task_as_doing(self, username, task_id):
        self.mongo_col.update_one(
            {
                'username': username,
                'tasks.id': task_id
            }, {
                '$set': {
                    'tasks.$.state': 'DOING'
                },
                '$inc': {
                    'doing': 1
                }
            }
        )

    def mark_task_as_done(self, username, task_id):
        self.mongo_col.update_one(
            {
                'username': username,
                'tasks.id': task_id
            }, {
                '$set': {
                    'tasks.$.state': 'DONE'
                },
                '$inc': {
                    'done': 1,
                    'doing': -1
                }
            }
        )
