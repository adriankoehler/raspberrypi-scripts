# -*- coding: utf-8 -*-

import time
import os
import sys
import random
import datetime
import RPi.GPIO as GPIO
import Adafruit_DHT
import telepot
from telepot.loop import MessageLoop

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_UP)

chat_id = 187354666
interval = 1800 #30min
desired_temp = 23
desired_hum = 60
below_desired_temp = False
below_desired_hum = False

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command

    if command == '/roll':
        bot.sendMessage(chat_id, random.randint(1,6))
    elif command == '/time':
        bot.sendMessage(chat_id, str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    elif command == '/getid':
        bot.sendMessage(chat_id, str(chat_id))
    elif command == '/rdy':
        bot.sendMessage(chat_id, (' Rdy! @ ' + (time.strftime("%d.%m.%Y %H:%M:%S"))))
    elif command == '/day':
        cmd = "/usr/local/bin/gpio write 6 1; /usr/local/bin/gpio write 28 1;"
        os.system(cmd)
        bot.sendMessage(chat_id, 'day mode')
    elif command == '/night':
        cmd = "/usr/local/bin/gpio write 6 0; /usr/local/bin/gpio write 28 0;"
        os.system(cmd)
        bot.sendMessage(chat_id, 'night mode')
    elif command == '/white':
        cmd = "echo 18=1 > /dev/pi-blaster; echo 23=1 > /dev/pi-blaster; echo 24=1 > /dev/pi-blaster"
        os.system(cmd)
        bot.sendMessage(chat_id, 'LEDs: white')
    elif command == '/off':
        cmd = "echo 18=0 > /dev/pi-blaster; echo 23=0 > /dev/pi-blaster; echo 24=0 > /dev/pi-blaster"
        os.system(cmd)
        bot.sendMessage(chat_id, 'LEDs: off')
    elif command == '/read':
        hum, temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4)
        time.sleep(2)
        message_temp = str((str(round(temp,2)) + ' °C').replace(".",","))
        message_hum = (str(round(hum,2)) + ' %').replace(".",",")
        os.system("echo " + message_temp)
        bot.sendMessage(chat_id, message_temp)
        bot.sendMessage(chat_id, message_hum)
    elif command.startswith('/update'):
        interval = command[8:]
        bot.sendMessage(chat_id, ('updated interval to: ' + str(interval)))

bot = telepot.Bot('449938028:AAHH_B3RCoHqOEC70pphQXweYNjLMssUcj4')

MessageLoop(bot, handle).run_as_thread()
os.system("echo '" + (time.strftime("%d.%m.%Y %H:%M:%S")) + ": raspberrypibot gestartet' >> /var/www/data/startup.log")
print 'Listening ...'

while True:
    hum, temp = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 4)
    if hum is not None and temp is not None:
        if hum < desired_hum:
            below_desired_hum = True
            bot.sendMessage(chat_id, 'Luftfeuchtigkeit unter ' + str(desired_hum) + '%! (' + str(round(hum,2)).replace(".",",") + '%)')
        if temp < desired_temp:
            below_desired_temp = True
            bot.sendMessage(chat_id, 'Temperatur ist unter ' + str(desired_temp) + '°C! (' + str(round(temp,2)).replace(".",",") + '°C)')
        if hum > desired_hum and below_desired_hum == True:
            below_desired_hum = False
            bot.sendMessage(chat_id, 'Luftfeuchtigkeit ist wieder über ' + str(desired_hum) + '%! (' + str(round(hum,2)).replace(".",",") + '%)')
        if temp > desired_temp and below_desired_temp == True:
            below_desired_temp = False
            bot.sendMessage(chat_id, 'Temperatur ist wieder über ' + str(desired_temp) + '°C! (' + str(round(temp,2)).replace(".",",") + '°C)')

    time.sleep(interval)
