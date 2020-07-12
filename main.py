
import discord, asyncio
import os, sys
from discord.ext import commands
from discord.ext import tasks

client = commands.Bot(command_prefix="..")
client.remove_command('help')

@client.event
async def on_ready():
    print(f'Successfuly logged in as {client.user.name}\nID: {client.user.id}')
    
@client.command(description='Load an extension.', aliases=['load'])
async def l(ctx, extension):
    try:
        client.load_extension(f'cogs.{extension}')
        await ctx.send(f'Loaded.')
        print(f'Loaded {extension}')
    except Exception as e:
        await ctx.send(f'Error. Check CONSOLE.')
        print(f'Error - {e}')

@client.command(description='Unload an extension.', aliases=['unload'])
async def ul(ctx, extension):
    try:
        client.unload_extension(f'cogs.{extension}')
        await ctx.send(f'Unloaded.')
        print(f'Unloaded {extension}')
    except Exception as e:
        await ctx.send(f'Error. Check CONSOLE.')
        print(f'Error - {e}')

@client.command(description='Reload an extension.', aliases=['reload'])
async def rl(ctx, extension):
    try:
        client.unload_extension(f'cogs.{extension}')
        await asyncio.sleep(1)
        client.load_extension(f'cogs.{extension}')
        await ctx.send(f'Reloaded.')
        print(f'Reloaded {extension}')
    except Exception as e:
        await ctx.send(f'Error. Check CONSOLE.')
        print(f'Error - {e}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run()

