import os
import json
import requests
from googlesearch import search


def generate_smart_reply(text):
    if text in ["/start", "/start@zappru_bot"]:
        bot_welcome = """
        Welcome to Codelocker bot!!!!
       """
        return bot_welcome
    elif text in ["/servertime", "/servertime@zappru_bot"]:
        return os.popen('date').read()  
    elif text in ["/listfile", "/listfile@zappru_bot"]:
        return os.popen('ls -lart').read()
    elif text in ["/detail", "/detail@zappru_bot"]:
        return os.popen('uname').read()
    elif text.split(' ')[0] in ['/hello', "/hello@zappru_bot"]:
        string = ' '.join(text.split(' ')[1:])
        return f"Bonjour my Friend { string }"
    elif text.split(' ')[0]  in ['/search', "/search@zappru_bot"]:
        for i in search(' '.join(text.split(' ')[1:]), tld="com", num=10, stop=1, pause=2):
            return i 
    elif text.strip().split(' ')[0] == "/get":
        if len(text.strip().split(' ')) == 1:
            return """/get btc or eth"""
        else:
            response = requests.get(f"https://data.messari.io/api/v1/assets/{text.split(' ')[1].lower()}/metrics").text
            return float([ i for i in json.loads(response).values()][1].get('market_data')['price_usd'])
    

    elif text in ["/help", "/help@zappru_bot"]:
        return """
    You can control me by sending these commands: 
    
    /help   - To get command 
    /start  - Codelocker Bot

    Server Details:
    /servertime   - to get Server time and date         
    /listfile     - list out files on server   
    /detail       - server details   
    /hello        - Test command
    
    Google Details     
    /search "String to be search" - To get top result
    
    CRYPTO Market prise:
    /get btc or eth - To get crypto value
    """  
    else:
        return "AI chat BOT is Under construction!! Please contact my Creator Raahool Kumeriya"

## Testing Bot at localhost
# if __name__ == "__main__":
#     while True:    
#         option = input("Enter reponse ")
#         if option == "Q":
#             import sys
#             sys.exit()
#         else:
#             print(option)
#             print(generate_smart_reply(option))
