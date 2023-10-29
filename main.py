from twilio.rest import Client
import keys_twilio
    ##################### Api Rest Twilio (Mensajes de verificación al teléfono) ##########################

client = Client(keys_twilio.account_sid, keys_twilio.auth_token)

message = client.messages.create(
    body="Este es el código de verificación",
    from_=keys_twilio.twilio_number,
    to=keys_twilio.target_number
)
print(message.body)
    #######################################################################################################