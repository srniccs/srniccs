from datetime import datetime, timedelta #
import json,requests #
from telebot.types import InlineKeyboardMarkup
import random #
import telebot #
import json,requests #
import time #
import bd #
from pytz import timezone #

api_key = "6863376501:AAEGsa-iq4avZMSSLNuCQpS40_uKwEY1g-Q"
chat_id = "-1001959341671"

LINK_SITE = '[👉🏻 ENTRE AQUI NO JOGO 👈🏻](https://betw.com/r/96qbvdC3)'

bot = telebot.TeleBot(token=api_key)

def ALERT_GALE1():
        tz = timezone('America/Sao_Paulo')
        now = datetime.now(tz)
        h = datetime.now().hour
        m = datetime.now().minute+1
        s = datetime.now().second

        if m > 59:
            h += 1
            m = 0

        if h <= 9:
            h = f'0{h}'
        if m <= 9:
            m = f'0{m}'
        if s <= 9:
            s = f'0{s}'
        message_id = bot.send_message(chat_id=chat_id, text=f'''
        𝙉𝙊𝙑𝘼 𝙊𝙋𝙊𝙍𝙏𝙐𝙉𝙄𝘿𝘼𝘿𝙀 𝙀𝙈 {h}:{m}:{s} 𝙂𝙀𝙍𝘼𝙉𝘿𝙊 𝙀𝙉𝙏𝙍𝘼𝘿𝘼... ''').message_id
        bd.message_ids1 = message_id
        time.sleep(15)
        bd.mensage_delete1 = True
        return  

def DELET_GALE1():
        if bd.mensage_delete1 == True:
            bot.delete_message(chat_id=chat_id, message_id=bd.message_ids1)
            bd.mensage_delete1 = False

while True:
    tz = timezone('America/Sao_Paulo')
    now = datetime.now(tz)
    h = datetime.now().hour
    m = datetime.now().minute+4
    s = datetime.now().second

    if m > 59:
        h += 1
        m = 0
    if h <= 9:
        h = f'0{h}'
    if m <= 9:
        m = f'0{m}'
    if s <= 9:
        s = f'0{s}'
    print(f'{h}:{m}:{s}')
    #hora = datetime.datetime.now().strftime("%H:%M")
    numero_aleatorio1 = random.randint(1, 10)
    numero_aleatorio2 = random.randint(1, 10)
    for i in range(1,10):
        print(numero_aleatorio1,numero_aleatorio2)
        
    dados  = bot.send_message(chat_id=chat_id, text=(f'''
🧧♦️ GERANDO OPORTUNIDADE ♦️🧧

🐯 Fortune Tiger 🐯
           
🔥 {(numero_aleatorio1)}X NORMAL
🔥 {(numero_aleatorio2)}X TURBO

⏰ Valido até:{h}:{m}
                                                     
  {LINK_SITE} '''),
parse_mode='MARKDOWN', disable_web_page_preview=True) 
    
    time.sleep(240)#240
    bot.send_message(chat_id=chat_id, text=(f'''
🧧🏮 CARTA LIBERADA 🏮🧧
 ✅🐯 𝐆𝐑𝐄𝐄𝐍                                 
''', dados . chat . id , dados . message_id))
    time.sleep(60)#60
    #ALERT_GALE1()
    time.sleep(10)#10
    #DELET_GALE1()
    time.sleep(50)#50
