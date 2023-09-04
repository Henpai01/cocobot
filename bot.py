import discord
import responses


async def send_message(message, user_messege, is_private):
    try:
        response = responses.get_message(user_messege)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_dicord_bot():
    TOKEN = 'MTE0ODA4NTg2ODYxNjIyMDcxNg.GQ_Ln-.xfmJrR1SwOx5u2Z2M8SEUwTe-2bOvKxh4wXqdw'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)


    @client.event
    async def on_ready():
        print(f"{client.user} is now running")


    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username= str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')
              
        if user_message[0] == '?':
            user_message = user_message[1: ] 
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)


    client.run(TOKEN)
