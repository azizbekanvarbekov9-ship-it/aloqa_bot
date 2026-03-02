"""Ushbu funcsiya botni 3 soniyaga tohtatadi va typing ni korsatadi"""
from aiogram import Bot
from aiogram.types import Message
from aiogram.utils.chat_action import ChatActionSender
from asyncio import sleep


async def command_start_answer(message: Message, bot: Bot):
    """ushbu funcsiya foydalanuvchi star ni bosganda
    Assalomu alaykum ni yuboradi"""
    async with ChatActionSender.typing(message.from_user.id, bot):
        await sleep(3)
        await message.answer("Assalomu alaykum")

async def echo (message: Message, bot: Bot):
    """Ushbi funcsiya foydalanuvchi botga habar yuborganda habani yuboradi"""
    async with ChatActionSender.typing(message.from_user.id, bot):
        await sleep(3)
        await message.forward(chat_id=2132289405 )
        await message.answer("Xabaringiz yetkazildi! iltimos kuting.")
