# -*- coding: utf-8 -*-
#tw0ne (C)

import os
import time
import telebot
from telebot import types
import api
import ftplib
#import timetable

markup = types.ReplyKeyboardMarkup()
markup.row('/help')
markup.row('/homework')
markup.row('/timer')
markup.row('/timetable')

API_TOKEN = (api.api_bot)
bot = telebot.TeleBot(API_TOKEN)



# start 

@bot.message_handler(commands=['start'])
def text(message):
     bot.reply_to(message, """\
Привет,Я School manager!
P.S Нажми help для справки о функциях !
PROD BY tw()ne""", reply_markup=markup)

#help

@bot.message_handler(commands=['help'])
def text(message):
     bot.reply_to(message, """\
/homework - домашнее задание на завтра
/timer - время до 1го урока и других важных событий 
/timetable - расписание на сегодня и завтра 
""")

#homework

@bot.message_handler(commands=['homework'])
def text(message):
    def download(ftp,directory,file):
        ftp.cwd(directory)
        f = open(file,"wb")
        ftp.retrbinary("RETR " + file,f.write)
        f.close()
    download(ftp, "/public_html/pages", "file.txt")
    f = open('/home/pyt/FinalBOt/FINAL EDIT BOT/main_bot/file.txt')
    bot.reply_to(message, (f.read(4000)))
    f.close()

#timer

@bot.message_handler(commands=['timer'])
def text(message):
   f = open('/home/pyt/FinalBOt/FINAL EDIT BOT/main_bot/time.txt')
   bot.reply_to(message, (f.read(4000)))
   f.close()

bot.polling()
