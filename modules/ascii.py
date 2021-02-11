import random

from hata import discord

from constants import TEST_GUILD


braindead: discord.Client
cat_ascii_images = (
    r"""
    ____
    (.   \
      \  |  
       \ |___(\--/)
     __/    (  . . )
    "'._.    '-.O.'
         '-.  \ "|\
            '.,,/'.,,
    """,
    r"""
     \    /\
      )  ( ')
     (  /  )
      \(__)|
    """,
    r"""
                             _
                            | \
                            | |
                            | |
       |\                   | |
      /, ~\                / /
     X     `-.....-------./ /
      ~-. ~  ~              |
         \             /    |
          \  /_     ___\   /
          | /\ ~~~~~   \ |
          | | \        || |
          | |\ \       || )
         (_/ (_/      ((_/
    """,
    r"""
     |\__/,|   (`\
     |_ _  |.--.) )
     ( T   )     /
    (((^_(((/(((_>
    """,
    r"""
     /\_/\
    ( o.o )
     > ^ <
    """,
    r"""
      \`*-.                   
       )  _`-.                
      .  : `. .               
      : _   '  \              
      ; *` _.   `*-._         
      `-.-'          `-.      
        ;       `       `.    
        :.       .        \   
        . \  .   :   .-'   .  
        '  `+.;  ;  '      :  
        :  '  |    ;       ;-.
        ; '   : :`-:     _.`* ;
     .*' /  .*' ; .*`- +'  `*'
     `*-*   `*-*  `*-*'        
    """,
    r"""
                      .-.
                       \ \
                        \ \
                         | |
                         | |
       /\---/\   _,---._ | |
      /^   ^  \,'       `. ;
     ( O   O   )           ;
      `.=o=__,'            \
        /         _,--.__   \
       /  _ )   ,'   `-. `-. \
      / ,' /  ,'        \ \ \ \
     / /  / ,'          (,_)(,_)
    (,;  (,,)                    
    """,
    r"""
     /\_/\
     >^.^<.---.
    _'-`-'     )\
   (6--\ |--\ (`.`-.
       --'  --'  ``-'BP 
    """
)

cat_ascii_emojis = (
    "^._.^= ∫",
    "/ᐠ｡ꞈ｡ᐟ\\",
    "✧/ᐠ-ꞈ-ᐟ\\",
    "₍⸍⸌̣ʷ̣̫⸍̣⸌₎",
    "[^._.^]ﾉ彡",
    "ᨐ ∫"
)


@braindead.interactions(guild=TEST_GUILD)
async def cat_ascii_image(client, event):
    """Get random cat ascii image art."""
    return f"```{random.choice(cat_ascii_images)}```"


@braindead.interactions(guild=TEST_GUILD)
async def cat_ascii_emoji(client, event):
    """Get random cat ascii emoji art."""
    return f"`{random.choice(cat_ascii_emojis)}`"
