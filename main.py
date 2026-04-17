import asyncio
from aiogram import Bot, Dispatcher
from src.commands.select_group import group
from src.commands import feeadback_and_report, start, \
    schedule, help, admin, send_info_update, send_logs
from src.commands.cache_update import cache_update
from src.lessons.week import week
import os
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv
from src.cache_group_users import launch
from src.logic_logs.file.logger import logger



load_dotenv()
async def main():
    bot = Bot(token=os.getenv('TOKEN_BOT'))
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_routers( 
        cache_update.router, feeadback_and_report.router, 
        group.router, start.router, 
        week.router, schedule.router,
        help.router, admin.router,
        send_info_update.router,
        launch.router, send_logs.router,
    )
    logger.info("Бот запущен")
    await bot.delete_webhook(drop_pending_updates=True) 
    await dp.start_polling(bot)

asyncio.run(main())