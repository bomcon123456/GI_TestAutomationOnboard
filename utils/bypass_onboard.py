import requests

from configs import API_EXPLAINER_URL


def bypass_onboard_expert(user_id, access_token):
    url = API_EXPLAINER_URL + user_id + '/subjects'
    data = {
        'subjects': [
            {
                'subject_id': 1006
            }
        ]
    }
    headers = {
        'Authorization': 'Bearer ' + access_token,
        'x-gotit-vertical': 'query'
    }
    response = requests.put(url, json=data, headers=headers)
    assert response.status_code == 200
