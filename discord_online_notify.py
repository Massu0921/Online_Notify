import json, socket, time, sys, os
import discord

time.sleep(20)

# open config.json
with open(os.path.dirname(os.path.abspath(__file__)) + "/config.json", 'r') as cf:
    config = json.load(cf)

client = discord.Client()

@client.event
async def on_ready():
    print('----------')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('----------')

    ch_myroom = client.get_channel(int(config["discord"]["ch_notify"]))
    device_info = socket.gethostbyname_ex(socket.gethostname() + ".local")
    info_txt = \
        "{}\n\"{}\" is Connected :globe_with_meridians:\nIP Address: {}"                                 \
        .format(time.asctime(), device_info[0], device_info[2])

    await ch_myroom.send(info_txt)
    await client.logout()
    await sys.exit()

if __name__ == "__main__":
    client.run(config["discord"]["token"])
