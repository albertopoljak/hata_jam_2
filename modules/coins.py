from hata import discord, Message

from constants import TEST_GUILD
from database_handler import DatabaseHandler

from constants import ShopItem


braindead: discord.Client


async def get_coins_helper(user_id: int) -> int:
    query = "SELECT COINS FROM USERS WHERE ID=?"

    async with DatabaseHandler.get_connection().execute(query, (user_id,)) as cursor:
        results = await cursor.fetchone()
        if results is None:
            return 0
        else:
            return results[0]


async def change_coins_helper(user_id: int, *, num_coins: int) -> None:
    """Update coins helper. Pass positive to add and negative to deduct."""
    query = """
        INSERT INTO USERS (ID) VALUES(?) 
        ON CONFLICT(ID) 
        DO UPDATE SET COINS=COINS+?
    """
    await DatabaseHandler.get_connection().execute(query, (user_id, num_coins))
    await DatabaseHandler.get_connection().commit()


@braindead.events()
async def message_create(client, message: Message):
    if message.guild is None or message.author.is_bot:
        return

    await change_coins_helper(message.author.id, num_coins=1)


@braindead.interactions(guild=TEST_GUILD)
async def coins(client, event, user: ("user", "Specific user") = None):
    """Shows your Neko coins.

    1 coin is awarded for each message.
    """
    if user is None:
        user = event.user
        message = "You have {neko_coins} Neko coins"
    else:
        message = f"{user.full_name} has {{neko_coins}} Neko coins"

    neko_coins = await get_coins_helper(user.id)
    return message.format(neko_coins=neko_coins)


@braindead.interactions(guild=TEST_GUILD)
async def level(client, event):
    """Shows your Neko level based on your neko coins.

    Each 100 coins awards you 1 level.
    """
    neko_coins = await get_coins_helper(event.user.id)
    neko_level = neko_coins // 100
    return f"Your Neko level is {neko_level}."


@braindead.interactions(guild=TEST_GUILD)
async def buy(client, event, item: (ShopItem.item_choices(), "Buy cat items with your Neko coins (NC).")):
    """Buy cat items with your Neko coins (NC)."""
    neko_coins = await get_coins_helper(event.user.id)
    selected_item: ShopItem = ShopItem[item]
    new_balance = neko_coins - selected_item.price
    if new_balance < 0:
        return f"Not enough Neko coins :(\nYou're missing {abs(new_balance)} coins!"

    await change_coins_helper(event.user.id, num_coins=-selected_item.price)
    return (
        f"You bought {selected_item.friendly_name}! '*{selected_item.buy_message}*'\n"
        f"Your new balance is {new_balance}."
    )
