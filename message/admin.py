"""Ushbu dastur habarlarni yuborish uchun"""
from aiogram.types import Message

async def admin_message(message: Message):
    """Ushbu funcsiya habar yuborsa habar yuborildi deb yuboradi,
    Agar reply qilib yozilmasa habarni yuboradi"""
    if message.reply_to_message:
        await message.copy_to(chat_id=message.reply_to_message.forward_from.id)
        await message.answer("👌 Habaringiz yuborildi")
    else:
        await message.answer(" Kimgadir yozmoqchi bolsangzi uni xabariga reply qilib yozing.")
