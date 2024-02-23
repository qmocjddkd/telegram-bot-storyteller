import logging
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from handlers import rt
import asyncio

logger = logging.getLogger(__name__)
logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

async def main():
    logger.info('Starting bot')
    
    bot = Bot(token='6816197087:AAHq2ZGIPm76xC6S0JsZYQX4Kt6vuk2-sc8')
    dp = Dispatcher()
    dp.include_router(rt)
    await bot.set_my_commands([
        BotCommand(command="/start", description="Запуск бота|Start bot"),
        BotCommand(command="/help", description="Показать формат сказки|Show the format of the fairy tale")
    ])
    # await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main())
