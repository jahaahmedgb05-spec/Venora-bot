TOKEN = os.getenv("DISCORD_TOKEN")

if TOKEN:
    bot.run(TOKEN)
else:
    print("خطأ: لم يتم العثور على الـ Token الخاص بالبوت!")
