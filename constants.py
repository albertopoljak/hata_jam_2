from enum import Enum
from typing import Dict

from hata import discord


TEST_GUILD = discord.Guild.precreate(633747521746763796)


class ShopItem(Enum):
    CATFOOD = 5, "Some catfood yum."
    WATER = 5, "Lick lick lick, ahhhh fresh!"
    PANTSU = 50, "Pantsu for catsu."
    CATNIP = 100, "You go brrrrrrrrrrrrrrrrr."
    CATTREE = 1000, "You spent so much coins and all you got is this lousy message."

    @property
    def friendly_name(self) -> str:
        """Don't yell at people."""
        return self.name.title()

    @property
    def price(self) -> int:
        return self.value[0]

    @property
    def buy_message(self) -> str:
        return self.value[1]

    @property
    def choice_string(self) -> str:
        """
        This wil be one of available choices.
        Since they can't have description everything has to be in the choice name itself.
        """
        return f"{self.friendly_name} {self.price}nc"

    @classmethod
    def item_choices(cls) -> Dict[str, str]:
        """This is used to typehint slash choices."""
        return {item.choice_string: item.name for item in cls}
