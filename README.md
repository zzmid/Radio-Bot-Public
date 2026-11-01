# Dayz-Radio-Bot
A public radio bot for dayz

Anything posted in your radio channel gets deleted and reposted by the bot as an anonymous radio message. The real sender gets logged in a staff channel so you can still see who sent what. Radio messages delete themselves after 2 hours by default (if the bot restarts before then, those ones stay up).

## Setup

1. Make a bot at https://discord.com/developers/applications
2. In the Bot tab turn on Message Content Intent, then hit Reset Token and copy it. That's your `TOKEN`
3. In OAuth2 > URL Generator tick the `bot` scope and these permissions: View Channels, Send Messages, Embed Links and Manage Messages. Open the link it gives you and pick your server
4. Make sure the bot can see and post in both the radio channel and the log channel, and can delete messages in the radio channel
5. Install requirements with `pip install -r requirements.txt`
6. Set the environment variables below and run `python radio.py`

## Environment variables

- `TOKEN` - your bot token
- `RADIO_CHANNEL_ID` - the channel people send radio messages in
- `LOG_CHANNEL_ID` - staff channel where the real sender gets logged (optional, leave it out to turn logging off)
- `DELETE_AFTER_SECONDS` - how long radio messages stay up in seconds, default is 7200 (2 hours). Don't set it to 0, that deletes them right away

To get a channel ID turn on Developer Mode in Discord settings (Advanced), then right click the channel and hit Copy Channel ID.
