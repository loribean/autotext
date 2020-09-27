#import text message API
from twilio.rest import Client

#import scheduling
import schedule
import random
import time
from dotenv import load_dotenv
load_dotenv()
import os

messages = ["Good morning, love!", "Woke up thinking of you!"]

def send_message(quotes_list=messages):
    account = os.getenv("twilio_account")
    token = os.getenv("twilio_token")
    cellphone = os.getenv("cellphone")
    twilio_number = os.getenv("twilio_number")
    client = Client(account, token)
    
    quote = messages[random.randint(0,len(messages)-1)]

    client.messages.create(to=cellphone,from_=twilio_number,body=quote)




# send a message in the morning
schedule.every().day.at("10:30").do(send_message, messages)

# send a message every minute
# schedule.every().minute.at(":17").do(send_message, messages)

while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(2)
