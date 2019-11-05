import requests


def bypass_onboard_expert(user_id, access_token):
    url = 'https://api-query.got-it.io/admin/explainers/' + user_id + '/subjects'
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
    print(response.status_code)
