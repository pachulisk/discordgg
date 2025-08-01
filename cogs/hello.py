import discord
from discord.ext import commands
from common.common import CogExtension
# 定義名為 Hello 的 Cog
class Hello(CogExtension):

    # 前綴指令
    @commands.command()
    async def Hello(self, ctx: commands.Context):
        await ctx.send("Hello, world!")

    # 關鍵字觸發
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author == self.bot.user:
            return
        if message.content == "Hello":
            await message.channel.send("Hello, world!")

# Cog 載入 Bot 中
async def setup(bot: commands.Bot):
    await bot.add_cog(Hello(bot))

