import requests
import time
import json


def get_user_id(name_or_id, token):
    '''Проверяем, существует ли пользователь и возвращаем его id, если он существует'''
    params = {
        'user_ids': name_or_id,
        'access_token': token,
        'version': 5.73
    }
    response = requests.get('https://api.vk.com/method/users.get', params)
    try:
        user = response.json()['response'][0]
        if 'deactivated' not in user.keys():
            num = user['uid']
        else:
            raise Exception
    except:
        print('Пользователь с таким именем или номером удален или не создан')
        return False
    return num


def get_friends(user_id, token):
    '''Получаем список друзей пользователя'''
    params = {
        'access_token': token,
        'user_id': user_id,
        'version': 5.73
        }
    response = requests.get('https://api.vk.com/method/friends.get', params)
    result = response.json()['response']
    return result


def get_groups(user_id, token):
    '''Получаем список групп пользователя, возвращаем в виде множества'''
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
    '''Получаем список id групп целевого пользователя и список id его друзей.
     Далее собираем множество всех групп всех друзей и возвращаем разность двух множеств
     '''
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
    '''По заданным id групп получаем их описания, отбираем действующие группы
    и приводим описания к тебуемому виду'''
    params = {
        'access_token': token,
        'group_ids': ','.join(list(map(str, list(group_ids)))),
        'fields': 'members_count',
        'version': 5.73
        }
    response = requests.get('https://api.vk.com/method/groups.getById', params)
    try:
        dirty_dict_of_groups = response.json()['response']
        group_list_of_clean_dicts = []
        for group in dirty_dict_of_groups:
            if 'deactivated' not in group.keys():
                clean_dict = {'name': group['name'], 'gid': group['gid'], 'members_count': group['members_count']}
                group_list_of_clean_dicts.append(clean_dict)
        result = group_list_of_clean_dicts
    except:
        result = False
    return result


def get_and_write_json_unique_groups():
    '''Собираем итоговый список и пишем его в файлик'''
    token = '278e52e9dc260aa5b15214b1edf6f7de2d78d3fc87936752fc6bff78accea17abb3f87251e9d1dff0f518'
    user = input('Введите id пользователя или экранное имя: ')
    user_id = get_user_id(user, token)
    if user_id:
        result_group_ids = find_unique(user_id, token)
        list_for_json = get_groups_info(result_group_ids, token)
        with open('found_groups.json', 'w', encoding='utf-8') as f:
            json.dump(list_for_json, f, ensure_ascii=False)
            print('found_groups.json создан')
    return


get_and_write_json_unique_groups()
