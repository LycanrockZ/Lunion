from discord.ext import commands
from AntiScam import AntiScam

whitelist = [721724665932021831, 378314060078252032, 169145791464734720] 
logs_channel =931244721249067108 
bot = commands.Bot(command_prefix='.') 
bot.remove_command('ayuda') 

@bot.listen()
async def on_message(message):
    await AntiScam(message, bot = bot, whitelist = whitelist, muted_role='Mute', verified_role='verificado', logs_channel=logs_channel) 
bot.run('OTYyNDA0MDU5NTk0MjQ0MTQ3.YlHCoA.pwJPg9AwQ7X_6I7JhojgB27w9c4')