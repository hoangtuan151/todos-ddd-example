from unittest import mock


# @mock.patch('todos.usecases.task_uc.TaskUC')
def test_get_user_task_list(test_client):
    # task_uc_mock().get_task_list.return_value = ['a', 'b']
    response = test_client.get('/tasks', headers={'Authorization': 'joe'})
    assert response.status_code == 200
    # task_uc_mock().get_task_list.assert_called_with('joe')
    #
    # !!!!! NOT PRODUCTIVE !!!!!
    #
