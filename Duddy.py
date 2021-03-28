import discord, os, json, random, ast, asyncio, datetime,  openpyxl, sys
from discord import message
import time
from urllib.request import urlopen, Request
import urllib
import urllib.request
import bs4
from discord.ext import commands
from discord.utils import get
import pytz


client = commands.Bot(command_prefix= "/")

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready(): 
    print("봇이 작동됨!!!")
    print(client.user)
    print("============================")
    import asyncio
    user = len(client.users)
    server = len(client.guilds)
    await client.change_presence(status=discord.Status.offline)
    game = discord.Game("부팅 중...현재 명령어 사용 불가")
    message = ["/도움말", str(user) + "명과" + str(server) + "개의 서버에서 사용중!"]
    while True:
        await client.change_presence(status=discord.Status.online, activity=discord.Game(message[0]))
        message.append(message.pop(0))
        await asyncio.sleep(5)

@client.event
async def on_member_join(user):
    embed = discord.Embed(title="두디 봇", description="`안녕하세요`**{}** `님 반갑습니다~`".format(user))
    embed.set_footer(text="두디 봇 ㅣ두디", icon_url="https://cdn.discordapp.com/attachments/794473634286403589/803465360728260618/thumb.jpg")
    embed.set_image(url="https://cdn.discordapp.com/attachments/806400210644369411/813197997692420126/last.png")
    await user.add_roles(client.get_guild(804937068358664192).get_role(808922015015763979), reason="디스코드봇 자동부여")
    await user.guild.system_channel.send(embed=embed)
    
@client.event
async def on_member_remove(user):
    embed = discord.Embed(title="두디 봇", description="`안녕히계세요..`**{}** `님 또 와주세요..`".format(user))
    embed.set_footer(text="두디 봇 ㅣ두디", icon_url="https://cdn.discordapp.com/attachments/794473634286403589/803465360728260618/thumb.jpg")
    embed.set_image(url="https://cdn.discordapp.com/attachments/806400210644369411/813198006253256795/last.png")
    await user.guild.system_channel.send(embed=embed)

