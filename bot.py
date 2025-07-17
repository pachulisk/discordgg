from dotenv import load_dotenv
load_dotenv()
import os
# # # 導入Discord.py模組
# # import discord

# # # client是跟discord連接，intents是要求機器人的權限
# # intents = discord.Intents.default()
# # intents.message_content = True
# # client = discord.Client(intents = intents)

# # # 調用event函式庫
# # @client.event
# # # 當機器人完成啟動
# # async def on_ready():
# #     print(f"目前登入身份 --> {client.user}")

# # @client.event
# # # 當頻道有新訊息
# # async def on_message(message):
# #     # 排除機器人本身的訊息，避免無限循環
# #     if message.author == client.user:
# #         return
# #     # 新訊息包含Hello，回覆Hello, world!
# #     if message.content == "Hello":
# #         await message.channel.send("Hello, world!")

# # client.run("機器人的TOKEN")

# # 導入Discord.py模組
# import discord
# # 導入commands指令模組
# from discord.ext import commands

# # intents是要求機器人的權限
# intents = discord.Intents.all()
# # command_prefix是前綴符號，可以自由選擇($, #, &...)
# bot = commands.Bot(command_prefix = "%", intents = intents)

# @bot.event
# # 當機器人完成啟動
# async def on_ready():
#     print(f"目前登入身份 --> {bot.user}")

# @bot.command()
# # 輸入%Hello呼叫指令
# async def Hello(ctx):
#     # 回覆Hello, world!
#     await ctx.send("Hello, world!")

token = os.getenv("TOKEN")



import os
import asyncio
import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "$", intents = intents)

# 當機器人完成啟動時
@bot.event
async def on_ready():
    print(f"目前登入身份 --> {bot.user}")

# 載入指令程式檔案
@bot.command()
async def load(ctx, extension):
    await bot.load_extension(f"cogs.{extension}")
    await ctx.send(f"Loaded {extension} done.")

# 卸載指令檔案
@bot.command()
async def unload(ctx, extension):
    await bot.unload_extension(f"cogs.{extension}")
    await ctx.send(f"UnLoaded {extension} done.")

# 重新載入程式檔案
@bot.command()
async def reload(ctx, extension):
    await bot.reload_extension(f"cogs.{extension}")
    await ctx.send(f"ReLoaded {extension} done.")

# 一開始bot開機需載入全部程式檔案
async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with bot:
        await load_extensions()
        await bot.start(token)

# 確定執行此py檔才會執行
if __name__ == "__main__":
    asyncio.run(main())
