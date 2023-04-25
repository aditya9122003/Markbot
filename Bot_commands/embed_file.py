from datetime import datetime
from sqlite3 import Timestamp
from attr import field
import discord
def embed_message(items):
    embed = discord.Embed(
        title = str(items[0]),
        description = str(items[1]),
        colour = discord.Color.blue(),
        timestamp = datetime.now()
    )
    embed.add_field(name = "Seller", value=str(items[2]), inline = True)
    # embed.set_footer(text = "footer")
    embed.set_image(url=str(items[4]))
    embed.set_thumbnail(url=str(items[5]))
    embed.set_author(name="author", icon_url="https://images.pexels.com/photos/247502/pexels-photo-247502.jpeg")
    embed.add_field(name="Price", value=str(items[3]), inline=True)

    # print("this gets executed")
    # embed = "hi"
    return embed