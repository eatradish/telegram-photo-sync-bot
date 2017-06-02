import telegram
import datetime
import random

bot = telegram.Bot(token='你的 TOKEN')

def download():
    a = 0
    while True:
        updates = bot.get_updates()
        u = updates[len(updates) - 1]
        if u.message.photo:
            if u != a:
                photo_file = bot.get_file(u.message.photo[-1].file_id)
                photo_file.download(custom_path='/var/www/file/ACG-img/' + 'photo-' + repr(datetime.datetime.now().timestamp()) + repr(random.random()*10) + '.jpg')
                a = u
            elif u == a:
                continue
        print(a)
download()
