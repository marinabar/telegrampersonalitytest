import telebot
import random

token = "561568815:AAE3kTf7n2apXhUFvLndnyxlWmbVffcvEm0"
telebot.apihelper.proxy = {'https': 'socks5://tvorogme@tvorog.me:6666'}
bot = telebot.TeleBot(token=token)

photo25=['http://www.muramur.ca/image/policy:1.3284377:1505397667/Costume-de-tranche-de-pain-pour-chat.jpg?w=1000&$p$w=f6a1fff',
                  'https://www.avantjetaisriche.com/wp-content/uploads/2017/01/costume-pizza-chat.jpg',
                  'http://blog.pretemoitonchat.com/wordpress/wp-content/uploads/2014/10/2.-2BTaco.jpg']
photo5=['https://cdn.thinglink.me/api/image/644170278137495554/1240/10/scaletowidth',
                'https://static.wamiz.fr/images/animaux/chats/large/persan-2922.jpg',
                'https://mobile-cdn.123rf.com/300wm/evdoha/evdoha1205/evdoha120502780/13734580-sifflement-chat-en-col%C3%A8re-agressive.jpg?ver=6',]
photo105=['https://www.atelier-mascarade.com/photos_v1_a_v3/photos_v39/v39579.jpg',
                  'https://img.ohmymag.com/article/1280/chat/chat-sphynx_76b7c59729ac1b54522420fc09cea8255f31f502.jpg',
                  'https://static.wamiz.fr/images/articles/facebook/article/interpreter-attitudes-chat-fb-5942b57e03e2d.jpg']
photo1310=['http://a133.idata.over-blog.com/300x291/3/96/78/46/CE1-CE2/chat-botte.jpg',
                   'http://www.lolchat.fr/wp-content/uploads/2014/03/chat-blanc-boule-poils.jpg',
                   'https://www.demotivateur.fr/images-buzz/8925/a.jpg',]
photo1317=['https://www.atelier-mascarade.com/photos_v1_a_v3/photos_v39/v39579.jpg',
                   'https://static.wamiz.fr/images/animaux/chats/large/persan-2922.jpg',
                   'https://cdn.thinglink.me/api/image/644170278137495554/1240/10/scaletowidth']

photo1917=['https://www.videobuzzy.com/images/gallerie/chat-dans-le-bain/(17).jpg',
                   'https://img.ohmymag.com/article/1280/chat/chat-sphynx_76b7c59729ac1b54522420fc09cea8255f31f502.jpg',
                   'http://www.vetopedia.fr/wp-content/uploads/2017/06/chat_surpris.jpg']
photoder=['https://www.avantjetaisriche.com/wp-content/uploads/2017/01/costume-pizza-chat.jpg',
                  'http://a133.idata.over-blog.com/300x291/3/96/78/46/CE1-CE2/chat-botte.jpg',
                  'https://static.wamiz.fr/images/articles/facebook/article/interpreter-attitudes-chat-fb-5942b57e03e2d.jpg']


a=0

@bot.message_handler(commands=['start'])
def start(message):
    global a
    text = message.text
    user_id = message.chat.id
    bot.send_message(user_id, "Hello")
    bot.send_message(user_id, "I am PsyKatBot, your new psy ")
    bot.send_message(user_id, "I am a pro of the image therapy")
    bot.send_message(user_id, "You are going to choose an answer for a question, and I will tell what kind of cat are you with an image")
    bot.send_message(user_id, "What is your favourite colour ?")
    bot.send_message(user_id, "/1 Blue or purple /2 Red or yellow /3 Black  /4 Other")
    if text == '/1' or text == '/4':
        a+=2
    else:
        a+=1
    

@bot.message_handler(commands=['1', '2', '3', '4' ])
def first(message):
    global a
    text = message.text
    user_id = message.chat.id
    bot.send_message(user_id, "Ok good, good let's continue")
    bot.send_message(user_id, "Now what device you rather :")
    bot.send_message(user_id, "/5 Phones /6 Computers /7 Tablets /8 Notebook ")
    if text == '/5' or text == '/8':
        a+=5
    else:
        a+=3

@bot.message_handler(commands=['5', '6', '7', '8' ])
def second(message):
    global a
    text = message.text
    user_id = message.chat.id
    bot.send_message(user_id, "Ok good, good let's continue")
    bot.send_message(user_id, "What is the result of 15//2 ?")
    bot.send_message(user_id, "/9 7,5 /10 8 /11 7")
    if text == '/9' or text == '/10':
        a+=3
    else:
        a-=2

@bot.message_handler(commands=['9', '10', '11'])
def third(message):
    global a
    text = message.text
    user_id = message.chat.id
    bot.send_message(user_id, "Ok good, good let's continue")
    bot.send_message(user_id, "What is your favourite road sign ?")
    bot.send_message(user_id, "/12 Access forbidden  /13 No passing /14 Speed limit /15 Bumpy road")
    if text == '/12' or text == '/13':
        a+=1
    else:
        a+=4
    
@bot.message_handler(commands=['12', '13', '14', '15' ])
def fourth(message):
    global a
    text = message.text
    user_id = message.chat.id
    bot.send_message(user_id, "Ok good, good let's continue")
    bot.send_message(user_id, "You rather tea or coffee ?")
    bot.send_message(user_id, "/16 Tea /17 Coffee")
    if text == '/16':
        a+=4
    else:
        a+=3

@bot.message_handler(commands=['16', '17'])
def fifth(message):
    global a
    text = message.text
    user_id = message.chat.id
    bot.send_message(user_id, "Ok good, good let's continue")
    bot.send_message(user_id, "You prefer flat roofs or angled roofs ?")
    bot.send_message(user_id, "/18 Flat /19 Angled /20 Both")
    if text == '/18' :
        a+=3
    elif text == '/19':
        a-=4
    elif text == '/20':
        a+=2

@bot.message_handler(commands=['18', '19', '20'])
def six(message):
    global a
    text = message.text
    user_id = message.chat.id
    bot.send_message(user_id, "Ok good, good let's continue")
    bot.send_message(user_id, "Now here is the cat you are")
    if a > 20:
        
        bot.send_photo(user_id, random.choice(photo25))
    if a <= 4:
        
        bot.send_photo(user_id, random.choice(photo5))
    if 4 < a > 8:
        
        bot.send_photo(user_id, random.choice(photo105))
    if 8 <= a > 11:
        
        bot.send_photo(user_id, random.choice(photo1310))
    if 11 <= a > 14:
        
        bot.send_photo(user_id, random.choice(photo1317))
    if 14 <= a > 17:
        
        bot.send_photo(user_id, random.choice(photo1917))
    if 17 <= a >= 20:
        
        bot.send_photo(user_id, random.choice(photoder))             
    bot.send_message(user_id, "To start again tap /start")
    
bot.polling(none_stop=True)




    
