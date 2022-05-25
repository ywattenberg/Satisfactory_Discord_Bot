import discord
import os
import datetime
from discord.ext import commands

TOKEN = 'OTc4OTEyMTYzNzQzODA5NTc2.GiYK7Z.M0uEOQEYE80HXAsHs09qwdkpsdsJG9g2WKOrAA'
GUILD = ''

bot = commands.Bot(command_prefix='/')

@bot.command(name='start')
@commands.has_any_role('Bot', 'King')
async def start_server(ctx):
    print('start')
    await ctx.message.add_reaction('✅')
    os.system('dir')
    await ctx.send('Server starting wait 2 min')

@bot.command(name='stop')
@commands.has_any_role('Bot', 'King')
async def start_server(ctx):
    print('stop')
    await ctx.message.add_reaction('✅')
    os.system('dir')
    await ctx.send('Server stopped')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')

bot.run(TOKEN)