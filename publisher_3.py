import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='rabbit', durable=True)

messages = ["Mensaje 7", "Mensaje 8", "Mensaje 9"]

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
