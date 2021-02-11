from urllib import parse

from hata import discord

from constants import TEST_GUILD


braindead: discord.Client


@braindead.interactions(guild=TEST_GUILD)
async def neko_image(
        client,
        event,
        category: ({"Kitsune": "kitsune", "NSFW": "nekolewd"}, "Which category?") = "neko"
):
    """Get image of neko."""
    response = await client.http.get(f"https://neko-love.xyz/api/v1/{category}")
    url = (await response.json())["url"]
    return discord.Embed().add_image(url)


@braindead.interactions(guild=TEST_GUILD)
async def which_cat(client, event):
    """Which cat are you today?"""
    encoded_name = parse.quote(event.user.full_name, safe="")
    response = await client.http.get(f"https://cataas.com/cat/says/{encoded_name}")
    return discord.Embed().add_image(str(response.url))
