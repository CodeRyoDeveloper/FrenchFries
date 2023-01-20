import discord

""" 
coderyo-discord-bot 是 CodeRyo 團隊應用於官方 Discord 上的綜合型客服機器人，
"""

intents=discord.Intents().all()     # 獲取所有的 Intents 對象
intents.message_content = True      # 允許讀取消息內容

# 讀取 config.json 的設定檔案
with open("config.json") as f:
    config=json.load(f)
    token=config['discord_bot_token']
    channelID=int(config['discord_channel_id'])
    
# Discord 機器人變數設置
bot = discord.Client(intents=intents)
    
# Discord 機器人狀態設置
@bot.event
async def on_ready():
    print('目前登入身份：',bot.user)
    game = discord.Game('coderyo.com')
    # discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
    await bot.change_presence(status=discord.Status.online, activity=game)
    
# Discord 機器人 TOKEN
bot.run(token)