@client.event
async def on_message(message): 
    if message.content.startswith("/킥"):
        if message.content == "/킥":
            await message.channel.send(embed=discord.Embed(title="에러 발생", description = "올바른 명령어는 '/킥 (킥할 유저의 아이디) (사유)'에요", color=0xff0000))
        else:
            if message.author.guild_permissions.administrator:
                user = await client.fetch_user(int(message.content.split(' ')[1][3:21]))
                reason = message.content[25:]
                if(len(message.content.split(" ")) == 1):
                    reason = "None"
                await message.guild.kick(user, reason=reason)
                embed = discord.Embed(title="Duddy Bot", color=0xAAFFFF) 
                embed.add_field(name="킥된 유저", value=f"`{user.mention}`", inline=False)
                embed.add_field(name="킥 시킨 관리자", value=f"`{message.author.mention}`", inline=False)
                embed.add_field(name="사유", value=f"`{reason}`", inline=False)
                embed.set_image(url="https://cdn.discordapp.com/attachments/806400210644369411/811947287945150484/001_1.png")
                embed.set_footer(text="두디 봇 ㅣ두디")
                await client.get_channel(int(821742242233581568)).send(embed=embed)
            else:
                await message.channel.send(embed=discord.Embed(title="오류발생", description =f"{message.author.mention}님은 권한이 없어요", color=0xff0000))
                return

    if message.content.startswith("/밴"):
        if message.content == "/밴":
            await message.channel.send(embed=discord.Embed(title="에러 발생", description = "올바른 명령어는 '/밴 (밴할 유저의 아이디) (사유)'에요", color=0xff0000))
        else:
            if message.author.guild_permissions.administrator:
                user = await client.fetch_user(int(message.content.split(' ')[1][3:21]))
                reason = message.content[25:]
                if(len(message.content.split(" ")) == 1):
                    reason = "None"
                await message.guild.ban(user, reason=reason)
                embed = discord.Embed(title="Duddy Bot", color=0xAAFFFF) 
                embed.add_field(name="밴된 유저", value=f"`{user.mention}`", inline=False)
                embed.add_field(name="밴 시킨 관리자", value=f"`{message.author.mention}`", inline=False)
                embed.add_field(name="사유", value=f"`{reason}`", inline=False)
                await client.get_channel(int(821746583673765908)).send(embed=embed)
            else:
                await message.channel.send(embed=discord.Embed(title="오류발생", description =f"{message.author.mention}님은 권한이 없어요", color=0xff0000))
                return

    if(message.content.split(" ")[0] == "/뮤트"):
        if(message.author.guild_permissions.manage_channels):
            try:
                user = message.guild.get_member(int(message.content.split(' ')[1][3:21]))
                await message.guild.get_channel(message.channel.category_id).set_permissions(user, send_messages=False)
                embed=discord.Embed(title="`🔇 : Mute`", color = 0x00ff00)
                embed.add_field(name="뮤트된 유저", value=f"`{user}`", inline=False)
                embed.add_field(name="뮤트한 유저", value=f"`{message.author}`")
                await message.channel.send(embed=embed)
            except Exception as e:
                await message.channel.send(embed=discord.Embed(title="에러 발생", description = str(e), color = 0xff0000))
                return
        else:
            await message.channel.send(embed=discord.Embed(title="권한 부족", description = message.author.mention + "님은 채널을 관리 할 수 있는 권한이 없습니다.", color = 0xff0000))
            return

    
    if(message.content.split(" ")[0] == "/뮤트해제"):
        if(message.author.guild_permissions.manage_channels):
            try:
                user = message.guild.get_member(int(message.content.split(' ')[1][3:21]))
                await message.guild.get_channel(message.channel.category_id).set_permissions(user, overwrite=None)
                embed=discord.Embed(title="`🔈 : Un Mute`", color = 0x00ff00)
                embed.add_field(name="뮤트된 유저", value=f"`{user}`", inline=False)
                embed.add_field(name="뮤트한 유저", value=f"`{message.author}`")
                await message.channel.send(embed=embed)
            except Exception as e:
                await message.channel.send(embed=discord.Embed(title="`에러 발생`", description = str(e), color = 0xff0000))
                return
        else:
            await message.channel.send(embed=discord.Embed(title="`권한 부족`", description = message.author.mention + "님은 채널을 관리 할 수 있는 권한이 없습니다.", color = 0xff0000))
            return

    
    if message.content.startswith("/청소"):
        if message.content == "/청소":
            await message.channel.send(embed=discord.Embed(title="에러 발생", description = "올바른 명령어는 '/청소 (청소할 개수)'에요", color=0xff0000))
        else:
            if message.author.guild_permissions.administrator:
                number = int(message.content.split(" ")[1])
                await message.delete()
                await message.channel.purge(limit=number)
                a = await message.channel.send(embed=discord.Embed(title="`두디 봇`", description =f"💬 : {number}개의 메세지가 {message.author.mention}님의 의하여 삭제 되었습니다", color=0x00ff00))
                print(f"{message.author.mention}님이 {number}개의 메세지를 청소하는 코드를 사용했어요")
            elif message.author.id == 704535152763601007:
                number = int(message.content.split(" ")[1])
                await message.delete()
                await message.channel.purge(limit=number)
                a = await message.channel.send(embed=discord.Embed(title="두디 봇", description =f"{number}개의 메세지가 {message.author.mention}님의 의하여 삭제 되었습니다", color=0x00ff00))
            else:
                await message.channel.send(embed=discord.Embed(title="오류발생", description =f"{message.author.mention}님은 권한이 없어요", color=0xff0000))
                return

    if message.content == "/핑":
        ping = client.latency
        if ping <= 100:
            embed=discord.Embed(title="", description = f'🏓 **{str(round(ping * 1000))}ms** 입니다!\n `🟢`[양호합니다]', color=0x00ff00)
            embed.set_footer(text="두디 봇 ㅣ두디")    
            await message.channel.send(embed=embed)
        else:
            embed=discord.Embed(title="", description = f'🏓 **{str(round(ping * 1000))}ms** 입니다!\n`🟡`[불안정합니다]', color=0x00ff00)
            embed.set_footer(text="두디 봇 ㅣ두디")
            await message.channel.send(embed=embed)
    
    if message.content == "/제작자":
        embed = discord.Embed(title="제작자 목록", description="", color=0x00ff00)
        embed.set_author(name="Duddy Bot", icon_url="https://cdn.discordapp.com/attachments/794473634286403589/803465360728260618/thumb.jpg")
        embed.set_image(url="https://cdn.discordapp.com/attachments/794473634286403589/803465360728260618/thumb.jpg")
        embed.add_field(name="두디(제작자)", value="파키(관리자)",inline=True)
        embed.add_field(name="카이(호스팅 담당)", value="카이(형님)",inline=True)
        embed.add_field(name="제우스(관리자)", value="부들(부 관리자)",inline=True)
        embed.set_image(url="https://cdn.discordapp.com/attachments/806400210644369411/811947287945150484/001_1.png")
        embed.set_footer(text="두디 봇 ㅣ두디")
        await message.channel.send(embed=embed)

    if message.content.startswith("/정보"):
        status = message.author.status
        if status == "online":
            status = "온라인🟢"
        elif status == "dnd":
            status = "방해금지⛔"
        elif status == "idle":
            status = "자리비움🟡"
        else:
            status = "오프라인⚪"
        if message.author.bot == False:
            bot = "유저"
        else:
            bot = "봇"
        date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
        embed = discord.Embed(title=f'{message.author.name}의 정보')
        embed.add_field(name="이름", value=message.author.name, inline=False)
        embed.add_field(name="별명", value=message.author.display_name)
        embed.add_field(name="가입일", value=str(date.year) + "년" + str(date.month) + "월" + str(date.day) + "일", inline=False)
        embed.add_field(name="아이디", value=message.author.id)
        embed.add_field(name="상태", value=f"{status}", inline=False)
        embed.add_field(name="최상위 역할", value=message.author.top_role.mention, inline=False)
        embed.add_field(name="봇", value=bot)
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.set_image(url="https://cdn.discordapp.com/attachments/806400210644369411/811947287945150484/001_1.png")
        embed.set_footer(text="두디 봇 ㅣ두디")
        await message.channel.send(embed=embed)
    
    if message.content == '/도움말' or message.content == '/도움' or message.content == '/help':
        await message.channel.send("https://discord.gg/baueR5wtRc")
    if message.content == '/도움말' or message.content == '/도움' or message.content == '/help':
        n = 0
        helps = [discord.Embed(title='목차', description='**페이지 1**\n`<<목차>>`\n**페이지 2**\n`<<관리 기능>>`\n**페이지 3**\n`<<추가 기능>>`\n**페이지 4**\n`<<편의 기능>>`\n**페이지 5**\n`<<재미 기능>>`\n**페이지 6**\n`<<봇 정보>>`', color=0x00ffff),
                 discord.Embed(title='관리 기능', description='**/킥 [사용자 ID] [사유]**\n사용자를 밴을 시킵니다\n**/밴 [사용자 ID] [사유]**\n사용자를 서버에서 밴을 시킵니다\n **/고정 [고정할 매세지]** \n매세지를 고정합니다\n **/핑** \n봇의 핑을 알려줍니다', color=0x00fffff),
                 discord.Embed(title='추가 기능', description='**/청소 [청소할 계수]**\n채팅청소를 합니다\n**/투표 [투표할 내용]**\n투표를 합니다\n **/정보** \n자신의 정보를 봅니다', color=0x00fffff),
                 discord.Embed(title='편의 기능', description='**/맵 선택**\n배드워즈 맵 중 하나가 선택이 됩니다\n**/register [자신의 마크 닉네임]**\n리지스터가 됩니다\n**/아이템**\n밴 아이템을 봅니다\n**/날씨 [지역]**\n지역에 날씨를 확인합니다.', color=0x00fffff),
                 discord.Embed(title='재미 기능', description='**/가위바위보 (가위 바위 또는 보)**\n가위바위보 게임을 해요', color=0x00fffff),
                 discord.Embed(title='봇정보', description='**/두디 서버 링크**\nhttps://discord.gg/baueR5wtRc\n**/개발자**\n봇 개발자는 두디님입니다!\n**/디자이너**\n디자이너는 두디님입니다!', color=0x00fffff),]
                
        help_msg = await message.channel.send(embed=helps[n])
        for i in ['⏪', '◀️', '⏹️', '▶️', '⏩']:
            await help_msg.add_reaction(i)
        def check(reaction, user):
        	return user == message.author and reaction.message.channel == message.channel
        while True:
            try:
                reaction, user = await client.wait_for('reaction_add', check=check, timeout=120)
            except asyncio.TimeoutError:
                break
            if reaction.emoji == '⏪':
                n = 0
                await help_msg.edit(embed=helps[n])
            elif reaction.emoji == '⏩':
                n = len(helps)-1
                await help_msg.edit(embed=helps[n])
            elif reaction.emoji == '◀️':
                if n != 0:
                    n -= 1
                    await help_msg.edit(embed=helps[n])
            elif reaction.emoji == '▶️':
                if n != len(helps)-1:
                    n += 1
                    await help_msg.edit(embed=helps[n])
            elif reaction.emoji == '⏹️':
                await help_msg.delete()
                break

    '''if message.content == "/도움말":
        embed=discord.Embed(title="**Duddy Bot**", description="  ", color=0x00ff56)
        embed.add_field(name="**/청소 <청소할 개수>**", value="`채팅을 청소하는 명령어입니다`", inline=False)
        embed.add_field(name="**/정보**", value="`자신의 정보를 보는 명령어입니다`", inline=False)
        embed.add_field(name="**/킥 <아이디>**", value="`상대방을 킥을 할때 사용하는 명령어입니다`", inline=False)
        embed.add_field(name="**/밴 <아이디>**", value="`상대방을 밴을 할때 사용하는 명령어입니다`", inline=False)
        embed.add_field(name="**/핑**", value="`자신의 핑을 보는 명령어입니다`", inline=False)
        embed.set_footer(text="추가 예정입니다.")
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.set_image(url="https://cdn.discordapp.com/attachments/806400210644369411/811947287945150484/001_1.png")
        embed.set_footer(text="두디 봇 ㅣ두디")
        await message.channel.send(embed=embed)
'''
    if message.content == "/맵 선택":
        maps = ['Lectus', 'Invasion', 'Rise', 'Boletum', 'Aquarium', 'katsu']
        cmap = random.choice(maps)
        embed = discord.Embed(title=cmap)
        embed.set_author(name="🎉 - 맵 선택 완료!")
        embed.set_image(url="https://cdn.discordapp.com/attachments/806400210644369411/811947287945150484/001_1.png")
        embed.set_footer(text="두디 봇 ㅣ두디")
        await message.channel.send(embed=embed)

    if message.content.startswith("씨발"):
        await message.delete()
        embed = discord.Embed(timestamp=message.created_at, colour=discord.Colour.red(), title="욕설감지", description=f"{message.author.mention}님이 욕을 하였습니다")
        embed.add_field(name="사용한 욕설", value=f"~~씨X~~")
        embed.set_image(url="https://cdn.discordapp.com/attachments/806400210644369411/811947287945150484/001_1.png")
        embed.set_footer(text="두디 봇 ㅣ두디")
        await message.channel.send(embed=embed)
    
    if message.content.startswith("개새끼"):
        await message.delete()
        embed = discord.Embed(timestamp=message.created_at, colour=discord.Colour.red(), title="욕설감지", description=f"{message.author.mention}님이 욕을 하였습니다")
        embed.add_field(name="사용한 욕설", value=f"~~개새X~~")
        embed.set_image(url="https://cdn.discordapp.com/attachments/806400210644369411/811947287945150484/001_1.png")
        embed.set_footer(text="두디 봇 ㅣ두디")
        await message.channel.send(embed=embed)

    if message.content.startswith("느금마"):
        await message.delete()
        embed = discord.Embed(timestamp=message.created_at, colour=discord.Colour.red(), title="욕설감지", description=f"{message.author.mention}님이 욕을 하였습니다")
        embed.add_field(name="사용한 욕설", value=f"~~느금X~~")
        embed.set_image(url="https://cdn.discordapp.com/attachments/806400210644369411/811947287945150484/001_1.png")
        embed.set_footer(text="두디 봇 ㅣ두디")
        await message.channel.send(embed=embed)

    if message.content.startswith("좆같네"):
        await message.delete()
        embed = discord.Embed(timestamp=message.created_at, colour=discord.Colour.red(), title="욕설감지", description=f"{message.author.mention}님이 욕을 하였습니다")
        embed.add_field(name="사용한 욕설", value=f"~~X같네~~")
        embed.set_image(url="https://cdn.discordapp.com/attachments/806400210644369411/811947287945150484/001_1.png")
        embed.set_footer(text="두디 봇 ㅣ두디")
        await message.channel.send(embed=embed)

    if message.content.startswith("뒤진새끼"):
        await message.delete()
        embed = discord.Embed(timestamp=message.created_at, colour=discord.Colour.red(), title="욕설감지", description=f"{message.author.mention}님이 욕을 하였습니다")
        embed.add_field(name="사용한 욕설", value=f"~~뒤진새X~~")
        embed.set_image(url="https://cdn.discordapp.com/attachments/806400210644369411/811947287945150484/001_1.png")
        embed.set_footer(text="두디 봇 ㅣ두디")
        await message.channel.send(embed=embed)

    if message.content.startswith('/투표'):
        subject = message.content [1:]
        embed=discord.Embed(title="투표!", description="찬성은👍 반대는👎", color=0x0088ff)
        embed.add_field(name="주제", value=subject, inline=False)
        embed.set_image(url="https://cdn.discordapp.com/attachments/806400210644369411/811947287945150484/001_1.png")
        embed.set_footer(text="두디 봇 ㅣ두디")
        message = await message.channel.send(embed=embed)
        await message.add_reaction("👍")
        await message.add_reaction("👎")

    if message.content.startswith("/register"):
        setName = str(message.content.split(" ")[1])
        role = discord.utils.get(message.guild.roles, name="register")
        embed = discord.Embed(title="정상적으로 회원가입이 완료되셨습니다.", description="닉네임 : {}".format(setName))
        embed.set_image(url="https://cdn.discordapp.com/attachments/806400210644369411/811947287945150484/001_1.png")
        embed.set_footer(text="두디 봇 ㅣ두디")
        await message.channel.send(embed=embed)
        await message.author.edit(nick="[0] " + setName)
    if message.content.startswith("/입장"):
        embed = discord.Embed(title="큐에 입장하였습니다",description="닉네임 : {}".format(setName))
        await message.channel.send(embed=embed)
    
    if message.content == "/가위바위보 가위" or message.content == "/가위바위보 바위" or message.content == "/가위바위보 보":
        random_ = random.randint(1, 3)

        if random_ == 1:
            if message.content == "/가위바위보 가위":
                await message.channel.send(f"{message.author.mention}님은 가위, 저도 가위! 비겼습니다.")
            elif message.content == "/가위바위보 바위":
                await message.channel.send(f"{message.author.mention}님은 바위, 저는 가위! {message.author.mention}님이 이겼습니다.")   
            elif message.content == "/가위바위보 보":
                await message.channel.send(f"{message.author.mention}님은 보, 저는 가위! 제가 이겼습니다.")   
        elif random_ == 2:
            if message.content == "/가위바위보 가위":
                await message.channel.send(f"{message.author.mention}님은 가위, 저는 바위! 제가 이겼습니다.")
            elif message.content == "/가위바위보 바위":
                await message.channel.send(f"{message.author.mention}님은 바위, 저도 바위! 비겼습니다.")   
            elif message.content == "/가위바위보 보":
                await message.channel.send(f"{message.author.mention}님은 보, 저는 바위! {message.author.mention}님이 이겼습니다.")
        elif random_ == 3:
            if message.content == "/가위바위보 가위":
                await message.channel.send(f"{message.author.mention}님은 가위, 저는 보! {message.author.mention}님이 이겼습니다.")
            elif message.content == "/가위바위보 바위":
                await message.channel.send(f"{message.author.mention}님은 바위, 저는 보! 제가 이겼습니다.")   
            elif message.content == "/가위바위보 보":
                await message.channel.send(f"{message.author.mention}님은 보, 저도 보! 비겼습니다.")

    if message.content.startswith("/고정"):
        if message.content == "/고정":
            await message.channel.send(embed=discord.Embed(title="에러 발생", description = "올바른 명령어는 '/고정 (고정할 매세지)'에요", color=0xff0000))
            return
        else:
            if message.author.guild_permissions.administrator:
                await message.pin()
            else:
                await message.channel.send(embed=discord.Embed(title="오류발생", description =f"{message.author.mention}님은 권한이 없어요", color=0xff0000))
                return

    if message.content == "/아이템":
        embed=discord.Embed(title="**BAN ITEM**", color=0x00ff56)
        embed.set_author(name="EWW RANKED BEDWARS", icon_url="https://cdn.discordapp.com/attachments/794473634286403589/803465360728260618/thumb.jpg")
        embed.add_field(name="엔더진주", value="옵시디언", inline=False)
        embed.add_field(name="팝업 타워", value="물", inline=False)
        embed.add_field(name="에메활", value="(금)활은 다이아2부터 사용 가능합니다.", inline=False)
        embed.add_field(name="침뿌후", value="침대 제거 이후 에메랄드 사용 가능합니다.", inline=False)
        embed.add_field(name="침뿌후", value="침대 제거 전 에메랄드 수집 가능합니다", inline=False)
        await message.channel.send(embed=embed)


    if message.content == "/뽑기":
        ran = random.randint(0,10)
        if ran == 0:
            embed=discord.Embed(title="뽑기 실패", color=0x00ff56)
            embed.set_author(name="Duddy Bot", icon_url="https://cdn.discordapp.com/attachments/794473634286403589/803465360728260618/thumb.jpg")
            await message.channel.send(embed=embed)
        if ran == 1:
            embed=discord.Embed(title="뽑기 실패", color=0x00ff56)
            embed.set_author(name="Duddy Bot", icon_url="https://cdn.discordapp.com/attachments/794473634286403589/803465360728260618/thumb.jpg")
            await message.channel.send(embed=embed)
        if ran == 2:
            embed=discord.Embed(title="뽑기 성공 \n  https://discord.gg/8u2X8sEzGv 들어오셔서 관리자한테 디엠을 보내주세요!", color=0x00ff56)
            embed.set_author(name="Duddy Bot", icon_url="https://cdn.discordapp.com/attachments/794473634286403589/803465360728260618/thumb.jpg")
            await message.channel.send(embed=embed)
        if ran == 3:
            embed=discord.Embed(title="뽑기 실패", color=0x00ff56)
            embed.set_author(name="Duddy Bot", icon_url="https://cdn.discordapp.com/attachments/794473634286403589/803465360728260618/thumb.jpg")
            await message.channel.send(embed=embed)
        if ran == 4:
            embed=discord.Embed(title="뽑기 실패", color=0x00ff56)
            embed.set_author(name="Duddy Bot", icon_url="https://cdn.discordapp.com/attachments/794473634286403589/803465360728260618/thumb.jpg")
            await message.channel.send(embed=embed)
        if ran == 5:
            embed=discord.Embed(title="뽑기 실패", color=0x00ff56)
            embed.set_author(name="Duddy Bot", icon_url="https://cdn.discordapp.com/attachments/794473634286403589/803465360728260618/thumb.jpg")
            await message.channel.send(embed=embed)
        if ran == 6:
            embed=discord.Embed(title="뽑기 실패", color=0x00ff56)
            embed.set_author(name="Duddy Bot", icon_url="https://cdn.discordapp.com/attachments/794473634286403589/803465360728260618/thumb.jpg")
            await message.channel.send(embed=embed)
        if ran == 7:
            embed=discord.Embed(title="뽑기 실패", color=0x00ff56)
            embed.set_author(name="Duddy Bot", icon_url="https://cdn.discordapp.com/attachments/794473634286403589/803465360728260618/thumb.jpg")
            await message.channel.send(embed=embed)
        if ran == 8:
            embed=discord.Embed(title="뽑기 실패", color=0x00ff56)
            embed.set_author(name="Duddy Bot", icon_url="https://cdn.discordapp.com/attachments/794473634286403589/803465360728260618/thumb.jpg")
            await message.channel.send(embed=embed)
        if ran == 9:
            embed=discord.Embed(title="뽑기 실패", color=0x00ff56)
            embed.set_author(name="Duddy Bot", icon_url="https://cdn.discordapp.com/attachments/794473634286403589/803465360728260618/thumb.jpg")
            await message.channel.send(embed=embed)
        if ran == 10:
            embed=discord.Embed(title="뽑기 실패", color=0x00ff56)
            embed.set_author(name="Duddy Bot", icon_url="https://cdn.discordapp.com/attachments/794473634286403589/803465360728260618/thumb.jpg")
            await message.channel.send(embed=embed)
    
    if message.content.startswith('/타이머'):

        Text = ""
        learn = message.content.split(" ")
        vrsize = len(learn)  
        vrsize = int(vrsize)
        for i in range(1, vrsize):    
            Text = Text + " " + learn[i]

        sec = int(Text)

        for i in range(sec, 0, -1):
            print(i)
            await message.channel.send(embed=discord.Embed(description='타이머 작동중 : '+str(i)+'초'))
            time.sleep(1)
        else:
            print("땡")
            await message.channel.send(embed=discord.Embed(description='타이머 종료!'))

    if message.content == "/초대링크":
        embed=discord.Embed(title="두디 서버 초대링크", description = "[초대 링크]",url="https://discord.com/api/oauth2/authorize?client_id=812203766756540417&permissions=8&scope=bot", color=0x00ff00)
        await message.channel.send(embed=embed)

    if message.content.startswith("/날씨"):
        learn = message.content.split(" ")
        location = learn[1]
        enc_location = urllib.parse.quote(location+'날씨')
        hdr = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + enc_location
        print(url)
        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        todayBase = bsObj.find('div', {'class': 'main_info'})

        todayTemp1 = todayBase.find('span', {'class': 'todaytemp'})
        todayTemp = todayTemp1.text.strip()  # 온도
        print(todayTemp)

        todayValueBase = todayBase.find('ul', {'class': 'info_list'})
        todayValue2 = todayValueBase.find('p', {'class': 'cast_txt'})
        todayValue = todayValue2.text.strip()  # 밝음,어제보다 ?도 높거나 낮음을 나타내줌
        print(todayValue)

        todayFeelingTemp1 = todayValueBase.find('span', {'class': 'sensible'})
        todayFeelingTemp = todayFeelingTemp1.text.strip()  # 체감온도
        print(todayFeelingTemp)

        todayMiseaMongi1 = bsObj.find('div', {'class': 'sub_info'})
        todayMiseaMongi2 = todayMiseaMongi1.find('div', {'class': 'detail_box'})
        todayMiseaMongi3 = todayMiseaMongi2.find('dd')
        todayMiseaMongi = todayMiseaMongi3.text  # 미세먼지
        print(todayMiseaMongi)

        tomorrowBase = bsObj.find('div', {'class': 'table_info weekly _weeklyWeather'})
        tomorrowTemp1 = tomorrowBase.find('li', {'class': 'date_info'})
        tomorrowTemp2 = tomorrowTemp1.find('dl')
        tomorrowTemp3 = tomorrowTemp2.find('dd')
        tomorrowTemp = tomorrowTemp3.text.strip()  # 오늘 오전,오후온도
        print(tomorrowTemp)

        tomorrowAreaBase = bsObj.find('div', {'class': 'tomorrow_area'})
        tomorrowMoring1 = tomorrowAreaBase.find('div', {'class': 'main_info morning_box'})
        tomorrowMoring2 = tomorrowMoring1.find('span', {'class': 'todaytemp'})
        tomorrowMoring = tomorrowMoring2.text.strip()  # 내일 오전 온도
        print(tomorrowMoring)

        tomorrowValue1 = tomorrowMoring1.find('div', {'class': 'info_data'})
        tomorrowValue = tomorrowValue1.text.strip()  # 내일 오전 날씨상태, 미세먼지 상태
        print(tomorrowValue)

        tomorrowAreaBase = bsObj.find('div', {'class': 'tomorrow_area'})
        tomorrowAllFind = tomorrowAreaBase.find_all('div', {'class': 'main_info morning_box'})
        tomorrowAfter1 = tomorrowAllFind[1]
        tomorrowAfter2 = tomorrowAfter1.find('p', {'class': 'info_temperature'})
        tomorrowAfter3 = tomorrowAfter2.find('span', {'class': 'todaytemp'})
        tomorrowAfterTemp = tomorrowAfter3.text.strip()  # 내일 오후 온도
        print(tomorrowAfterTemp)

        tomorrowAfterValue1 = tomorrowAfter1.find('div', {'class': 'info_data'})
        tomorrowAfterValue = tomorrowAfterValue1.text.strip()

        print(tomorrowAfterValue)  # 내일 오후 날씨상태,미세먼지

        embed = discord.Embed(
            title=learn[1]+ ' 날씨 정보',
            description=learn[1]+ '날씨 정보입니다.',
            colour=discord.Colour.gold()
        )
        embed.add_field(name='현재온도', value=todayTemp+'˚', inline=False)  
        embed.add_field(name='체감온도', value=todayFeelingTemp, inline=False)  
        embed.add_field(name='현재상태', value=todayValue, inline=False)  
        embed.add_field(name='현재 미세먼지 상태', value=todayMiseaMongi, inline=False)  
        embed.add_field(name='오늘 오전/오후 날씨', value=tomorrowTemp, inline=False)  
        embed.add_field(name='**----------------------------------**',value='**----------------------------------**', inline=False)  # 구분선
        embed.add_field(name='내일 오전온도', value=tomorrowMoring+'˚', inline=False)  # 내일오전날씨
        embed.add_field(name='내일 오전날씨상태, 미세먼지 상태', value=tomorrowValue, inline=False)  # 내일오전 날씨상태
        embed.add_field(name='내일 오후온도', value=tomorrowAfterTemp + '˚', inline=False)  # 내일오후날씨
        embed.add_field(name='내일 오후날씨상태, 미세먼지 상태', value=tomorrowAfterValue, inline=False)  # 내일오후 날씨상태
        message = await message.channel.send(embed=embed)
    
    if(message.content.split(" ")[0] == "/rb"):
        if(message.author.guild_permissions.manage_channels):
            role = discord.utils.get(message.guild.roles, name="Ranked Ban")
            await message.channel.send(str(role)+"에게 역할이 적용되었습니다.")
            await message.author.add_roles(role)
    
      
    
    if message.content.startswith("/출석체크"):
        i = 0
        d = i
        if i == 0:
            embed=discord.Embed(title="출석체크가 완료되었습니다.", color=0x00ff56)
            embed.set_author(name="Duddy Bot", icon_url="https://cdn.discordapp.com/attachments/794473634286403589/803465360728260618/thumb.jpg")
            embed.add_field(name="`출석:`{}".format(d+1), value="출석은 하루에 한번만 가능합니다.", inline=False)
            await message.channel.send(embed=embed)
        elif i == 1:
            embed=discord.Embed(title="출석체크가 완료되었습니다.", color=0x00ff56)
            embed.set_author(name="Duddy Bot", icon_url="https://cdn.discordapp.com/attachments/794473634286403589/803465360728260618/thumb.jpg")
            embed.add_field(name="`출석:`{}".format(d+2), value="출석은 하루에 한번만 가능합니다.", inline=False)
            await message.channel.send(embed=embed)
        else:
            embed=discord.Embed(title="출석체크가 완료되었습니다.", color=0x00ff56)
            embed.set_author(name="Duddy Bot", icon_url="https://cdn.discordapp.com/attachments/794473634286403589/803465360728260618/thumb.jpg")
            embed.add_field(name="`출석:`{}".format(d+3), value="출석은 하루에 한번만 가능합니다.", inline=False)
            await message.channel.send(embed=embed)

    if message.content == "/룰":
        if message.author.guild_permissions.administrator:
            embed=discord.Embed(title="**Rule**", color=0x00ff56)
            embed.set_author(name="Duddy Bot", icon_url="https://cdn.discordapp.com/attachments/794473634286403589/803465360728260618/thumb.jpg")
            embed.add_field(name="**————[🔇뮤트🔇]————**", value="`• 통화방을 시끄럽게 하는 행위 => (뮤트 1회)\n• 분쟁 (말싸움 등) => 뮤트 2일 )`", inline=False)
            embed.add_field(name="**————[⚠️경고 1개⚠️]————**", value="`• 같은 내용의 메세지를 불필요하게 3번 이상 하는 행위\n• 오해의 여지가 있는 발언\n• 역활,관리자를 구걸하는 행위`", inline=False)
            embed.add_field(name="**————[⚠️경고 2개⚠️]————**", value="`• 상대방에게 공격적 또는 예의없는 태도\n• 정치적 발언 또는 그것과 관련된 사진`", inline=False)
            embed.add_field(name="**<<<<<[🚫밴🚫]>>>>>**", value="`• 성드립 , 섹드립 또는 성적 수치심을 주는 발언은 밴입니다\n• 다른사람의 신상 정보를 올리는 행위\n• 욕배틀, 박제방 등 부적절한 서버를 홍보하는 행위`", inline=False)
            embed.add_field(name="<<<<<[🚫밴 웨이브🚫]>>>>>", value="`• 밴 역할은 채팅을 칠수도 없으며 통화방에도 참가할 수 없습니다\n• 경고 10개는 3일 밴\n• 경고 20개는 3주 밴\n• 경고 30개는 영구밴이므로 규칙 잘 지키시길 바랍니다`", inline=False)
            await message.channel.send(embed=embed)
    
    
    if message.content.startswith("/계산"):
        global calcResult
        param = message.content.split()
        try:
            if param[1].startswith("더하기"):
                calcResult = int(param[2])+int(param[3])
                embed = discord.Embed(title="결과", description =f"`{str(calcResult)}입니다`", color=0xff0000)
                await message.channel.send(embed=embed)
                #await message.channel.send("`결과` **:** "+str(calcResult))
            if param[1].startswith("빼기"):
                calcResult = int(param[2])-int(param[3])
                embed = discord.Embed(title="결과", description =f"`{str(calcResult)}입니다`", color=0xff0000)
                await message.channel.send(embed=embed)
                #await message.channel.send("`결과` **:** "+str(calcResult))
            if param[1].startswith("곱하기"):
                calcResult = int(param[2])*int(param[3])
                embed = discord.Embed(title="결과", description =f"`{str(calcResult)}입니다`", color=0xff0000)
                await message.channel.send(embed=embed)
                #await message.channel.send("`결과` **:** "+str(calcResult))
            if param[1].startswith("나누기"):
                calcResult = int(param[2])/int(param[3])
                embed = discord.Embed(title="결과", description =f"`{str(calcResult)}입니다`", color=0xff0000)
                await message.channel.send(embed=embed)
                #await message.channel.send("`결과` **:** "+str(calcResult))
        except IndexError:
            await message.channel.send("**무슨 숫자를 계산할지 알려주세요!**")
        except ValueError:
            await message.channel.send("**숫자로 넣어주세요!**")
        except ZeroDivisionError:
            await message.channel.send("**0으로 나눌 수 없습니다!**")
    
    if message.content.startswith("/팀 1 6"):
        role = random.randrange(1,3)
        role1 = random.randrange(1,3)
        role2 = random.randrange(1,3)
        role3 = random.randrange(1,3)
        role4 = random.randrange(1,3)
        role5 = random.randrange(1,3)
        embed = discord.Embed(title="**Duddy Bot**", description =f"**1팀** `{role}` ㅣ `{role3}`")
        embed.add_field(name="**---------------**", value=f"**2팀** `{role1}` ㅣ `{role4}`", inline=False)
        embed.set_footer(text="※ㅣ수가 똑같이 나오면 다시 돌려주세요.")
        await message.channel.send(embed=embed)

    if message.content.startswith("/팀 8인"):
        list = []
        ran_num = random.randint(1,2)
        ran_num1 = random.randint(1,2)

        for i in range(2):
            while ran_num in list:
                ran_num = random.randint(1,2)
            list.append(ran_num)

        for i in range(2):
            while ran_num1 in list:
                ran_num1 = random.randint(1,2)
            list.append(ran_num1)
        
        list.sort()
        await message.channel.send(list)

    if message.content == "/이모지 출력":
        msg = await message.channel.send("채팅을 보기 위해서는 밑에 이모지를 눌러주세요!")
        await msg.add_reaction("\U00000030\U0000FE0F\U000020E3")
        role = discord.utils.get(message.guild.roles, name="똑똑한 두디")
        await msg.author.add_roles(role)
        return

    if message.content == "/디엠":
        embed=discord.Embed(title="`Duddy Bot`", color=0x00ff56)
        embed.add_field(name= "Hello what happened?",value = "무슨 일이 있으셨나요? \n무슨 일이 있으시면 L_duddy#9391로 문의 주세요!")
        embed.set_author(name="Duddy Bot", icon_url="https://cdn.discordapp.com/attachments/794473634286403589/803465360728260618/thumb.jpg")
        await message.author.send(embed=embed)

       

    if message.content.startswith ("/공지"):
        await message.channel.purge(limit=1)
        i = (message.author.guild_permissions.administrator)
        if i is True:
            notice = message.content[4:]
            channel = client.get_channel(812209518220935188)
            embed = discord.Embed(title="**Duddy Bot**", description="공지사황은 필히 확인 부탁드립니다.\n――――――――――――――――――――――――――\n\n{}\n\n――――――――――――――――――――――――――".format(notice),timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. L_duddy#9391 | 담당 관리자 : {}".format(message.author), icon_url="https://cdn.discordapp.com/attachments/794473634286403589/803465360728260618/thumb.jpg")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/794473634286403589/803465360728260618/thumb.jpg")
            await message.channel.send ("@everyone", embed=embed)
 
        if i is False:
            await message.channel.send("{}, 당신은 관리자가 아닙니다".format(message.author.mention))
access_token = os.environ["ODEyMjAzNzY2NzU2NTQwNDE3.YC9VtA.z0PuGb_BU5AKZISA5B5lpWUOG-c"]
client.run(access_token)

