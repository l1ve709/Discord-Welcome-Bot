# Discord Voice Bot Project

This project provides the following: 3 different Discord bots connect to 3 different voice channels, and when a member joins these voice channels, a music-playing function is triggered. Optionally, you can add the ID of a recording role to the `ytRole` variable. When a user with this role joins the voice channel, the playing music automatically stops.

(**THIS WELCOME BOT IS IN BETA VERSION, VOICE DETECTION FEATURE IS CURRENTLY UNAVAILABLE**)

## Language(s) Used

<picture>
  <source srcset="https://skillicons.dev/icons?i=py" media="(prefers-color-scheme: dark)">
  <img src="https://skillicons.dev/icons?i=py">
</picture>

## Features

- **Multiple Bots:** Connects three bots to different voice channels simultaneously.
- **Automatic Music Playback:** Plays a specified audio file in the voice channel.
- **Role-Based Music Control:** Stops music playback when a user with a specific role joins the voice channel.
- **Automatic Connection:** The bots automatically connect to the specified voice channels and begin playing music as users join.

## Requirements

- `discord.py` library (V2.0)
- Python 3.8+
- A Discord application with three different bot tokens
- An audio file (e.g., `merhabaoyuncu.mp3`)

## Setup

1. **Install the libraries:**

    ```bash
    pip install discord.py
    ```

2. **Set Bot Tokens:**

   Add your bot tokens to the `bot_tokens` list in the `main()` function.

3. **Set Voice Channel IDs:**

   Find the IDs of the voice channels the bots will connect to, and add them to the `voice_channel_ids` list.

4. **Set the Audio File:**

   Use the `audioPath` variable to specify the full file path of the audio file you want to play. For example: `/home/container/merhabaoyuncu.mp3`

5. **Set the Role ID:**

   Enter the ID of the role that will stop the music in the `ytRole` variable.

## Usage

1. Run the project with the following terminal command:

    ```bash
    python bot.py
    ```

2. The bots will activate and connect to the specified voice channels.

3. When a user with the specified role joins the voice channel, the bot will stop playing music.

4. **Manual Connection:** If a bot disconnects from the voice channel, you can reconnect it using the `.join` command (only for the channel you are currently in).

## Commands

- `.join`: Reconnects the bot to the voice channel (ONLY JOINS THE CHANNEL YOU ARE CURRENTLY IN).

## Troubleshooting

- If the bot does not connect or cannot play the audio file, check the error messages in the terminal. Adjust the file path or permissions as needed.

## License

Protected by the MIT License.

## My Discord Account

![My Discord](https://lantern.rest/api/v1/users/794909914760871967?svg=1&theme=dark&borderRadius=2&hideActivity=1&hideStatus=0)
