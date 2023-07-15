import asyncio
import logging

from aiogram import Bot, Dispatcher

from config_data import Config, load_config
from handlers import user_handlers
from keyboards.main_menu import set_main_menu

logger = logging.getLogger(__name__)


async def run_bot():
    logging.basicConfig(
        level=logging.INFO,
        filename='services/bot_log.log',
        filemode='w',
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')
    logger.info('Starting bot')
    config: Config = load_config('.env')
    bot: Bot = Bot(token=config.bot.token, parse_mode='HTML')
    dp: Dispatcher = Dispatcher()
    await set_main_menu(bot)

    dp.include_router(user_handlers.router)
    try:
        await bot.send_message(chat_id=config.bot.admin, text='Бот запущен')
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(run_bot())
