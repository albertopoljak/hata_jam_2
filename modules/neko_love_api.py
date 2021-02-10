from hata import discord

from constants import TEST_GUILD


braindead: discord.Client
BASE_API_URL = "https://neko-love.xyz/api/v1/"


async def api_get(base_url: str, endpoint: str) -> str:
    response = await braindead.http.get(f"{base_url}{endpoint}")
    return (await response.json())["url"]


@braindead.interactions(guild=TEST_GUILD)
async def neko_image(
        client,
        event,
        category: ({"Kitsune": "kitsune", "NSFW": "nekolewd"}, "Which category?") = "neko"
):
    """Get image of neko."""
    url = await api_get(BASE_API_URL, category)
    embed = discord.Embed()
    embed.add_image(url)
    return embed
