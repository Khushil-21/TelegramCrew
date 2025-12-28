# Telegram Bot Message Watcher

A Python-based Telegram bot that watches for incoming messages and handles text, voice, and audio messages using only HTTP requests (no external libraries except standard library).

## Features

- 🔍 **Watch Messages**: Long polling to receive real-time messages
- 💬 **Text Messages**: Receive and send text messages
- 🎤 **Voice Messages**: Receive voice messages and send voice notes
- 🎵 **Audio Messages**: Handle audio file messages
- 📥 **File Download**: Download voice and audio files from Telegram servers
- 🚀 **Pure HTTP**: Uses only Python's standard library (`urllib`)

## Setup

1. **Get Your Bot Token**
   - Talk to [@BotFather](https://t.me/botfather) on Telegram
   - Create a new bot with `/newbot`
   - Copy the bot token

2. **Configure the Bot**
   - Open `main.py`
   - Replace `YOUR_BOT_TOKEN_HERE` with your actual bot token:
     ```python
     BOT_TOKEN = "1234567890:ABCdefGHIjklMNOpqrsTUVwxyz"
     ```

3. **Run the Bot**
   ```bash
   python main.py
   ```

## Usage

### Watch Messages

The bot automatically starts watching for messages when you run `main.py`. It will:
- Print incoming text messages
- Download and save voice messages as `voice_<message_id>.ogg`
- Download and save audio messages as `audio_<message_id>.mp3`

### Send Text Message

```python
send_text_message(
    chat_id=123456789,
    text="Hello from Python!",
    reply_to_message_id=None  # Optional: reply to a specific message
)
```

### Send Voice Message

```python
send_voice_message(
    chat_id=123456789,
    voice_file_path="path/to/voice.ogg",
    caption="Check out this voice message!",  # Optional
    reply_to_message_id=None  # Optional
)
```

## Functions Overview

### Core Functions

- **`make_request(method, params, files)`** - Makes HTTP requests to Telegram Bot API
- **`get_updates(offset, timeout)`** - Gets updates using long polling
- **`send_text_message(chat_id, text, reply_to_message_id)`** - Sends text messages
- **`send_voice_message(chat_id, voice_file_path, caption, reply_to_message_id)`** - Sends voice messages
- **`download_file(file_id, save_path)`** - Downloads files from Telegram

### Message Handlers

- **`handle_text_message(message)`** - Processes incoming text messages
- **`handle_voice_message(message)`** - Processes incoming voice messages
- **`handle_audio_message(message)`** - Processes incoming audio messages
- **`process_message(message)`** - Routes messages to appropriate handlers

### Main Functions

- **`watch_messages()`** - Main loop for watching messages
- **`main()`** - Entry point

## Message Format

The bot prints received messages in this format:

```
[TEXT] From: John (@john_doe)
Chat ID: 123456789
Message: Hello, bot!

[VOICE] From: Jane (@jane_doe)
Chat ID: 987654321
Duration: 5s, Size: 12345 bytes
File ID: AwACAgIAAxkBAAI...

[AUDIO] From: Bob (@bob_smith)
Chat ID: 555555555
Title: Song Name, Artist: Artist Name
Duration: 180s, Size: 3456789 bytes
File ID: CQACAgIAAxkDAAI...
```

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)

## Notes

- Voice messages are saved in OGG format
- Audio messages are saved in MP3 format (or original format)
- The bot uses long polling with 30-second timeout for efficient message retrieval
- All HTTP requests are made using `urllib` from Python's standard library
- Error handling is included for network issues and API errors

## Customization

You can customize the message handlers in `main.py`:

- Modify `handle_text_message()` to respond to specific commands
- Change `handle_voice_message()` to process voice files differently
- Update `handle_audio_message()` to handle audio files as needed

## Stopping the Bot

Press `Ctrl+C` to gracefully stop the message watcher.

