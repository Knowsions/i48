# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient
 
# Find these values at https://twilio.com/user/account
account_sid = "AC930f8c2979f5bd61ea9f50d613813f99"
auth_token = "60c4a99ba94111ba30110205e93f61d2"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(to="+524772398525", from_="+18122264688",
body="El mejor de los dias, soy Juan Perez, su agente de seguros HDI, recordandole su poliza 11111 esta proxima a vencer. Gracias.")