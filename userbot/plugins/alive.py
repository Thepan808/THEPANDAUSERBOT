import time
import random
import time
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot
from userbot.Config import Config
from telethon import version
import time
from userbot import ALIVE_NAME, LEGENDversion
from LEGENDBOT.utils import admin_cmd, edit_or_reply, sudo_cmd, time_formatter
from userbot.cmdhelp import CmdHelp
from . import *

uptime = get_readable_time((time.time() - StartTime))
DEFAULTUSER = ALIVE_NAME or "๐๐ษ รชษณฬdแบรธโ๏ธ ๐ฎ๐ณ"
LEGEND_IMG = Config.ALIVE_PIC
CUSTOM_ALIVE_TEXT = Config.ALIVE_MSG or "โัgัะธโ Choice ๐๐ษ รชษณฬdแบรธโ๏ธ"
CUSTOM_YOUR_GROUP =Config.YOUR_GROUP or "@Legend_Userbot"

Legend = bot.uid
mention = f"[{DEFAULTUSER}](tg://user?id={Legend})"

@bot.on(admin_cmd(outgoing=True, pattern="legend$"))
@bot.on(sudo_cmd(pattern="legend$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    reply_to_id = await reply_id(alive)

    if  LEGEND_IMG:
        LEGEND_caption = f"**{CUSTOM_ALIVE_TEXT}**\n"
        
        LEGEND_caption += f"~~~~~~~~~~~~~~~~~~~~~~~\n"
        LEGEND_caption += f"        **โ๐ญ๐โ  ๐พ๐๐๐๐๐โ** \n"
        LEGEND_caption += f"โข๐ฅโข **Oีกีฒฬาฝฬษพ**          ~ {ALIVE_NAME}\n\n"
        LEGEND_caption += f"โขโฆโข **๐๐ษ รชษณฬdแบรธโ **ย   ~ {LEGENDversion}\n"
        LEGEND_caption += f"โขโฆโข **โ าฝฬlาฝฬthรธีฒฬ**     ~ `{version.__version__}`\n"
        LEGEND_caption += f"โขโฆโข **๐ฯtime**         ~ `{uptime}`\n"
        LEGEND_caption += f"โขโฆโข **๐ถ๐๐๐๐**           ~ [๐ถ๐๐๐๐](t.me/Legend_Userbot)\n"
        LEGEND_caption += f"โขโฆโข **๐ผ๐ข ๐ถ๐๐๐๐**  ~ {CUSTOM_YOUR_GROUP}\n"   

        await alive.client.send_file(
            alive.chat_id, LEGEND_IMG, caption=LEGEND_caption, reply_to=reply_to_id
        )
        await alive.delete()
    else:
        await edit_or_reply(
            alive,
            f"**{CUSTOM_ALIVE_TEXT}**\n\n"
            f"~~~~~~~~~~~~~~~~~~~~~~~ \n"
            f"         \n"
            f"โขโกโข ๐ฟัโัฯะฝฮฟะธ    : `{version.__version__}`\n"
            f"โฆ โัgัะธโฯฮฟฯ  : `{LEGENDversion}`\n"
            f"โฆ ฯฯฯฮนะผั        : `{uptime}`\n"
            f"๐ฑ ษฑฮฑเธฃฦญฮตษพ        : {mention}\n"
            f"๐ฑ ฯฯษณฮตษพ         : [โัgัะธโ](t.me/The_LegendBoy)\n"
        )


msg = f"""
**  โ๏ธ โ  The Panda โ  ฮนั ฯะธโฮนะธั โ๏ธ**

       {Config.ALIVE_MSG}
    **  Bรธโ๏ธ แบโ๏ธฮฑโ๏ธยตั **
**โขโ๏ธโขรีกีฒฬาฝฬr     :** **{mention}**
**โขโฆโข๐๐ษ รชษณฬdแบรธโ๏ธ  :** {LEGENDversion}
**โขโฆโขโ๏ธาฝฬlาฝฬฦญhรธีฒ  :** {version.__version__}
**โขโฆโขรbรปรรช     :**  {abuse_m}
**โขโฆโขรudรธ      :**  {is_sudo}
**โขโฆโขBรธt.      :** {Config.BOY_OR_GIRL}
"""
botname = Config.BOT_USERNAME

@bot.on(admin_cmd(pattern="alive$"))
@bot.on(admin_cmd(pattern="alive$", allow_sudo=True))
async def legend_a(event):
    try:
        legend = await bot.inline_query(botname, "alive")
        await legend[0].click(event.chat_id)
        if event.sender_id == The_LegendBoy:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg)

CmdHelp("alive").add_command(
    "bot", None, "ฯัั ฮฑะธโ ััั"
).add_command(
    "legend", None, "Its Same Like Alive"
).add_command(
    "alive", None, "Its Show ur Alive Template"
).add_warning(
    "Harmless Moduleโ"
).add_info(
     "Checking Alive"
).add_type(
    "Official"
).add()
