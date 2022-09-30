import telegram.ext as tele
import time
from telegram import *
# from aiogram import InlineKeyboardButton, InlineKeyboardMarkup
import Responses as Resp
import random
import requests


# with open('token.txt', 'r') as f:
#     TOKEN = f.read()
TOKEN = "5739362149:AAGj26fJRtNlT5Ul8Q5Do28tbrUExt7b8oQ"


def start(update,context):
    first_name = update.message.from_user["first_name"]
    update.message.reply_text('''
    Commands:
   /help
   /roastme
   /flirt
   /meme

   Messages:
   Greetings --> hey, hello, hi
   Time
   Location

   Fun:
   how gay / how lesbian / how straight
   how male/ how female / how waifu
    ''')
    print(update.message)


def help(update, context):
    update.message.reply_text("Contact @rupesh_ghimire for any suggestions or help. Thank you for your time.")



def flirt(update, context):
    lines = ''' I'd never play hide and seek with you because someone like you is impossible to find
                Do you have a name or can I call you mine?
                How was heaven when you left it?
                I'm on top of things Would you like to be one of them?
                What time do you have to be back in heaven?
                I'll treat you like my homework: Slam you on the table and do you all night long!
                There are so many types of art but you are my favorite
                You are as beautiful as 1.618
                You know you're in love when you can't fall asleep because reality is finally better than your dreams
                Can I follow you? Cause my mom told me to follow my dreams
                I'd never play hide and seek with you because someone like you is impossible to find
                People are catching Coronavirus but the only thing I'm catching is feelings for you
                Let me tie your shoes, cause I dont want you falling for anyone else
                Roses are red, my face is too, that only happens when I'm around you
                I am going to complain to Spotify about you not being this weeks hottest single
                Roses are red, violets are blue, I'm not that pretty but damn look at you
                You may fall from the sky, you may fall from a tree, but the best way to fall… is in love with me
                Do you have a name or can I call you mine?
                Can I follow you? Cause my mom told me to follow my dreams
                If being in love was illegal, will you be my partner in crime?
                Can I have your picture so I can show Santa what I want for Christmas?
                Even if there wasn't any gravity on earth, I would still fall for you!
                Roses are red violets are blue I didn't know what perfect was until I met you
                Are you a camera? Because every time I look at you, I smile
                Your hand looks heavy can i hold it for you?
                Roses are red, violets are blue, lava is hot and so are you
                Covid 19 cancelling everything, except my feelings for you
                There's only one thing I want to change about you Your last name
                Are you Coronavirus? Because i wouldn't mind spending two weeks in bed with you
                I'm no organ donor but I'd be happy to give you my heart     '''
    lines = lines.split("\n")
    pickup_line = lines[random.randrange(0,30)]
    update.message.reply_text(pickup_line)
 
 

def roastme(update, context):
    lines = ''' My hair straightener is hotter than you.
                I have heels higher than your standards.
                You have more faces than Mount Rushmore
                I'm jealous of people who don't know you.
                You're entitled to your incorrect opinion.
                I'm visualizing duck tape over your mouth.
                You're the reason I prefer animals to people.
                If I had a face like yours, I'd sue my parents.
                I'd smack you, but that would be animal abuse.
                You sound reasonable… Time to up my medication.
                Hey, I found your nose, it's in my business again!
                I might be crazy, but crazy is better than stupid.
                My middle finger gets a boner every time I see you.
                Is there an app I can download to make you disappear?
                90% of your 'beauty' could be removed with a Kleenex.
                The people who know me the least have the most to say.
                I am allergic to stupidity, so I break out in sarcasm.
                I didn't change. I grew up. You should try it sometime.
                My phone battery lasts longer than your relationships.
                I'm sorry that my brutal honesty inconvenienced your ego.
                Some people should use a glue stick instead of chapstick.
                It's scary to think people like you are allowed to vote.'''
    lines = lines.split("\n")
    roast_line = lines[random.randrange(0,22)]
    update.message.reply_text(roast_line)


def meme(update, context):
    response = requests.get('https://meme-api.herokuapp.com/gimme').json()
    url = response.get('url')
    update.message.reply_photo(url)


# button1 = InlineKeyboardButton(text = "How Gay", callback_data ="howgay")
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


# def trivia(update, context):
#     details = []
#     response = requests.get('https://the-trivia-api.com/api/questions').json()
#     # print(response)
#     for element in response:
#         question = element.get('question')
#         print(question)
#         right = element.get('correctAnswer')
#         print(right)
#         wrongs = element.get('incorrectAnswers')
#         print(wrongs)
#         options = []
#         print(options)
#         for wrong in wrongs:
#             print(wrong)
#             options.append(wrong)
#         options.append(right)
#         options.append(question)
#         print(options)

#         buttons = [[KeyboardButton(options.pop(options.index(random.choice(options))))],
#         [KeyboardButton(options.pop(options.index(random.choice(options))))],
#         [KeyboardButton(options.pop(options.index(random.choice(options))))],
#         [KeyboardButton(options.pop(options.index(random.choice(options))))]]  

#         context.bot.send_message(chat_id=update.effective_chat.id, one_time_keyboard = True, resize_keyboard = True , text = question, reply_markup=ReplyKeyboardMarkup(buttons)) 
#         details.append(options)

#     update.message.reply_text("Testing")


# def triviahandler(update, context):
#     # points = 0
#     pass
    # for options in details:
    #     question = options.pop()
    #     print(question)
    #     right = options[-1]
    #     print(right)
    #     wrongs = options[:-1]
    #     print(wrongs)
    #     print(options)
    #     random.shuffle(options)


    #     if update.message.text == right:
    #         points = points + 1
    #         print(points)
    #     update.message.reply_text("Your total point is: "+ points)
    #     print(points)


def message_handler(update,context):
    text = str(update.message.text).lower()
    response = Resp.sampleResponses(text)
    update.message.reply_text(response)


updater = tele.Updater(TOKEN, use_context=True)
disp = updater.dispatcher


#Handlers Here
disp.add_handler(tele.CommandHandler("start", start))
disp.add_handler(tele.CommandHandler("roastme", roastme))
disp.add_handler(tele.CommandHandler("flirt", flirt))
disp.add_handler(tele.CommandHandler("help", help))
disp.add_handler(tele.MessageHandler(tele.Filters.text, message_handler))
# disp.add_handler(tele.CommandHandler('trivia', trivia))
# disp.add_handler(tele.MessageHandler(tele.Filters.text, triviahandler))
disp.add_handler(tele.CommandHandler("meme", meme))


updater.start_polling()
updater.idle()