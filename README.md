# Discord Bot

This is a Discord bot built using `discord.py` that can change its status and activity based on user commands.

## Features

- Change bot status to Online, Idle, Do Not Disturb, or Invisible.
- Change bot activity to Playing, Watching, Listening, or Streaming.
- Switch between two activities at a set interval.


## Configure

config.json:
`{
    "token": "YOUR_DISCORD_BOT_TOKEN_HERE",
    "owner_id": "YOUR_DISCORD_OWNER_ID_HERE"
}`

## Commands

### Set Status

Use the `/set_status` command to change the bot's status.

**Command Usage:**
/set_status status:<Online|Idle|Do Not Disturb|Invisible>

### set_activity

Use the `/set_activity` command to change the bot's activity

Change the bot's activity. The bot can switch between two activities at a specified interval.

**Options:**
- `activity_type`: Choose the type of activity (Playing, Watching, Listening, Streaming).
- `activity_text1`: Enter the text for the first activity.
- `activity_text2` (optional): Enter the text for the second activity.
- `interval` (optional): Set the interval in seconds for switching between activities.

Example usage:

/set_activity activity_type
activity_text1:"Hello" activity_text2:"I am Groot" interval:5

[Support Server](https://discord.gg/HAyAe387Tk)
