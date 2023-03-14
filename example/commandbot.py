import discord
from discord import app_commands 
from discord.ext import commands
class client(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        intents.members = True
        super().__init__(intents=intents)
        self.synced = False 

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: #檢查斜線指令是否已經同步 
            await tree.sync(guild = discord.Object(id=guild_id)) #特定伺服器: 如果是全域指令請留白 (全域註冊需要1-24小時
            self.synced = True
        print(f"We have logged in as {self.user}.")

bot = client()
tree = app_commands.CommandTree(bot)

@tree.command(guild = discord.Object(id=guild_id), name = 'test1', description='測試') #guild specific slash command
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message(f"初步測試成功{interaction.user.mention}", ephemeral = True) #ephemeral是否只有客戶端可見
@tree.command(guild = discord.Object(id=guild_id), name = 'test2', description='沒東西 別看!')
async def img(interaction: discord.Interaction):
    channel = bot.get_channel(channel_id)
    await interaction.response.send_message(f"{interaction.user.mention}抓到摸魚", ephemeral = False)
@tree.command(guild = discord.Object(id=guild_id), name = 'test3', description='試試')
async def kfg(interaction: discord.Interaction):    
    await interaction.response.send_message(f"試試就逝世",ephemeral=False)

bot.run("token")