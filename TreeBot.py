import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix = '$')

@client.event
async def on_ready():
        print('We are logged in as {0.user}!'.format(client))
        game = discord.Game("Coding | $cmds")
        await client.change_presence(status=discord.Status.online, activity=game)
#Unban Command
@client.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in banned_users:
        user = ban_entry.user

        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned!')
            return
#Kick Command
@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member : discord.Member, *, reason=None):
  await member.kick(reason=reason)
  await ctx.send('Kicked!')
#Ban Command
@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member : discord.Member, *, reason='Banned By TreeBot.'):
  await member.ban(reason=reason) 
  await ctx.send('Banned!')
#Creator Command
@client.command()
async def creator(ctx):
  
  await ctx.send('Made By treesdomatter231!')
#Ping Command (Tests The Bot)
@client.command()
async def ping(ctx):
  
  await ctx.send('Pong!')
#CMDS Command
@client.command()
async def cmds(ctx):
  await ctx.send('Help Documentation For Tree Bot Is Here: https://github.com/unkwn-byte/Discord-Bots/blob/main/commands.md')
#clear Command
@client.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=5):
        await ctx.channel.purge(limit=amount)
#code Command
@client.command()
async def code(ctx):
    ctx.send('https://github.com/unkwn-byte/Discord-Bots/blob/main/TreeBot.py')

@client.command()
async def version(ctx):
  
  await ctx.send('Version: 1.02')

@client.command()
async def invite(ctx):
  
  await ctx.send('Heres your invite: https://discord.gg/w9sXTJXyz2')
  
@client.command()
async def github(ctx):
  
  await ctx.send('The GitHub is located here: https://github.com/unkwn-byte/Discord-Bots')
  
client.run('TOKEN GOES HERE')
