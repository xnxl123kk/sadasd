import discord
import asyncio
import datetime

client = discord.Client()

@client.event
async def on_ready():
    print("봇이 정상적으로 실행되었습니다.")
    game = discord.Game('dm')
    await client.change_presence(status=discord.Status.online, activity=game)

#/dm {할말}로 전체DM 전송
@client.event
async def on_message(message):
    if message.content.startswith('/dm'):
        for i in message.guild.members:
            if i.bot == True:
                pass
            else:
                try:
                    msg = message.content[4:]
                    #메시지 관리권한이 있을시 사용가능
                    if message.author.guild_permissions.manage_messages:
                        embed = discord.Embed(color=0x1DDB16, timestamp=message.created_at)
                        embed.add_field(name="공지사항", value=msg, inline=True)
                        embed.set_footer(text=f"[눈보라샵]")
                        await i.send(embed=embed)
                except:
                    pass


client.run('NzYzNjY2MjY2MzcxMzkxNDg4.X37Bog.cg0m09HDpsSBbt_o3vLKBObeFN8')
