from userbot import bot
from sys import argv
import sys
import os
from telethon import TelegramClient
from var import Var
from userbot.Config import Config
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest
from userbot.utils import load_module, start_assistant, load_addons, load_abuse 
from userbot.utils import *
from userbot import LOAD_PLUG, LOGS, LEGENDversion
from pathlib import Path
import asyncio
import glob
import telethon.utils
os.system("pip install -U telethon")

l2= Config.SUDO_COMMAND_HAND_LER
LEGEND_PIC = "https://telegra.ph/file/331263e3cc2770706645a.mp4"
l1 = Config.COMMAND_HAND_LER
import os
os.system("pip install safety-ub")
from safety import StartSafety as safe
            
async def add_bot(bot_token):
    try:
        await bot.start(bot_token)
        bot.me = await bot.get_me()
        bot.uid = telethon.utils.get_peer_id(bot.me)
    except Exception as e:
        print(f"LEGEND_STRING - {str(e)}")
        sys.exit()
        
        
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    try:
        if Var.BOT_USERNAME is not None:
            LOGS.info("Checking Telegram Bot Username...")
            bot.tgbot = TelegramClient(
                "BOT_TOKEN", api_id=Var.APP_ID, api_hash=Var.API_HASH
            ).start(bot_token=Var.BOT_TOKEN)
            LOGS.info("Checking Completed. Proceeding to next step...")
            LOGS.info("♥️ Starting LegendBot ♥️")
            bot.loop.run_until_complete(add_bot(Config.BOT_USERNAME))
            LOGS.info("🥇🔥 LegendBot Startup Completed 🔥🥇")
        else:
            bot.start()
    except Exception as e:
        LOGS.error(f"BOT_TOKEN - {str(e)}")
        sys.exit()

print("📍⚜Loading Modules / Plugins⚜✔")


async def module():
  import glob
  path = 'userbot/plugins/*.py'
  files = glob.glob(path)
  for name in files:
    with open(name) as f:
      path1 = Path(f.name)
      shortname = path1.stem
      load_module(shortname.replace(".py", ""))
    
assistant = os.environ.get("ASSISTANT", None)
async def assistants():
    if assistant == "ON":
        extra_repo = "https://github.com/LEGEND-OS/assistant"
        try:
            os.system(f"git clone {extra_repo}")  
        except BaseException:
            pass
        import glob
        LOGS.info("🤖Loading Assistant Plugin🤖")
        path = "assistant/*.py"
        files = glob.glob(path)
        for name in files:
            with open(name) as ex:
                path2 = Path(ex.name)
                shortname = path2.stem
                try:
                    start_assistant(shortname.replace(".py", ""))
                    if not shortname.startswith("__") or shortname.startswith("_"):
                        LOGS.info(f"[LEGEND-BOT 3.0] - Assistant -  🤴Installed🤴 - {shortname}")
                except Exception as e:
                    LOGS.warning(f"[LEGEND-BOT 3.0] - Assistant - ⚠️⚡ERROR⚡⚠️ - {shortname}")
                    LOGS.warning(str(e))
    else:
        print("Addons Not Loading")
addon = os.environ.get("EXTRA_PLUGIN", None)             
async def addons():
    if addon == "ON":
        extra_repo = "https://github.com/LEGEND-OS/LegendBot-Addons"
        try:
            os.system(f"git clone {extra_repo}")  
        except BaseException:
            pass
        import glob
        LOGS.info("🔱🏆Loading Extra Plugin🏆🔱")
        path = "LegendBot-Addons/*.py"
        files = glob.glob(path)
        for name in files:
            with open(name) as ex:
                path2 = Path(ex.name)
                shortname = path2.stem
                try:
                    load_addons(shortname.replace(".py", ""))
                    if not shortname.startswith("__") or shortname.startswith("_"):
                        LOGS.info(f"[LEGEND-BOT 2.1] - Addons -  ✅Installed✅ - {shortname}")
                except Exception as e:
                    LOGS.warning(f"[LEGEND-BOT 2.1] - Addons - ⚠️⚡ERROR⚡⚠️ - {shortname}")
                    LOGS.warning(str(e))
    else:
        print("Addons Not Loading")
        
abuse = os.environ.get("ABUSE", None) 
async def abuses():
    if abuse == "ON":
        abuse_repo = "https://github.com/LEGEND-OS/ABUSE"
        try:
            os.system(f"git clone {abuse_repo}")  
        except BaseException:
            pass
        import glob
        LOGS.info("🤬🤪 Loding Abuse 🤪🤬")
        path = "ABUSE/*.py"
        files = glob.glob(path)
        for name in files:
            with open(name) as ex:
                path2 = Path(ex.name)
                shortname = path2.stem
                try:
                    load_abuse(shortname.replace(".py", ""))
                    if not shortname.startswith("__") or shortname.startswith("_"):
                        LOGS.info(f"[LEGEND-BOT 2.1] - Abuse -  🔥📍Installed✔ - {shortname}")
                except Exception as e:
                    LOGS.warning(f"[LEGEND-BOT 2.1] - Abuse - ⚠️⚡ERROR⚡⚠️ - {shortname}")
                    LOGS.warning(str(e))
    else:
        print("Abuse Not Loading")

async def fetch_plugins_from_channel():
    """Fetch Plugins From Channel"""
    try:
        async for message in bot.search_messages(
            Config.PLUGIN_CHANNEL, filter="document", query=".py"
        ):
            hmm = message.document.file_name
            if not os.path.exists(os.path.join("./userbot/plugins/", hmm)):
                await bot.download_media(message, file_name="./userbot/plugins/")
    except BaseException as e:
        LOGS.warning(f"Failed! To Install Plugins From Plugin Channel Due To {e}!")
        return
    LOGS.info("All Plugins From Plugin Channel Loaded!")


bot.loop.run_until_complete(module())
bot.loop.run_until_complete(addons())
bot.loop.run_until_complete(abuses())
bot.loop.run_until_complete(assistants())


print(f"""♥️♦♥️⚜♥️
╔════❰THEPANDABOT❱═❍⊱❁۪۪
║┣⪼ Criador - BAIANOR
║┣⪼ Grupo - NEM TENHO
║┣⪼ CRIADOR - ZZZ
║┣⪼ TELETHON - 1.2.0
║┣⪼ ✨ 『🔱🇱 🇪 🇬 🇪 🇳 🇩 🔱』T H E ♦ P A N D A✨
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍⊱""")

async def legend_is_on():
    try:
        safe()
        if Config.LOGGER_ID != 0:
            await bot.send_file(
                Config.LOGGER_ID,
                LEGEND_PIC,
                caption=f"#START \nEstou online parceiro com Sucesso\n\n**Versão- {LEGENDversion}**\n\nDigite `{l1}help` or `{l1}ping` para checar! \n\nEntre [No Canal parceiro](t.me/GR4V3_S4D_CRAZZY) & [No grupo fiato](t.me/blazer808_Stay) É nós fela da pota",
            )
    except Exception as e:
        print(str(e))

# Join LegndBot Channel after deploying 🤐😅
    try:
        await bot(JoinChannelRequest("@GR4V3_S4D_CRAZZY"))
    except BaseException:
        pass

    try:
        await bot(JoinChannelRequest("@blazer808_Stay"))
    except BaseException:
         pass

bot.loop.create_task(legend_is_on())
if len(sys.argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    bot.run_until_disconnected()
