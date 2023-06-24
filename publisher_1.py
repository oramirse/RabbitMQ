import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='rabbit', durable=True)

messages = ["Mensaje 1", "Mensaje 2", "Mensaje 3"]

for message in messages:
    channel.basic_publish(
        exchange='',
        routing_key='rabbit',
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=2,  # make message persistent
        )
    )

connection.close()
