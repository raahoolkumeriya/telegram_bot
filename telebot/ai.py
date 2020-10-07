import os
import json
import requests
from googlesearch import search


def generate_smart_reply(text):
    if text == "/start":
        bot_welcome = """
        Welcome to Codelocker bot!!!!
       """
        return bot_welcome
    elif text == "/servertime":
        return os.popen('date').read()  
    elif text == "/listfile":
        return os.popen('ls -lart').read()
    elif text == "/detail":
        return os.popen('uname').read()
    elif text =='/hello':
        return "Say hello to Rahul"
    elif text.split(' ')[0]  == '/search':
        for i in search(' '.join(text.split(' ')[1:]), tld="com", num=10, stop=1, pause=2):
            return i 
    # elif text.strip().split(' ')[0] == "/get":
    #     if len(text.strip().split(' ')) == 1:
    #         return """/get MECUSDT or ETHUSDT"""
    #     else:
    #         response = requests.get('https://api.nosdaq.com/openapi/quote/v1/ticker/price').text
    #         return float([ i for i in json.loads(response) if text.split(' ')[1].upper() in i.values()][0]["price"])
    
    elif text.strip().split(' ')[0] == "/mecusdt":
        response = requests.get('https://api.nosdaq.com/openapi/quote/v1/ticker/price').text
        return float([ i for i in json.loads(response) if 'MECUSDT' in i.values()][0]["price"])
    
    elif text.strip().split(' ')[0] == "/ethusdt":
        response = requests.get('https://api.nosdaq.com/openapi/quote/v1/ticker/price').text
        return float([ i for i in json.loads(response) if 'ETHUSDT' in i.values()][0]["price"])
    

    elif text == "/help":
        return """
    You can control me by sending these commands: 
    
    /help - To get command 
    /start - Codelocker Bot

    Server Details:
    /servertime - to get Server time and date         
    /listfile - list out files on server   
    /detail - server details   
    /hello - Test command
    
    Google Details     
    /search "String to be search"
    
    NOSDAQ
    /mecusdt
    /ethusdt
    """  
    else:
        return "AI chat BOT is Under construction!! Please contact my Creator Raahool Kumeriya"

# if __name__ == "__main__":
#     while True:    
#         option = input("Enter reponse ")
#         if option == "Q":
#             import sys
#             sys.exit()
#         else:
#             print(option)
#             print(generate_smart_reply(option))
