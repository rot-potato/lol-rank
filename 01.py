import discord
from discord.ext import commands
import asyncio
import random
from time import sleep

client = discord.Client()

COR =0x690FC3
TOKEN = 'NTUxMTM5MzkyMDMxNTU1NTk0.D1spHg.D9FOPKXvC1XOkqgDfkZGIeurP2U'
msg_id = None
msg_user = None

@client.event
async def on_ready():
    print("Iniciando os motores...")
    sleep(0.5)
    print(client.user.name)
    print(client.user.id)
    print('Pronto!')

@client.event
async def on_message(message):

    if message.content.lower().startswith("!lol"):
        embed1 = discord.Embed(
            title="Escolha seu Elo!",
            color=COR,
            description="- Ferro = 👎\n"
                        "- Bronze = 🐤\n"
                        "- Prata  =  📘 \n"
                        "- Ouro  = 📙\n"
                        "- Platina = 👍\n"
                        "- Diamante = ✋\n"
                        "- Mestre = 👊\n"
                        "- Grã-Mestre = ✊\n"
                        "- Desafiante = 🙏\n",)

    botmsg = await client.send_message(message.channel, embed=embed1)

    await client.add_reaction(botmsg, "👎")
    await client.add_reaction(botmsg, "🐤")
    await client.add_reaction(botmsg, "📘")
    await client.add_reaction(botmsg, "📙")
    await client.add_reaction(botmsg, "👍")
    await client.add_reaction(botmsg, "✋")
    await client.add_reaction(botmsg, "👊")
    await client.add_reaction(botmsg, "✊")
    await client.add_reaction(botmsg, "🙏")

    global msg_id
    msg_id = botmsg.id

    global msg_user
    msg_user = message.author

@client.event
async def on_reaction_add(reaction, user):
    msg = reaction.message

    if reaction.emoji == "👎" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Ferro-LOL", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji == "🐤" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Bronze-LOL", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji == "📘" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Prata-LOL", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji == "📙" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Ouro-LOL", msg.server.roles)
        await client.add_roles(user, role)
        print("add")

    if reaction.emoji == "👍" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Platina-LOL", msg.server.roles)
        await client.add_roles(user, role)
        print("add")

    if reaction.emoji == "✋" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Diamante-LOL", msg.server.roles)
        await client.add_roles(user, role)
        print("add")

    if reaction.emoji == "👊" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Mestre-LOL", msg.server.roles)
        await client.add_roles(user, role)
        print("add")

    if reaction.emoji == "✊" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Grã_Mestre-LOL", msg.server.roles)
        await client.add_roles(user, role)
        print("add")

    if reaction.emoji == "🙏" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Desafiante-LOL", msg.server.roles)
        await client.add_roles(user, role)
        print("add")

@client.event
async def on_reaction_remove(reaction, user):
    msg = reaction.message

    if reaction.emoji == "👎" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Ferro-LOL", msg.server.roles)
     await client.add_roles(user, role)
     print("remove")

    if reaction.emoji == "🐤" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Bronze-LOL", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")

    if reaction.emoji == "📘" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Prata-LOL", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")

    if reaction.emoji == "📙" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Ouro-LOL", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")

    if reaction.emoji == "👍" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Platina-LOL", msg.server.roles)
        await client.add_roles(user, role)
        print("remove")

    if reaction.emoji == "✋" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Diamante-LOL", msg.server.roles)
        await client.add_roles(user, role)
        print("remove")

    if reaction.emoji == "👊" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Mestre-LOL", msg.server.roles)
        await client.add_roles(user, role)
        print("remove")

    if reaction.emoji == "✊" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Grã_Mestre-LOL", msg.server.roles)
        await client.add_roles(user, role)
        print("remove")

    if reaction.emoji == "🙏" and msg.id == msg_id:  # and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Desafiante-LOL", msg.server.roles)
        await client.add_roles(user, role)
        print("remove")

client.run(TOKEN)