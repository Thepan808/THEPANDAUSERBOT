from userbot import *
from LEGENDBOT.utils import *
from userbot.cmdhelp import CmdHelp
from telethon import events, version
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User

#-------------------------------------------------------------------------------

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "LEGEND"

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

legend = bot.uid

mention = f"[{DEFAULTUSER}](tg://user?id={legend})"


PM_IMG = "https://telegra.ph/file/4f03f6d4e9521902eb57f.jpg"
pm_caption ="**𝖑𝖊ɠêɳ̃dẞø✞︎ 𝙸𝚜 𝙾𝚗𝚕𝚒𝚗𝚎**\n\n"

pm_caption += f"**┏🔥✞t͛ẞ̸ 𝖑𝖊ɠêɳ̃dẞø✞︎t🔥┓**\n"
pm_caption += f"**┣🚀 𝙼𝚢 𝙼𝚊𝚜𝚝𝚎𝚛    : {mention}**\n"
pm_caption += f"**┣🚀 𝚃𝚎𝚕𝚎𝚝𝚑𝚘𝚗 : `{version.__version__}`**\n"
pm_caption += f"**┣🚀 𝖑𝖊ɠêɳ̃dẞø✞︎ : {LEGENDversion}**\n"
pm_caption += f"**┣🚀 𝚂𝚞𝚍𝚘     : `{sudou}`**\n"
pm_caption += f"**┣🚀 𝙾𝚠𝚗𝚎𝚛     : [𝖑𝖊ɠêɳ̃d](https://t.me/The_LegendBoy)**\n"
pm_caption += f"**┗[♦️𝙶𝚛𝚘𝚞𝚙♦️](https://t.me/Legend_Userbot)┛**\n"

pm_caption += "    [✨яєρο✨](https://github.com/LEGEND-OS/LEGENDBOT) 🔹 [📜License📜](https://github.com/LEGEND-OS/LEGENDBOT/blob/master/LICENSE)"


@bot.on(admin_cmd(outgoing=True, pattern="bot$"))
@bot.on(sudo_cmd(pattern="bot$", allow_sudo=True))
async def amireallyalive(alive):
    if alive.fwd_from:
        return
    await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()


CmdHelp("alv").add_command(
  'alive', None, 'Check weather the bot is alive or not'
).add_command(
  'bot', None, 'Check weather the bot is alive or not. In your custom Alive Pic and Alive Msg'
).add_warning(
  "Harmless Module"
).add_info(
  'Are u alive?'
).add_type(
  "Official"
).add()
