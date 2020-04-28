import json

from flask import Flask
from flask import Response
from json import dumps, JSONEncoder
from flask import request
from todos.repos.sqlite_repos import SQLiteRepos
from todos.repos.mongo_repos import MongoRepos
from todos.usecases.task_uc import TaskUC

# REPO = SQLiteRepos('./sqlitedb/sqlite.db')
REPO = MongoRepos(connect_uri='mongodb+srv://dev_user:shWYBWKhiKXshWfi@mg-clt-itpr5-0104-c9eww.azure.mongodb.net')
app = Flask(__name__)


def flask_response(result=None, status=200, mimetype='application/json'):
    if type(result) in [dict, list]:
        resp = Response(dumps(result), status=status, mimetype=mimetype)
    elif type(result) in [str]:
        resp = Response(result, status=status, mimetype=mimetype)
    else:
        if mimetype == 'application/json':
            resp = Response('{}', status=status, mimetype=mimetype)
        else:
            resp = Response(result, status=status, mimetype=mimetype)

    return resp


def auth_check():
    auth_header = request.headers['Authorization']
    token = auth_header.replace('Bearer ', '')
    return token


class TaskJsonEncoder(JSONEncoder):
    def default(self, o):
        try:
            return {
                'taskid': o.tid,
                'description': o.desc,
                'status': o.state,
                'emergency': True if o.emergency == 1 else False
            }
        except AttributeError:
            return super().default(o)


@app.route('/tasks', methods=['GET'])
def api_get_all_tasks():
    username = auth_check()
    task_uc = TaskUC(REPO)
    task_list = task_uc.get_task_list(username)
    result = json.dumps(task_list, cls=TaskJsonEncoder)
    return flask_response(result)


@app.route('/tasks', methods=['POST'])
def api_new_task():
    username = auth_check()
    req_body = request.json
    description = req_body['description']
    emergency = req_body.get('emergency', 0)

    task_uc = TaskUC(REPO)
    result = task_uc.create_task(username, description, emergency)
    return flask_response(json.dumps(result, cls=TaskJsonEncoder))


@app.route('/tasks/<task_id>/status', methods=['PUT'])
def api_update_task_status(task_id):
    username = auth_check()
    req_body = request.json
    new_status = req_body['status']

    try:
        task_uc = TaskUC(REPO, REPO)
        if new_status == 1:
            task_uc.mark_task_as_doing(username, task_id)
        elif new_status == 2:
            task_uc.mark_task_as_done(username, task_id)
        return flask_response('SUCCESS', mimetype='text/plain')
    except Exception as e:
        return flask_response(str(e), mimetype='text/plain')
