import asyncio

from hero import ExtensionConfig
from hero.utils import AsyncUsingDB, SyncToAsync, SyncToAsyncThreadSafe


class SchedulerConfig(ExtensionConfig):
    verbose_name = "Scheduler"


def schedulable(func):
    """Marks a controller method as schedulable."""
    if not asyncio.iscoroutinefunction(func) or isinstance(func, (AsyncUsingDB, SyncToAsync, SyncToAsyncThreadSafe)):
        raise TypeError('Schedulable controller method must be async.')

    func.schedulable = True
    return func
