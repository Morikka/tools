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
            with open('wx.jpg','rb') as f:
                bot.sendPhoto(chat_id,f)
            f.close()
        elif command.startswith('/cat'):
            getphoto = rand()
            with open('cat/'+str(getphoto)+'.jpg','rb') as f:
                bot.sendPhoto(chat_id,f)
            f.close()

MessageLoop(bot, handle).run_as_thread()

while 1:
    time.sleep(10)