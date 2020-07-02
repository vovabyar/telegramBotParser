from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from telethon import sync, events
import requests
import json
import hashlib
import time
import re
from virus_total_apis import PublicApi as VirusTotalPublicApi
from telethon import TelegramClient
import webbrowser
import urllib.request
import os

n = 0


api_id = 1700439

api_hash = 'b456cd4dfc1bfd56d078294fc501a949'

client = TelegramClient('anon', api_id, api_hash)

client.start()

dlgs = client.get_dialogs()

for dlg in dlgs:
    if dlg.title == 'LTC Click Bot':
        tegmo = dlg
    
class RunChromeTests():
    def testMethod(self):
        caps = {'browserName': 'chrome'}
        driver = webdriver.Remote(command_executor=f'http://localhost:4444/wd/hub', desired_capabilities=caps)
        driver.maximize_window()
        driver.get(url_rec)
        time.sleep(waitin + 10)
        driver.close()
        driver.quit()

while True:
    msgs = client.get_messages(tegmo, limit=1)
    for mes in msgs:
        if re.search(r'\bseconds to get your reward\b', mes.message):
            print("Найдено reward")
            str_a = str(mes.message)
            zz = str_a.replace('You must stay on the site for', '')
            qq = zz.replace('seconds to get your reward.', '')
            waitin = int(qq)
            print ("Ждать придется: ", waitin)
            client.send_message('LTC Click Bot', "/visit")
            time.sleep(3)
            msgs2 = client.get_messages(tegmo, limit=1)
            for mes2 in msgs2:
                button_data = mes2.reply_markup.rows[1].buttons[1].data
                message_id = mes2.id
				
                print("Перехожу по ссылке")
                time.sleep(2)
                try:
                    url_rec = messages[0].reply_markup.rows[0].buttons[0].url
                    ch = RunChromeTests()
                    ch.testMethod()
                    time.sleep(6)
                except:
                    client.send_message('LTC Click Bot', "/visit")
                fp = urllib.request.urlopen(url_rec)
                mybytes = fp.read()
                mystr = mybytes.decode("utf8")
                fp.close()
                if re.search(r'\bSwitch to reCAPTCHA\b', mystr):
                    from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
                    resp = client(GetBotCallbackAnswerRequest(
                            'LTC Click Bot',
                            message_id,
                            data=button_data
                    ))
                    time.sleep(2)
                    print("КАПЧА!")

                else:
                    time.sleep(waitin)

                    time.sleep(2)

        elif re.search(r'\bSorry\b', mes.message):
            client.send_message('LTC Click Bot', "/visit")
            time.sleep(6)
            print("Найдено Sorry")

        else:
            messages = client.get_messages('Litecoin_click_bot')
            url_rec = messages[0].reply_markup.rows[0].buttons[0].url
            f = open("per10.txt")
            fd = f.read()
            if fd == url_rec:
                print("Найдено повторение переменной")
                msgs2 = client.get_messages(tegmo, limit=1)
                for mes2 in msgs2:
                    button_data = mes2.reply_markup.rows[1].buttons[1].data
                    message_id = mes2.id
                    from telethon.tl.functions.messages import GetBotCallbackAnswerRequest
                    resp = client(GetBotCallbackAnswerRequest(
                        tegmo,
                        message_id,
                        data=button_data
                    ))
                    time.sleep(2)
            else:
                url = 'https://www.virustotal.com/vtapi/v2/url/scan'
                params = {
                    'apikey': '306c899cf2958abe7d84cab75bf52412279e0cda579571112c2f81764c20b65c', 'url': url_rec}
                response = requests.post(url, data=params)
                my_file = open('per10.txt', 'w')
                my_file.write(url_rec)
                print("Новая запись в файле сдерана")
                time.sleep(16)
                n = n + 1
                print("Пройдено циклов: ", n)