# zingBot

A roasting telegram bot

## Features

- 🤖 Smart conversations using Deepseek API
- 🎭 Unique roasting style with witty comebacks
- 🌐 Proxy support for global access
- 🔒 Secure environment configuration

## Installation

1. Clone the repository:
   ```bash
    git clone https://github.com/AirTouch666/zingBot.git
    cd zingBot
    ```
2. Create and activate virtual environment:
    ```bash
    python -m venv .venv
    (↓ Linux & macOS ↓)
    source .venv/bin/activate
    (↓ Windows ↓)
    .venv\Scripts\activate
    ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Open .env and configure environment variables:
   ```
     TELEGRAM_TOKEN=your_telegram_bot_token
     DEEPSEEK_API_KEY=your_deepseek_api_key
     USE_PROXY=true or false
     PROXY_URL=your_proxy_url
    ```
## Getting API Keys

1. Telegram Bot Token:
   - Contact [@BotFather](https://t.me/BotFather) on Telegram
   - Send `/newbot` command
   - Follow instructions to create your bot
   - Save the API token

2. Deepseek API Key:
   - Visit [Deepseek's website](https://platform.deepseek.com)
   - Create an account
   - Generate an API key

## Running the Bot

```bash
python zing_bot.py
```

## Usage

1. Search for your bot on Telegram
2. Send `/start` to begin
3. Send any message and wait for the bot's witty roast

## Proxy Configuration

To use a proxy:
1. Set `USE_PROXY=true` in `.env`
2. Configure `PROXY_URL` with your proxy server address

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

## Contact

If you have any questions or suggestions, feel free to:
- Open an [Issue](https://github.com/AirTouch666/zingBot/issues)

## Thanks

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- [Deepseek](https://deepseek.com)