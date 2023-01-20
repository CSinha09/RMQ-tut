import pika
import time
import random

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue='letterbox')

msg_ID = 1

while(1):

    msg = f"Sending Msg_ID={msg_ID}"

    channel.basic_publish(exchange='', routing_key='letterbox', body=msg)

    print(f"Msg is sen : {msg}")

    time.sleep(random.randint(1,4))

    msg_ID+=1

