import json
import time

from discordrpc import AsyncDiscord, commands

CLIENT_ID = ""  # Provide your client id
CLIENT_SECRET = ""  # Provide your client secret

callback_received = False


def callback(code, event):
    print(f"code: {code} event: {event}")
    if code == 0:
        return
    event = json.loads(event)
    if event.get("cmd") != commands.AUTHORIZE:
        print(f"unknown command: {event.get("cmd")}")
        return


print("Setting up Discord client")
client = AsyncDiscord(CLIENT_ID, CLIENT_SECRET)

client.connect(callback)
print("Authorizing connection")
client.authorize()

try:
    while not callback_received:
        print("waiting for callback")
        time.sleep(1)
except KeyboardInterrupt:
    print("received interrupt, disconnecting client")
    client.disconnect()
