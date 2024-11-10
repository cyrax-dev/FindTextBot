import asyncio

from aiogram import Bot, Dispatcher

from src.handlers.command_handler import command_router
from src.handlers.callback_handler import callback_router
from src.utils import Config


config = Config()
bot = Bot(token=config.token)
dp = Dispatcher()


@dp.startup()
async def ready():
    print("Бот запущен")


async def main() -> None:
    dp.include_routers(command_router, callback_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
