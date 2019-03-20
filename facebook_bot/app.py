from flask import  Flask, request
from pymessenger.bot import Bot
import random


app = Flask(__name__)

ACCESS_TOKEN = "EAAIidDT4VXcBAAk8y7gDRjrY7sm50cmFztTh18etz5LFXqbnDm7ZCVy3vsUM2h1rj22Gv6PosVZCsQVsYEv8slwcnMZC7ywCPodOF4OJtnHrFGlYTVwLBnL29VUP5aeZATyYF5tYeZCvaTaRUUkc6oj4fwn1G3ZCKbLv5O0z4KlAZDZD"
VERIFY_TOKEN = "TESTINGTOKEN152789"

bot = Bot(ACCESS_TOKEN)


#Получать сообщения, посылаемые фейсбуком нашему боту мы будем в этом терминале вызова
@app.route('/', methods = ['GET', 'POST'])
def receive_messege():
    # return "Hello world"
    if request.method == "GET":
        # до того как позволить людям отправлять что-либо боту, Facebook проверяет маркер,
        # подтверждающий, что все запросы, получаемые ботом, приходят из Facebook
        token_sent = request.args['hub.verify_token']
        return verify_fb_token(token_sent)

    # если запрос не был GET, это был POST-запрос и мы обрабатываем запрос пользователя
    else:
        # получаем сообщение, отправленное пользователем боту
        output = request.get_json()
        for event in output['entry']:
            messagging = event['messaging']
            for message in messagging:
                if message.get('message'):
                # определяем ID, чтобы знать куда отправлять ответ
                 recipient_id = message['sender']['id']
                # если пользователь отправил text
                if message['message'].get('text'):
                    response_sent_text = get_message()
                    sent_message(recipient_id, response_sent_text)
                # если пользователь отправил GIF, фото, видео и любой не текстовый объект
                if message['message'].get('attachments'):
                    response_sent_nontext = get_message()
                    send_message(recipient_id, response_sent_nontext)
        return "Message Processed"




def verify_fb_token(token_sent):
    '''Сверяет токен, отправленный фейсбуком, с имеющимся у вас.
    При соответствии позволяет осуществить запрос, в обратном случае выдает ошибку.'''
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


def send_message(recipient_id, response):
    '''Отправляет пользователю текстовое сообщение в соответствии с параметром response.'''
    bot.send_text_message(recipient_id, response)
    return "success"

def get_message():
    '''Отправляет случайные сообщения пользователю.'''
    sample_responses = ["It's working!"]
    # sample_responses = ["Потрясающе!", "Я вами горжусь!", "Продолжайте в том же духе!", "Лучшее, что я когда-либо видел!"]
    return random.choice(sample_responses)



if __name__ == "__main__":
    app.run()