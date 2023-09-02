import requests


async def register_api(fullname, phone_number, chat_id):
    data = {
        'fullname': fullname,
        'phone_number': phone_number,
        'chat_id': chat_id
    }
    response = requests.post('http://127.0.0.1:8000/tg-users/', data=data)
    return response


async def get_all_chat_ids_api():
    response = requests.get('http://127.0.0.1:8000/tg-users/')
    ids = []
    for id in response.json():
        ids.append(id['chat_id'])
    return ids


async def get_categories_api():
    response = requests.get('http://127.0.0.1:8000/categories/')
    return response.json()


async def my_orders_api(chat_id):
    user_id = await get_one_users_id_api(chat_id)
    response = requests.get('http://127.0.0.1:8000/orders/')
    order = []
    for i in response.json():
        if i['telegram_user'] == user_id:
            order.append(i)
    return order


async def get_one_users_id_api(pk):
    response = requests.get('http://127.0.0.1:8000/tg-users/')
    number = 0
    for user in response.json():
        if user['chat_id'] == pk:
            number = user['id']
    return number


async def get_foods_of_category_api(id):
    response = requests.get(f'http://127.0.0.1:8000/categories/{id}/foods/')
    return response.json()


if __name__ == '__main__':
    print(get_foods_of_category_api(1))
