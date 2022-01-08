import discord

token = "Token"
message = "Text"

client = discord.Client()


@client.event
async def on_connect():
    for friend in client.user.friends:
        try:
            await friend.send(message)
            print(f"Messaged {friend.name}")
        except:
            pass

    for channel in client.private_channels:
        try:
            await channel.send(message)
            print(f"Messaged {friend.name}")
        except:
            pass


client.run(token, bot=False)