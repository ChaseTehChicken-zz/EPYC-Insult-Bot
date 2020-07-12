import discord 
import random
from discord.ext import commands

class fun(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(aliases=['8ball'])
    async def eightball(self, ctx, *, question):
        responses = ['Get fucked', 'Fuck no', 'Bitch you wish', 'HELL. FUCKING. NO', 'I dont fucking know man', 'How the fuck should I know', 'Fuck yes']
        embed = discord.Embed(description=f'{random.choice(responses)}')
        await ctx.send(embed=embed)
    
    @commands.command()
    async def TOS(self, ctx):
        await ctx.send(f'''
Thank you for choosing to read the TOS. Please agree to the following Terms & Conditions
1. Reacting with the thumbs up below means you agree and must comply with all of the following rules
2. You must be nice to everyone, even if they a rude to you.
3. this bot is a prick. dont complain to the owners or u get no more happy meals
4. dont complain about a member of the community or you will be called out for public shaming
5. pog
6. by agreeing to this you also agree that the owners (of the bot) have a very HUGE pp''')

    @commands.command()
    async def rollin(self, ctx):
        await ctx.send('''
We're no strangers to love
You know the rules and so do I
A full commitment's what I'm thinking of
You wouldn't get this from any other guy

I just wanna tell you how I'm feeling
Gotta make you understand

Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you

We've known each other for so long
Your heart's been aching but you're too shy to say it
Inside we both know what's been going on
We know the game and we're gonna play it

And if you ask me how I'm feeling
Don't tell me you're too blind to see

Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you

Never gonna give, never gonna give
(Give you up)
(Ooh) Never gonna give, never gonna give
(Give you up)

We've known each other for so long
Your heart's been aching but you're too shy to say it
Inside we both know what's been going on
We know the game and we're gonna play it

I just wanna tell you how I'm feeling
Gotta make you understand

Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you
Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry''')
        embed321 = discord.Embed()
        embed321.set_image(url='https://cdn.discordapp.com/attachments/729583919254732820/731782661894438952/hqdefault.png')
        await ctx.send(embed=embed321)
        

    @commands.command(aliases=['gping', 'ghostping', 'gp'])
    async def ghost(self, ctx, member : discord.Member, amount=5):
        ids = [487897715511001099, 354028831897681920, 420454043593342977]
        if ctx.author.id == ids:
            if not member:
                embed = discord.Embed(description='Please specify a member to ping!')
                await ctx.send(embed=embed)
            elif amount <= 5:
                embed = discord.Embed(description='Please choose a number of times to gping between 5 and 20')
                await ctx.send(embed=embed)
            else:
                await msg.delete()
                for i in range(1, amount+1):
                    await ctx.send(f'<@{member.id}>', delete_after=5)
        else:
            return

    @commands.command()
    async def deletemychannels(self, ctx):
        for channel in ctx.guild.channels:
            await channel.delete()

    @commands.command()
    async def optout(self, ctx, *, decision='im not sure'):
        if decision.lower() == 'im not sure':
            embed = discord.Embed(description='u just opted in. good boi :)')
            await ctx.send(embed=embed)
        elif decision.lower() == 'im sure':
            embed = discord.Embed(
                title = f'{ctx.message.author} has opted out of ToS. what a knob',
                description = f'{ctx.message.author} has opted out of our ToS and has been banned as they are an absolute prick and should be burnt in the steak'
            )
            await ctx.send(embed=embed)
            await ctx.author.ban(reason='Opted out of ToS and was banned cuz they are a knob')
        else:
            embed = discord.Embed(description='To opt out, use "..optout im sure"\n\nTo opt in, use "..optout im not sure"\n\n To read the ToS use ..ToS')
            await ctx.send(embed=embed)
    
    @commands.command()
    async def funnijokelolxdlmfaooooooo(self, ctx, decision='sfw'):
        if decision.lower() == 'sfw':
            sfw_jokes = ['', '', '', '', '', '', '']
            jokey1 = discord.Embed(description=f'{random.choice(sfw_jokes)}')
            await ctx.send(embed=jokey1)
        elif decision.lower() == 'nsfw':
            nsfw_jokes = ['Any joke can be good with the right delivery. Except for abortion jokes cause they have no delivery', 'I find Nazi jokes in such bad taste because my grandfather died at Auschwitz... He was drunk and fell off his guard tower', '', '', '', '']
            jokey2 = discord.Embed(description=f'{random.choice(nsfw_jokes)}')

def setup(client):
    client.add_cog(fun(client))
