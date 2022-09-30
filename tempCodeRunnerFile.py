button1 = InlineKeyboardButton(text = "How Gay", callback_data ="howgay")
# button2 = InlineKeyboardButton(text = "How Lesbian", callback_data ="howlesbian")
# button3 = InlineKeyboardButton(text = "How Straight", callback_data ="howstraight")
# button4 = InlineKeyboardButton(text = "How Male", callback_data ="howmale")
# button5 = InlineKeyboardButton(text = "How Female", callback_data ="howfemale")
# button6 = InlineKeyboardButton(text = "How Waifu", callback_data ="waifu")

# keyboard_inline = InlineKeyboardMarkup().add(button1,button2,button3).add(button4,button5,button6)


# @dp.message_handler(command = ["how"])
# async def response_how(message: types.Message):
#     await message.reply("%Rating: ", reply_markup = keyboard_inline)

# @dp.callback_query_handler(text = ["howgay", "howstraight","howlesbian","howmale","howfemale","waifu"])
# async def random_percent(call:types.CallbackQuery):
#     if call.data == "howgay":
#         await call.message.answer("You are:"+ random.randint(1, 100) + "% Gay.")

#     elif call.data == "howlesbian":
#         await call.message.answer("You are:"+ random.randint(1, 100) + "% Lesbian.")

#     elif call.data == "howstraight":
#         await call.message.answer("You are:"+ random.randint(1, 100) + "% Straight.")

#     elif call.data == "howmale":
#         await call.message.answer("You are:"+ random.randint(1, 100) + "% Male.")

#     elif call.data == "howfemale":
#         await call.message.answer("You are:"+ random.randint(1, 100) + "% Female.")

#     elif call.data == "waifu":
#         await call.message.answer("You are:"+ random.randint(1, 100) + "% Waifu.")
#     await call.answer()