from collections import defaultdict

import requests
import asyncio


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


async def get_one_users_id_api(chat_id):
    response = requests.get('http://127.0.0.1:8000/tg-users/')
    number = 0
    for user in response.json():
        if user['chat_id'] == chat_id:
            number = user['id']
    return number


async def get_foods_of_category_api(id):
    response = requests.get(f'http://127.0.0.1:8000/categories/{id}/foods/')
    return response.json()


async def get_food_photo(id):
    response = requests.get(f'http://127.0.0.1:8000/foods/{id}/')
    return requests.get(response.json()['image']).content


async def get_food_detail_api(id):
    response = requests.get(f'http://127.0.0.1:8000/foods/{id}/')
    return response.json()


async def set_photo_caption_api(id):
    text = ""
    response = await get_food_detail_api(id)
    try:
        text += response['name']
        text += '\n\n'
        text += str(response['price'])
        text += '\n\n'
        text += response['description']
    except KeyError:
        text += 'not content'
    return text


async def add_to_basket_api(user, amount, food):
    data = {
        'amount': amount,
        'telegram_user': user,
        'food': food,
    }
    response = requests.post('http://127.0.0.1:8000/basket/', data=data)
    return response


async def get_user_basket_api(chat_id):
    user_id = await get_one_users_id_api(chat_id)
    response = requests.get('http://localhost:8000/basket/')
    filtered_foods = [item for item in response.json() if item['telegram_user'] == user_id]
    food_ids_to_amount = {item['food']: item['amount'] for item in filtered_foods}
    return food_ids_to_amount


async def get_food_of_basket(chat_id):
    ids = await get_user_basket_api(chat_id)
    foods_list = []
    for id in ids:
        response = requests.get(f'http://localhost:8000/foods/{id}/')
        food_data = response.json()
        food_data['quantity'] = ids[id]
        foods_list.append(food_data)
    return foods_list


async def get_basket_summary(chat_id):
    basket_items = await get_food_of_basket(chat_id)
    food_quantities = {}
    total_price = 0
    for item in basket_items:
        food_name = item['name']
        quantity = item['quantity']
        price_per_item = item['price']
        item_price = quantity * price_per_item
        if food_name in food_quantities:
            food_quantities[food_name] += quantity
        else:
            food_quantities[food_name] = quantity
        total_price += item_price
    response_message = "Savatda:\n\n"
    for food_name, quantity in food_quantities.items():
        response_message += f"{quantity}️⃣ ✖️ {food_name}\n"
    response_message += f"\ntotal:    {total_price} so'm"
    return response_message


async def get_user_basket_ids(chat_id):
    ids = []
    user_id = await get_one_users_id_api(chat_id)
    respponse = requests.get('http://localhost:8000/basket/')
    for order in respponse.json():
        if order['telegram_user'] == user_id:
            ids.append(order['id'])
    return ids


async def empty_basket(chat_id):
    ids = await get_user_basket_ids(chat_id)
    for id in ids:
        requests.delete(f'http://localhost:8000/basket/{id}/')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    print(loop.run_until_complete(get_user_basket_ids(5062242028)))
