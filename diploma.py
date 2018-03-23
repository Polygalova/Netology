import requests
import time
import json
import os


def call_vk(method, params):
    params['access_token'] = '430bbae2070f1d2248b167ec0557344c8edf8b8b2b081e869dc128e1ae7f05e8cc15a7b644ed6c07b1326'
    params['version'] = '5.73'
    url = os.path.join('https://api.vk.com/method/', method)
    response = requests.get(url, params)
    if 'error' in response:
        print('Ошибка!', response.json()['error']['error_msg'])
        return False
    else:
        return response.json()['response']


def get_user_id(name_or_id):
    '''Проверяем, существует ли пользователь и возвращаем его id, если он существует'''
    params = {'user_ids': name_or_id}
    try:
        user = call_vk('users.get', params)[0]
        if user:
            if 'deactivated' not in user:
                num = user['uid']
                return num
            else:
                print('Пользователь с таким именем или номером удален или заблокирован')
    except:
        print('Пользователь с таким именем или номером не существует')
        return False


def get_friends(user_id):
    '''Получаем список друзей пользователя'''
    params = {'user_id': user_id}
    return call_vk('friends.get', params)


def get_groups(user_id):
    '''Получаем список групп пользователя, возвращаем в виде множества'''
    params = {'user_id': user_id}
    try:
        return set(call_vk('groups.get', params))
    except:
        return set()


def find_unique(user_id):
    '''Получаем множество id групп целевого пользователя и список id его друзей.
     Далее собираем множество всех групп всех друзей и возвращаем разность двух множеств
     '''
    user_groups = get_groups(user_id)
    friends_groups = set()
    friends_ids = get_friends(user_id)
    if friends_ids:
        quantity = len(friends_ids)
        for friend_id in friends_ids:
            print('Осталось обработать {} друзей'. format(quantity))
            friends_groups |= get_groups(friend_id)
            time.sleep(0.26)
            quantity -= 1
    return user_groups - friends_groups


def get_groups_info(group_ids):
    '''По заданным id групп получаем их описания, отбираем действующие группы
    и приводим описания к тебуемому виду'''
    params = {
        'group_ids': ','.join(list(map(str, list(group_ids)))),
        'fields': 'members_count',
        }
    try:
        dirty_dict_of_groups = call_vk('groups.getById', params)
        group_list_of_clean_dicts = []
        for group in dirty_dict_of_groups:
            if 'deactivated' not in group:
                clean_dict = {'name': group['name'], 'gid': group['gid'], 'members_count': group['members_count']}
                group_list_of_clean_dicts.append(clean_dict)
        return group_list_of_clean_dicts
    except:
        return False


def get_and_write_json_unique_groups():
    '''Собираем итоговый список и пишем его в файлик'''
    user = input('Введите id пользователя или экранное имя: ')
    user_id = get_user_id(user)
    if user_id:
        result_group_ids = find_unique(user_id)
        list_for_json = get_groups_info(result_group_ids)
        with open('found_groups.json', 'w', encoding='utf-8') as f:
            json.dump(list_for_json, f, ensure_ascii=False, indent=4)
            print('found_groups.json создан')
    return


get_and_write_json_unique_groups()
