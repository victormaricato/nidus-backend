from apscheduler.schedulers.asyncio import AsyncIOScheduler

async def scheduler():
  schedule = AsyncIOScheduler()
  schedule.start()
  return schedule