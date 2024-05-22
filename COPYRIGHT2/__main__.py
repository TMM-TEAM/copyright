import asyncio
import importlib
from pyrogram import idle
from COPYRIGHT2 import COPYRIGHT2
from COPYRIGHT2.modules import ALL_MODULES

LOGGER_ID = -1001801976314

loop = asyncio.get_event_loop()

async def daxxpapa_boot():
    for all_module in ALL_MODULES:
        importlib.import_module("COPYRIGHT2.modules." + all_module)
    print("𝖻𝗈𝗍 𝗌𝗎𝖼𝖼𝖾𝗌𝗌𝖿𝗎𝗅 𝗌𝗍𝖺𝗋𝗍")
    await idle()
    print("lowde coder ke baal coder bnega aa gya na error jao baap se jakr error solve krwao @moh_maya_officisl")
    await COPYRIGHT2.send_message(LOGGER_ID, "**𝖨 𝖺𝗆 𝖺𝗅𝗂𝗏𝖾 𝖡𝖺𝖻𝗒 𝖸𝗈𝗎𝗋 𝖡𝗈𝗍 𝖲𝗎𝖼𝖼𝖾𝗌𝗌𝖿𝗎𝗅 𝖣𝖾𝗉𝗅𝗈𝗒 \n Mʏ Dᴇᴠᴇʟᴏᴘᴇʀ  [˹ 𝗠𝗥 मोह माया˼ [⛦⃕͜🇮🇳]](https://t.me/moh_maya_official)**")

if __name__ == "__main__":
    loop.run_until_complete(daxxpapa_boot())
    
