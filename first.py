import os
from http import client
from twilio.rest import Client
# cl = Client("ACefbcbf4c94234feb0f8a6ec85ff63292",
#             "a28ecb820b75c3aa69b9333072bd8213")
# cl.messages.create(to="+998939956232",
#                    from_="+19378843082",
#                    body="Hi, Everyone! (har bir sms xabar narxi 0.255$ va bu faqatgina chiquvchi sms uchun!!!)")


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

auth_token_promotion = client.accounts.v1.auth_token_promotion().update()

print(auth_token_promotion.date_created)
