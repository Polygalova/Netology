import requests
import time
import json


def get_friends(user_id, token):
    params = {
        'access_token': token,
        'user_id': user_id,
        'version': 5.73
        }
    response = requests.get('https://api.vk.com/method/friends.get', params)
    try:
        result = response.json()['response']
    except:
        print('Пользователь удален, заблокирован или не создан')
        result = False
    return result


def get_groups(user_id, token):
    params = {
        'access_token': token,
        'user_id': user_id,
        'extended': 0,
        'version': 5.73
        }
    response = requests.get('https://api.vk.com/method/groups.get', params)
    try:
        result = set(response.json()['response'])
    except:
        result = set()
    return result


def find_unique(user_id, token):
    user_groups = get_groups(user_id, token)
    friends_groups = set()
    friends_ids = get_friends(user_id, token)
    if friends_ids:
        quantity = len(friends_ids)
        for friend_id in friends_ids:
            print('Осталось обработать {} друзей'. format(quantity))
            friends_groups |= get_groups(friend_id, token)
            time.sleep(0.26)
            quantity -= 1
    return user_groups - friends_groups


def get_groups_info(group_ids, token):
    params = {
        'access_token': token,
        'group_ids': ','.join(list(map(str, list(group_ids)))),
        'fields': 'members_count',
        'version': 5.73
        }
    response = requests.get('https://api.vk.com/method/groups.getById', params)
    try:
        dirty_groups = response.json()['response']
        group_list_of_clean_dicts = []
        for group in dirty_groups:
            if 'deactivated' not in group.keys():
                clean_dict = {'name': group['name'], 'gid': group['gid'], 'members_count': group['members_count']}
                group_list_of_clean_dicts.append(clean_dict)
        result = group_list_of_clean_dicts
    except:
        result = False
    return result


def get_user_id(screen_name, token):
    params = {
        'user_ids': screen_name,
        'access_token': token,
        'version': 5.73
    }
    response = requests.get('https://api.vk.com/method/users.get', params)
    try:
        num = response.json()['response'][0]['uid']
    except:
        print('Пользователя с таким именем нет')
        return False
    return num


def get_and_write_json_unique_groups():
    token = '610c39bd318cf194aad8ac01c77aea627eacc280e70f9b2091be8e8d5261fe150e6b4dfa889410e210085'
    user_id = input('Введите id пользователя или экранное имя: ')
    if not user_id.isdigit():
        user_id = get_user_id(user_id, token)
    if user_id:
        result_group_ids = find_unique(user_id, token)
        list_for_json = get_groups_info(result_group_ids, token)
        with open('found_groups.json', 'w', encoding='utf-8') as f:
            json.dump(list_for_json, f, ensure_ascii=False)
            print('found_groups.json создан')
    return


get_and_write_json_unique_groups()
