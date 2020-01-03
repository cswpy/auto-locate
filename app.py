import get_location
from flask import Flask, request
from pymessenger.bot import Bot

VERIFY_TOKEN = 'Phillip'
ACCESS_TOKEN = 'EAAmZAlFSOPFsBAO6byMH6GSZCWRcfSWPlMry7yFq7ZAvCFlSMeMAapbz3IGIwJM4yLbSgxib9yTaSJ0ZBCr4vpOGp2vPTTmdkNGgaaZAtjfa6UJh3mqBs4nBW1U3rgR9jBO0hNVJwLCurZBnZCbhkBN2IUp1zoM72vhVNWFWQLS0AZDZD'

app = Flask(__name__)
bot = Bot(ACCESS_TOKEN)

@app.route('/',methods=['GET','POST'])
def request_recv():
    if request.method == 'GET':
        token_recv = request.args.get('hub.verify_token')
        msg_sent = verify_token(token_recv)
        return msg_sent
    
    else:
        output = request.get_json()
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                if message.get('message'):
                    recipient_id = message['sender']['id']
                    if message['message']['text'] == 'location':
                        location = get_location()
                        send_message(recipient_id,location)
                    else:
                        send_message(recipient_id,'Phill is unavailable right now, he will check your message as soon as possible.')
                        return "Message Processed"

def verify_token(token_recv):
    if token_recv==VERIFY_TOKEN:
        return request.args.get('hub.challenge')
    else:
        return 'Invalid Verification Token'

def send_message(id,text):
    bot.send_text_message(id,text)
    return 'Successfully Sent'

if __name__=='__main__':
    app.run()