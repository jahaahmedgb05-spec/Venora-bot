import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from flask import Flask
from threading import Thread

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# باش البوت ميطفاش 24/24 فـ Railway
app = Flask('')
@app.route('/')
def home():
    return "Venora Bot is alive!"
def run():
  app.run(host='0.0.0.0',port=8080)
def keep_alive():
    t = Thread(target=run)
    t.start()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} خدام دابا')

@bot.command()
async def ping(ctx):
    await ctx.send("Pong! Venora خدامة 🏓")

keep_alive()
bot.run(TOKEN)
