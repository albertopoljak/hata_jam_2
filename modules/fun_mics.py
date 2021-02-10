import random
from collections import namedtuple

from hata import discord, DiscordException

from constants import TEST_GUILD, GREEN_COLOR


braindead: discord.Client

NekoName = namedtuple("NekoName", ("name", "meaning"))
neko_names = (
    NekoName("Akemi", "bright beautiful"),
    NekoName("Akiko", "bright child"),
    NekoName("Akira", "bright / clear"),
    NekoName("Aiko", "child of love"),
    NekoName("Airi", "love jasmine"),
    NekoName("Asami", "morning beauty"),
    NekoName("Asuka", "tomorrow perfume, fragrance"),
    NekoName("Ayame", "iris"),
    NekoName("Ayano", "my color"),
    NekoName("Ceiko", "child of splendor"),
    NekoName("Chieko", "child of intelligence, wisdom"),
    NekoName("Chika", "scatter flowers"),
    NekoName("Chiyo", "one thousand generations"),
    NekoName("Chiyoko", "child of a thousand generations"),
    NekoName("Emi", "beautiful blessing"),
    NekoName("Emiko", "beautiful blessing child"),
    NekoName("Eri", "blessed prize"),
    NekoName("Etsuko", "child of joy"),
    NekoName("Fumiko", "child of abundant beautyFemale"),
    NekoName("Hana", "flower"),
    NekoName("Hanako", "flower child"),
    NekoName("Haru", "spring"),
    NekoName("Haruko", "spring child"),
    NekoName("Haruna", "spring vegetables"),
    NekoName("Hideko", "child of excellence"),
    NekoName("Hikari", "light, radiance"),
    NekoName("Hina", "sun vegetables"),
    NekoName("Hisako", "child of long life"),
    NekoName("Hiro", "generous"),
    NekoName("Hiroko", "generous child"),
    NekoName("Hiromi", "generous beauty"),
    NekoName("Hitomi", "pupil of the eye"),
    NekoName("Honoka", "harmony flower"),
    NekoName("Hoshi", "star"),
    NekoName("Hoshiko", "star child"),
    NekoName("Hotaru", "firefly"),
    NekoName("Izumi", "spring, fountain"),
    NekoName("Kamiko", "superior child"),
    NekoName("Katsumi", "victorious beauty"),
    NekoName("Kazumi", "harmonious beauty"),
    NekoName("Kazuko", "child of harmony"),
    NekoName("Keiko", "blessed child / respectful child"),
    NekoName("Kiko", "chronical child"),
    NekoName("Kimi", "noble"),
    NekoName("Kimiko", "empress child"),
    NekoName("Kiyomi", "pure beauty"),
    NekoName("Kumiko", "long–time beautiful child"),
    NekoName("Kyo", "cooperation"),
    NekoName("Kyoko", "respectful child"),
    NekoName("Madoka", "circle, round"),
    NekoName("Mai", "dance"),
    NekoName("Maki", "true hope"),
    NekoName("Maiko", "child of dance"),
    NekoName("Makoto", "sincere"),
    NekoName("Mami", "true beauty"),
    NekoName("Mana", "love"),
    NekoName("Manami", "loving beautiful"),
    NekoName("Mao", "dance cherry blossom"),
    NekoName("Masa", "just / true"),
    NekoName("Masumi", "true clarity"),
    NekoName("Mariko", "true village child"),
    NekoName("Mayumi", "true gentle beauty"),
    NekoName("Mi", "beautiful"),
    NekoName("Michi", "pathway"),
    NekoName("Michiko", "beautiful wise child"),
    NekoName("Midori", "green"),
    NekoName("Mieko", "beautiful blessing child"),
    NekoName("Miho", "protected, guaranteed beauty"),
    NekoName("Mika", "beautiful fragrance"),
    NekoName("Miki", "beautiful princess"),
    NekoName("Miku", "beautiful sky"),
    NekoName("Minako", "beautiful child"),
    NekoName("Minori", "truth"),
    NekoName("Mio", "beautiful cherry blossom"),
    NekoName("Misaki", "beautiful blossom"),
    NekoName("Mitsuko", "child of light"),
    NekoName("Mitsuru", "satisfy, full"),
    NekoName("Miwa", "beautiful hamony, peace"),
    NekoName("Miyako", "beautiful night child"),
    NekoName("Miyu", "beautiful gentle"),
    NekoName("Miyuki", "beautiful blessing"),
    NekoName("Momoka", "peach tree flower"),
    NekoName("Moriko", "child of the forest"),
    NekoName("Nana", "seven"),
    NekoName("Nanami", "seven seas"),
    NekoName("Nao", "honest"),
    NekoName("Naoko", "honest child"),
    NekoName("Naomi", "honest beautiful"),
    NekoName("Natsuki", "summer hope"),
    NekoName("Natsumi", "beautiful summer"),
    NekoName("Nobuko", "faithful, trustworthy child"),
    NekoName("Noriko", "lawful child"),
    NekoName("Ren", "lotus / love"),
    NekoName("Rin", "dignified"),
    NekoName("Rina", "jasmine"),
    NekoName("Rio", "village cherry blossom"),
    NekoName("Rika", "true fragrance"),
    NekoName("Riko", "child of truth"),
    NekoName("Ryoko", "refreshing child"),
    NekoName("Sachiko", "joyful, happy child"),
    NekoName("Saki", "blossom of hope"),
    NekoName("Sakura", "cherry blossom"),
    NekoName("Satoko", "wise child"),
    NekoName("Satomi", "beautiful and wise"),
    NekoName("Shinju", "pearl"),
    NekoName("Shiori", "poem"),
    NekoName("Shigeko", "growing child"),
    NekoName("Shika", "deer"),
    NekoName("Shizuka", "quiet summer"),
    NekoName("Shizuko", "quiet child"),
    NekoName("Sora", "sky"),
    NekoName("Sumiko", "child of clarity"),
    NekoName("Suzu", "bell"),
    NekoName("Suzume", "sparrow"),
    NekoName("Takako", "noble child"),
    NekoName("Takara", "treasure"),
    NekoName("Tamiko", "child of many beauties"),
    NekoName("Teruko", "shining child"),
    NekoName("Tomomi", "beautiful friend"),
    NekoName("Tomiko", "child of wealth, fortune"),
    NekoName("Toshiko", "clever child"),
    NekoName("Umeko", "plum child"),
    NekoName("Yasu", "peace iness / snow"),
    NekoName("Yasuko", "child of peace"),
    NekoName("Yoko", "child of sunlight"),
    NekoName("Yoshi", "lucky / righteous"),
    NekoName("Yoshie", "beautiful stream"),
    NekoName("Yoshiko", "child of goodness"),
    NekoName("Yua", "binding love"),
    NekoName("Yuina", "bind together"),
    NekoName("Yuka", "gentle flower"),
    NekoName("Yukari", "beautiful pear tree"),
    NekoName("Yumi", "reason beautiful"),
    NekoName("Yumiko", "reason beautiful child"),
    NekoName("Yui", "bind clothing"),
    NekoName("Yuki", "happy"),
    NekoName("Yukiko", "child of snow / child of happiness"),
    NekoName("Yuko", "gentle child"),
    NekoName("Yuri", "lily"),
    NekoName("Yuriko", "lily child"),
    NekoName("Yuuna", "gentle"),
)


@braindead.interactions(guild=TEST_GUILD)
async def catify(client, event, user: ("user", "Specific user") = None):
    """Change your or someone else nickname to random cat name."""

    choice = random.choice(neko_names)
    if user is None:
        user = event.user

    previous_nickname = user.name_at(event.guild)

    try:
        await client.user_edit(event.guild, user, nick=choice.name)
    except DiscordException:
        return discord.Embed("Missing permission", "Can't change nickname as I don't have required permission.")

    return discord.Embed(
        title="Catified!",
        description=f"{previous_nickname} is now known as **{choice.name}** meaning *{choice.meaning}*.",
        color=GREEN_COLOR
    )


@braindead.interactions(guild=TEST_GUILD)
async def best_neko(client, event):
    """Shows you the best neko girl!"""
    best_neko_user = await client.user_get(184734189386465281)
    return discord.Embed(title=best_neko_user.full_name).add_image(url=best_neko_user.avatar_url_as(size=4096))
