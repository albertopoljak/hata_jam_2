from hata import discord

from constants import TEST_GUILD


braindead: discord.Client


async def neko_api_get(endpoint: str) -> str:
    response = await braindead.http.get(f"https://neko-love.xyz/api/v1/{endpoint}")
    return (await response.json())["url"]


@braindead.interactions(guild=TEST_GUILD)
async def neko_image(
        client,
        event,
        category: ({"Kitsune": "kitsune", "NSFW": "nekolewd"}, "Which category?") = "neko"
):
    """Get image of neko."""
    url = await neko_api_get(category)
    embed = discord.Embed()
    embed.add_image(url)
    return embed
