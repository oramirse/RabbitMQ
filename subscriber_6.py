import pika

def callback(ch, method, properties, body):
    print("Suscriptor 6 recibio:", body.decode())
    ch.basic_ack(delivery_tag=method.delivery_tag)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='rabbit', durable=True)
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='rabbit', on_message_callback=callback)

channel.start_consuming()