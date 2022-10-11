
# Simple SMS Sender using Twilio API
# https://www.twilio.com
# pip install twilio

from twilio.rest import Client

account_sid = " ACCOUNT SID FROM CONSOLE"
auth_token = " AUTH TOKEN FROM CONSOLE"

# Client is the object in this case.
# Client is from the twilio api library.
c = Client(account_sid, auth_token)

# messages.create is the object method in this case.
message = c.messages.create(
    to = " NUM TO SEND TO",
    from_ = " NUM FROM CONSOLE",
    body = "Hello from Python!"
)

print(message.sid)

