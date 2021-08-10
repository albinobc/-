import discord
from discord import channel
from discord import guild
from discord import message
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
TOKEN = 'ODc0MjQ4NTcyMzI4MDk1NzQ2.YRENbg.E13dPyuzOMGbYkYI9ozFRdYAmT0'
client = commands.Bot(command_prefix='!')



@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('뻘짓'))
    print('[system] 제목학원 테스터가 성공적으로 구동됨')

    @bot.command()
    async def 홀짝(ctx):
        import random
        dice = random.randint(1, 6)
        embed = discord.Embed(title='홀, 짝중에 하나를 선택해주세요.',
                              description='선택 한 뒤에 어떤 수가 나왔는지 알려드려요.')
        embed.add_field(name='> 주사위의 눈', value='???')
        embed.add_field(name='> 홀수', value='🔴')
        embed.add_field(name='> 짝수', value='🔵')
        await ctx.message.delete()
        msg = await ctx.channel.send(embed=embed)
        await msg.add_reaction('🔴')
        await msg.add_reaction('🔵')

        try:
            def check(reaction, user):
                return str(reaction) in ['🔴', '🔵'] and \
                       user == ctx.author and reaction.message.id == msg.id

            reaction, user = await bot.wait_for('reaction_add', check=check)
            if (str(reaction) == '🔴' and dice % 2 == 1) or \
                    (str(reaction) == '🔵' and dice % 2 == 0):
                embed = discord.Embed(title='홀, 짝중에 하나를 선택해주세요.',
                                      description='정답입니다! 계속해서 도전해보세요!')
            else:
                embed = discord.Embed(title='홀, 짝중에 하나를 선택해주세요.',
                                      description='틀렸습니다... 계속해서 도전해보세요!')
            embed.add_field(name='> 주사위의 눈', value=str(dice))
            embed.add_field(name='> 홀수', value='🔴')
            embed.add_field(name='> 짝수', value='🔵')
            await msg.clear_reactions()
            await msg.edit(embed=embed)
        except:
            pass

    @bot.event
    async def on_message(msg):
        if msg.author.bot: return None
        await bot.process_commands(msg)

    @bot.command()
    async def 안녕(uuu):
        await uuu.channel.send('나도 안녕!')

    @bot.command()
    async def 제목(hhh):
         embed = discord.Embed(title='지을 제목과 짤의 링크를 작성해주세요.',
                              description='예) 크크루삥뽕-https://discordapp.com/channels/')
         await hhh.message.delete()
         msg = await hhh.channel.send(embed=embed)

    @bot.command()
    async def 제목짓기(fff,*,message):
        emb=discord.Embed(title=f'{fff.message.author.mention}', description=f"{message}")
        msg=await fff.channel.send(embed=emb)
        await fff.message.delete()
        await msg.add_reaction('👍')





bot.run(TOKEN)
