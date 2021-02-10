import os
from time import perf_counter

from hata import Client, start_clients
from hata.ext.slash import setup_ext_slash
from hata.ext import asyncio as hata_asyncio  # noqa
from hata.ext.commands import setup_ext_commands
from hata.ext.extension_loader import EXTENSION_LOADER

from database_handler import DatabaseHandler


braindead = Client("YOUR_TOKEN_HERE")
setup_ext_commands(braindead, "!")
setup_ext_slash(braindead)


@braindead.events
async def ready(client):
    print(f"{client:f} logged in.")
    await DatabaseHandler.create_connection()


@braindead.commands
async def ping(client, message):
    """Simple ping command for debug purposes."""
    start = perf_counter()
    msg = await braindead.message_create(message.channel, "Ping!")
    difference = perf_counter() - start
    await braindead.message_edit(msg, f":ping_pong: {difference*100:.2f}ms")


EXTENSION_LOADER.add_default_variables(braindead=braindead)

for name in os.listdir("modules"):
    if name.endswith(".py"):
        EXTENSION_LOADER.add(f"modules.{name[:-3]}")

EXTENSION_LOADER.load_all()
start_clients()
