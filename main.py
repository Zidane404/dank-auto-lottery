import discord, asyncio, json, random

from discord.ext import commands

with open('./config.json') as f:
    config = json.load(f)

token = config.get('token')


bot = commands.Bot(command_prefix=config.get('prefix'), self_bot=True)
bot.remove_command('help')

@bot.event
async def on_ready():
    print("Successfully Authorised as: " + bot.user.name + " UID: (" + str(bot.user.id) + ")")
    print('Use $lottery [amount] in any channel to begin! ')

@bot.command()
async def lottery(ctx, amount: int,):
    await ctx.message.delete()
    for i in range (0, amount):
        async with ctx.typing():
            await asyncio.sleep(3)
        await ctx.send("pls lottery")
        async with ctx.typing():
            await asyncio.sleep(random.randint(5,10))
        await ctx.send("yes")
        await asyncio.sleep(3600)
        await asyncio.sleep(random.randint(20,60))

bot.run(token, bot=False)

