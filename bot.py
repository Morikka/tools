import telepot
from telepot.loop import MessageLoop
import random
import os
import time

bot = telepot.Bot('')
bot.setWebhook()

def rand():
    ans = random.randint(0,749)
    f = 'cat/'+str(ans)+'.jpg'
    jud = os.access(f,os.F_OK)
    #print str(ans)+' '+str(jud)
    if jud:
        return ans
    return rand()

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    if content_type == 'text':
        command = msg['text']
        if command.startswith('/money'):
            bot.sendPhoto(chat_id,open('wx.jpg','rb'))
        elif command.startswith('/cat'):
            getphoto = rand()
            bot.sendPhoto(chat_id,open('cat/'+str(getphoto)+'.jpg','rb'))

MessageLoop(bot, handle).run_as_thread()

while 1:
    time.sleep(10)