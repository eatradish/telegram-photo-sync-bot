import telegram
import datetime
import random

bot = telegram.Bot(token='你的 TOKEN')

def download():
    u = []
    updates = []
    while True:
        b = updates
        updates = bot.get_updates()
        #u = updates[len(updates) - 1]
        u = list(set(updates) - set(b))
        print(u)
        #list(map(lambda x: x[0]-x[1], zip(v2, v1)))
        for index in u:
            if index.message.photo:
                photo_file = bot.get_file(index.message.photo[-1].file_id)
                photo_file.download(custom_path='/var/www/file/ACG-img/' + 'photo-' + repr(datetime.datetime.now().timestamp()) + repr(random.random()*10) + '.jpg', timeout = 300)

download()
