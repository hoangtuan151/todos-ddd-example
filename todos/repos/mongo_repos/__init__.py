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
