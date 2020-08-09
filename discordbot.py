from discord.ext import commands
import os
import traceback
import random

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

from discord.ext.commands import CommandNotFound
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command()
async def name(ctx):
    await ctx.send('Torisan')

@bot.command()
async def version(ctx):
    await ctx.send('ver2')
    

list = ["刀","扇", "薙", "銃", "忍", "傘", "書", "毒", "絡", "騎", "古", "琵", "炎", "笛", "戦", "社","経", "絆","機", "新","爪","拒", "鎌", "塵", "旗","橇","鏡","櫂","兜", "槌","嵐"]


@bot.command()
import random

async def megami3(ctx):
    await random.shuffle(list)
    await ctx.send(str(list[0]+list[1]+list[2])+"とかで良いんじゃないですか？")
    
@bot.command()
async def megami2(ctx):
    random.shuffle(list)
    await ctx.send(str(list[0]+list[1])+"とかで良いんじゃないですか？")
    
@bot.event
async def on_message(message):
    if message.content=="megami1":
        megami = ["刀","扇", "薙", "銃", "忍", "傘", "書", "毒", "絡", "騎", "古", "琵琶", "炎", "笛", "戦", "社","経", "絆","機", "新","爪","拒", "鎌", "塵", "旗","橇","鏡","櫂","兜", "槌","嵐"]
        choice = random.choice(megami)
        await message.send_message(message.channel, choice) 
        
@bot.command()
def setup(bot):
    print("ロード完了")
   
@bot.event
if (message.content === 'restart') {
  if (message.author.id !== '#4495') return;
  message.channel.send('Restarted.').then(() => {
  process.exit(1);
})
};



bot.run(token)
