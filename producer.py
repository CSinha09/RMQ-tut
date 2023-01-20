import pika

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.queue_declare(queue='letterbox')

msg = "Hello World!!!!"

channel.basic_publish(exchange='', routing_key='letterbox', body=msg)

print(f"Msg is sen : {msg}")

connection.close()
