import discord
from discord.ext import commands, tasks

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)
activity1 = discord.Game(name="Hello")
activity2 = discord.Game(name="I am Groot")
switch_interval = 30
current_activity = 1
current_status = discord.Status.online

# Define the user ID that can execute restricted commands
allowed_user_id = YOUR_ALLOWED_USER_ID_HERE

def check_author(ctx):
    return ctx.author.id == allowed_user_id

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    await bot.change_presence(status=current_status, activity=activity1)
    switch_activity.start()

@tasks.loop(seconds=switch_interval)
async def switch_activity():
    global current_activity
    if current_activity == 1:
        await bot.change_presence(activity=activity1, status=current_status)
        current_activity = 2
    elif current_activity == 2:
        await bot.change_presence(activity=activity2, status=current_status)
        current_activity = 1

# Command to change bot's status
@bot.tree.command(name="set_status", description="Change the bot's status")
@app_commands.describe(status="Choose a new status for the bot")
@app_commands.choices(status=[
    app_commands.Choice(name="Online", value="online"),
    app_commands.Choice(name="Idle", value="idle"),
    app_commands.Choice(name="Do Not Disturb", value="dnd"),
    app_commands.Choice(name="Invisible", value="invisible"),
])
@commands.check(check_author)
async def set_status(interaction: discord.Interaction, status: app_commands.Choice[str]):
    global current_status
    if status.value == 'online':
        current_status = discord.Status.online
    elif status.value == 'idle':
        current_status = discord.Status.idle
    elif status.value == 'dnd':
        current_status = discord.Status.dnd
    elif status.value == 'invisible':
        current_status = discord.Status.invisible
    await bot.change_presence(status=current_status, activity=activity1 if current_activity == 1 else activity2)
    await interaction.response.send_message(f'Status changed to {status.name}.', ephemeral=True)

# Command to change bot's activity
@bot.tree.command(name="set_activity", description="Change the bot's activity")
@app_commands.describe(
    activity_type="Choose a type of activity",
    activity_text1="Enter the first activity text",
    activity_text2="Enter the second activity text (optional)",
    interval="Enter the switch interval in seconds (optional)"
)
@commands.check(check_author)
async def set_activity(
    interaction: discord.Interaction,
    activity_type: app_commands.Choice[str],
    activity_text1: str,
    activity_text2: str = None,
    interval: int = None
):
    global activity1, activity2, switch_interval

    if activity_type.value == 'playing':
        activity1 = discord.Game(name=activity_text1)
        if activity_text2:
            activity2 = discord.Game(name=activity_text2)
    elif activity_type.value == 'watching':
        activity1 = discord.Activity(type=discord.ActivityType.watching, name=activity_text1)
        if activity_text2:
            activity2 = discord.Activity(type=discord.ActivityType.watching, name=activity_text2)
    elif activity_type.value == 'listening':
        activity1 = discord.Activity(type=discord.ActivityType.listening, name=activity_text1)
        if activity_text2:
            activity2 = discord.Activity(type=discord.ActivityType.listening, name=activity_text2)
    elif activity_type.value == 'streaming':
        activity1 = discord.Streaming(name=activity_text1, url="https://twitch.tv/your_channel")
        if activity_text2:
            activity2 = discord.Streaming(name=activity_text2, url="https://twitch.tv/your_channel")

    if interval:
        switch_interval = interval
        switch_activity.change_interval(seconds=switch_interval)

    message = f'Activity changed to {activity_type.name} with text "{activity_text1}"'
    if activity_text2:
        message += f' and "{activity_text2}"'
    message += f' switching every {switch_interval} seconds.'

    await interaction.response.send_message(message, ephemeral=True)
    switch_activity.restart()

bot.run('YOUR_BOT_TOKEN')
