from twilio.rest import Client

# Create an account in https://www.twilio.com/
# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              from_='+49199******', # Replace with your phone number
                              body='Hi, I am Tejveer ', # text you want to send
                              to='+49562*****'          # Replace with your Twilio number
                          )

print(message.sid)