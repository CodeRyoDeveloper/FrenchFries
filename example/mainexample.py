import discord
import json

from email import message
from discord.utils import get

intents=discord.Intents().all()     # 獲取所有的 Intents 對象
intents.message_content = True      # 允許讀取消息內容
intents.members = True              # 允許讀取成員資料

try:
    # 讀取 config.json 的設定檔案
    with open("config.json") as f:
        config=json.load(f)
        token=config['discord_bot_token']
        channelID=int(config['discord_channel_id'])
except FileNotFoundError:
    print('找不到 config.json 檔案')
except KeyError:
    print('config.json 檔案格式不正確')
    
# Discord 機器人變數設置
bot = discord.Client(intents=intents)
    
# Discord 機器人狀態設置
@bot.event
async def on_ready():
    print('目前登入身份：',bot.user)
    game = discord.Game('coderyo.com')
    # discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
    await bot.change_presence(status=discord.Status.online, activity=game)

# Discord AutoRole
@bot.event
#當有成員加入（DC群）時
async def on_member_join(member):
    #給予加入DC群的成員 config.id 的身分組
    role = discord.utils.get(member.guild.roles, id=962360300563230800)
    await member.add_roles(role)
    #發送歡迎訊息
    channel = discord.utils.get(member.guild.channels, id=962354694997540935)
    await channel.send(f"{member.mention} 剛剛加入了【CodeRyoᶠʳⁱᵉˢ🍟碼凌薯】！")

# Discord 機器人 TOKEN
try:
    bot.run(token)
except discord.LoginFailure:
    print("Discord Bot Token 錯誤！")