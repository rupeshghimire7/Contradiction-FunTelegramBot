from datetime import datetime
import re
import random


def sampleResponses(inputText):
    user_message  = str(inputText).lower()
    print(user_message)

    if user_message in ["hey", "hello", "hi" ]:
        return "Hey! How is it going?"

    if user_message in ["good", "nice", "as usual" ]:
        return "Great! Way to go."
    
    if user_message in ["time", "what time is it now", "tell me time" ]:
        now =  datetime.now()
        now = now.strftime("%d/%m%y, %H:%M:%S")
        return str(now)

    if user_message in ["Location", "location", "my location"]:
        return "My bed or my heart. As you wish. ^_~"
    

    if user_message in [r"how gay", r"how lesbian", r"how straight", r"how male", r"how female", r"how waifu"]:
        return f"You are {random.randint(0,100)} % {user_message[4:]}"

    if user_message in [r"love you"]:
        return f"Love you too. Know that you are special and precious."

    return("I don't understand you. Please use commands and messages as specified in /start ")