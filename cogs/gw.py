import discord
from discord.ext import commands
from common.common import CogExtension
import requests
# 定義名為 Hello 的 Cog
class Gateway(CogExtension):

    def create_fee_package(gwid, yyyymmdd_effective, yyyymmdd_expiration, remark, traffic, amount):
      # API接口URL，这里需要替换为实际的接口地址
      url = "http://http://107.172.190.217/create_fee_package"
      
      # 请求体数据
      payload = {
          "gwid": gwid,
          "effective_date": yyyymmdd_effective,
          "expiration_date": yyyymmdd_expiration,
          "remark": remark,
          "traffic": traffic,
          "amount": amount
      }
      
      try:
          # 发送POST请求
          response = requests.post(url, json=payload)
          
          # 检查请求是否成功
          response.raise_for_status()
          
          # 返回响应结果（假设接口返回JSON格式）
          return response.json()
      
      except requests.exceptions.RequestException as e:
          # 处理请求异常
          print(f"请求发生错误: {e}")
          return None
      
    # 前綴指令
    @commands.command()
    async def cfp(self, ctx: commands.Context):
        """
        cfp = create fee package，创建资费包
        """
        await ctx.send("请输入网关ID:")
        gwid = await self.bot.wait_for("message")
        await ctx.send("请输入生效日期yyyy-mm-dd:")
        effective_date = await self.bot.wait_for("message")
        await ctx.send("请输入过期日期yyyy-mm-dd:")
        expiration_date = await self.bot.wait_for("message")
        await ctx.send("请输入备注:")
        remark = await self.bot.wait_for("message")
        await ctx.send("请输入流量(数字，单位GB)")
        traffic = await self.bot.wait_for("message")
        await ctx.send("请输入金额(数字，单位$)")
        amount = await self.bot.wait_for("message")
        # 发起请求
        result = self.create_fee_package(gwid, effective_date, expiration_date, remark, traffic, amount)
        await ctx.send("资费包创建中...")
        await ctx.send(result)

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

