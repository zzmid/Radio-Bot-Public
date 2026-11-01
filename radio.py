import os
import discord
from discord.ext import commands

TOKEN = os.getenv("TOKEN")

RADIO_CHANNEL_ID = int(os.getenv("RADIO_CHANNEL_ID") or 0)
LOG_CHANNEL_ID = int(os.getenv("LOG_CHANNEL_ID") or 0)
DELETE_AFTER_SECONDS = int(os.getenv("DELETE_AFTER_SECONDS") or 7200)  # 2 hours

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} ({bot.user.id})")


@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return

    if message.channel.id == RADIO_CHANNEL_ID:

        log_channel = bot.get_channel(LOG_CHANNEL_ID)

        # log who really sent it
        if log_channel:
            embed = discord.Embed(
                title="Radio Log",
                description=message.content if message.content else "*No text*",
                color=discord.Color.dark_gray()
            )

            embed.add_field(
                name="Sender",
                value=f"{message.author} (<@{message.author.id}>)",
                inline=False
            )

            embed.add_field(name="Sender ID", value=str(message.author.id))
            embed.add_field(name="Message ID", value=str(message.id))

            embed.set_footer(
                text=f"{message.created_at.strftime('%Y-%m-%d %H:%M:%S UTC')}"
            )

            await log_channel.send(embed=embed)

        # delete the original so nobody sees who sent it
        try:
            await message.delete()
        except discord.Forbidden:
            return

        # repost it as the radio
        radio_embed = discord.Embed(
            description=(
                f"*A voice comes through the radio...*\n\n"
                f"{message.content}"
            ),
            color=discord.Color.dark_gray()
        )

        await message.channel.send(
            embed=radio_embed,
            delete_after=DELETE_AFTER_SECONDS
        )

    await bot.process_commands(message)


if not TOKEN:
    raise ValueError("No TOKEN found in environment variables.")

if not RADIO_CHANNEL_ID:
    raise ValueError("No RADIO_CHANNEL_ID found in environment variables.")

bot.run(TOKEN)
