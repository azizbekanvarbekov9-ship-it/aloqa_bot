"""Ushbu dastur main ni bajaradi"""
from asyncio import run


from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties


import message

from config import TOKEN
dp = Dispatcher()


async def startup_answer(bot: Bot):
    """ushbu funcsiya bot ishga tushsa habarni yuboradi"""
    await bot.send_message(2132289405, "Bot ishga tushdi! ✅")

async def shutdown_answer(bot: Bot):
    """ushbu funcsiya bot ishdan to'xtasa habarni yuboradi"""
    await bot.send_message(2132289405, "Bot ishdan to'xtadi! ❗")


async def start():
    """Ushbu funcsiya qolgan funcsiyalarni bajaradi"""
    dp.startup.register(startup_answer)
    dp.shutdown.register(shutdown_answer)
    dp.include_router(message.router)

    bot = Bot(
        token=(TOKEN),
        default=DefaultBotProperties(parse_mode='HTML'),
    )

    await dp.start_polling(bot, polling_timeout=1)

run(start())
