# import os
# from twilio.rest import Client


# # Find your Account SID and Auth Token at twilio.com/console
# # and set the environment variables. See http://twil.io/secure
# account_sid = "ACdfb05434f9576928e6cf5d0d156dff61"
# auth_token = "34195d89f4621f6f1ab8083794013b54"
# client = Client(account_sid, auth_token)

# message = client.messages \
#                 .create(
#                      body="Join Earth's mightiest heroes. Like Kevin Bacon.",
#                      from_='+17603164588',
#                      to='23783350860'
#                  )

# print(message.sid)

"""
from twilio.rest import Client

# Vos identifiants Twilio
account_sid = "ACdfb05434f9576928e6cf5d0d156dff61"
auth_token = "34195d89f4621f6f1ab8083794013b54"
client = Client(account_sid, auth_token)

# Créer un Messaging Service (si vous n'en avez pas déjà créé un)
service = client.messaging.services.create(friendly_name='My Messaging Service')

# Envoyer des messages en utilisant le Messaging Service
message = client.messages.create(
    body='Votre message ici',
    messaging_service_sid=service.sid,
    to=['+237683350860','+237690784542']  # Liste des numéros destinataires
)

print(message.sid)

"""


# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "ACdfb05434f9576928e6cf5d0d156dff61"
auth_token = "34195d89f4621f6f1ab8083794013b54"
client = Client(account_sid, auth_token)

message = client.messages.create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+17603164588',
                     to='+237683350860'
                 )

print(message.sid)