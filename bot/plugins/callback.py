# Cleaned & Refactored by @Mak0912 (TG)

from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from info import Config
from pyrogram import __version__

@Client.on_callback_query(filters.regex("^about$"))
async def about_callback(client, query: CallbackQuery):
    text = f"""
<b>✨ Chatmola hai pardhan </b>

👨‍💻 <b>Developer:</b> <a href='tg://user?id={Config.OWNER_ID}'>This Person</a>
📢 <b>Backup Channel:</b> <a href='https://t.me/+KLY3ssrtdNY4MjM1'>𝙏𝙃𝙀 𝙋𝙎 𝘽𝙊𝙏𝙎</a>
💬 <b>Support:</b> <a href='https://t.me/Cutehubsupport_bot'>𝙋𝙎 - 𝘿𝙄𝙎𝘾𝙐𝙎𝙎𝙄𝙊𝙉</a>
"""
    await query.message.edit_text(
        text=text,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🔒 Close", callback_data="close")]
        ])
    )

@Client.on_callback_query(filters.regex("^close$"))
async def close_callback(client, query: CallbackQuery):
    await query.message.delete()
    try:
        await query.message.reply_to_message.delete()
    except:
        pass
