import asyncio
import logging
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger(__name__)

bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message) -> None:
    """Handle /start command."""
    await message.answer(
        f"Привет, {message.from_user.full_name}! 👋\n"
        "Я простой Telegram-бот на Python.\n"
        "Напиши /help, чтобы узнать список команд."
    )


@dp.message(Command("help"))
async def cmd_help(message: Message) -> None:
    """Handle /help command."""
    await message.answer(
        "📋 Доступные команды:\n"
        "/start — приветственное сообщение\n"
        "/help  — список команд\n"
        "/echo  — бот повторит твоё следующее сообщение"
    )


@dp.message(Command("echo"))
async def cmd_echo(message: Message) -> None:
    """Ask user to send a message to echo."""
    await message.answer("Напиши любое сообщение, и я его повторю!")


@dp.message()
async def echo_handler(message: Message) -> None:
    """Echo all non-command messages."""
    await message.answer(message.text or "(не текстовое сообщение)")


async def main() -> None:
    logger.info("Starting bot...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
