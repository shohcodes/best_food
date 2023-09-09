# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
#
#
# def foods_button(id):
#     inline_keyboard = InlineKeyboardMarkup(row_width=2)
#     inline_keyboard.add(InlineKeyboardButton('zokir', callback_data='q'),
#                         InlineKeyboardButton('zokirjon', callback_data='a'))
#     return inline_keyboard
#
#
# if __name__ == '__main__':
#     print(foods_button(1))
#


data = 'lavashlar_3'
print(data.split('_')[1])

# clicked_button_name = None
# for button in callback.message.reply_markup.inline_keyboard:
#     if button["callback_data"] == callback.data:
#         clicked_button_name = button["text"]
#         break
# button_text = callback.message.reply_markup.inline_keyboard[1][0].text
# b = callback.message.reply_markup.inline_keyboard
# print(b)
# call_data = callback.data
# buttons = callback.message.reply_markup.inline_keyboard[0]  # [0].text
# button_text = None
# for button in buttons:
#     if button.callback_data == call_data:
#         button_text = button.text
#         break
# print(button_text)
# clicked_button_name = None
# for button in callback.message.reply_markup.inline_keyboard[0]:
#     if button["callback_data"] == callback.data:
#         clicked_button_name = button["text"]
#         break