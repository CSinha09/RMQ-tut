import pika
import time 
import random

def on_msg_received(ch, method, properties, body):
    processign_time = random.randint(1,6)
    print(f"received {body}, will need {processign_time} to process")
    time.sleep(processign_time)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print("Finished processing...")

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue='letterbox')

channel.basic_qos(prefetch_count=1)

channel.basic_consume(queue='letterbox', on_message_callback=on_msg_received)

print("Starting consuming msgs")

channel.start_consuming()
