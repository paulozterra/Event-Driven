#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='Hola Curso UTEC!')
channel.basic_publish(exchange='', routing_key='email', body='Esto es un email!')
print(" [x] Mensaje Enviado ! 'Hola Curso UTEC!'")
connection.close()
