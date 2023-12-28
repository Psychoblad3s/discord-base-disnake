import os
import disnake; from disnake.ext import commands;
from utils.logs import log
from utils.cfg import cfg
from utils.animations import Animations
from cogs.cogs import errorCog

import disnake.errors as api_exceptions
from aiohttp import client_exceptions as web_exceptions

log = log()

cfgData = cfg(f"cfg.ini").cfgLoad()
intents = disnake.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=cfgData("BotSettings","command_prefix"), intents=intents)
name = cfgData("BotSettings","bot_name")

os.system(f'title {name}')

bot.add_cog(cog=errorCog(bot))
bot.remove_command('help')

@bot.event
async def on_ready():
    os.system('cls')
    log.succes(msg="Бот был успешно запущен")

@bot.slash_command(name="привет",description="привет")
async def hi(inter):
    await inter.response.send_message(f"Привет, {inter.author.name}")

if __name__ == "__main__":
    os.system('cls')

    def start():
        try:
            bot.run(cfgData("BotSettings","token"))
            return bot
        
        except api_exceptions.LoginFailure:
            log.error("Указан неверный токен, укажите верный токен для авторизации.")
            token = Animations.inputAnimate()
            cfg("cfg.ini").cfgUpdate("BotSettings","token",token)
            os.system('start main.py')

        except web_exceptions.ClientConnectionError:
            log.error("Нету подключения к интернету. Не можем запустить бота.")
        
    bot = start()