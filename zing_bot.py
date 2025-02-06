import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
import httpx
from typing import Optional
import urllib3

urllib3.disable_warnings()

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
DEEPSEEK_API_KEY = os.getenv('DEEPSEEK_API_KEY')
USE_PROXY = os.getenv('USE_PROXY', 'false').lower() == 'true'
PROXY_URL = os.getenv('PROXY_URL')

TIMEOUT = 60.0

def get_proxy_settings() -> Optional[dict]:
    if USE_PROXY:
        return {
            'http://': PROXY_URL,
            'https://': PROXY_URL
        }
    return None

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "我是 zingBot，专门怼人的机器人。\n"
        "来啊，互相伤害啊！说点什么，让我教教你做人！"
    )

async def get_deepseek_response(message: str) -> str:
    transport = httpx.AsyncHTTPTransport(
        verify=False,
        proxy=PROXY_URL if USE_PROXY else None
    )
    
    async with httpx.AsyncClient(
        transport=transport,
        timeout=httpx.Timeout(TIMEOUT)
    ) as client:
        response = await client.post(
            "https://api.deepseek.com/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "deepseek-chat",
                "messages": [
                    {
                        "role": "system",
                        "content": "你是一个毒舌机器人，喜欢用幽默但尖锐的方式怼人。记住要有趣但不能太过分或带有侮辱性。"
                    },
                    {
                        "role": "user",
                        "content": message
                    }
                ],
                "temperature": 0.7
            }
        )
        result = response.json()
        return result['choices'][0]['message']['content']

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    try:
        response = await get_deepseek_response(user_message)
        await update.message.reply_text(response)
    except Exception as e:
        await update.message.reply_text("哎呀，我正在酝酿更毒的话，请稍后再试～")
        print(f"Error: {str(e)}")

def main():
    proxy_url = PROXY_URL if USE_PROXY else None
    
    application = (
        Application.builder()
        .token(TELEGRAM_TOKEN)
        .proxy_url(proxy_url)  
        .get_updates_proxy_url(proxy_url)  
        .build()
    )

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot is running...")
    print(f"Proxy enabled: {USE_PROXY}")
    print(f"Proxy URL: {PROXY_URL if USE_PROXY else 'None'}")
    
    application.run_polling(
        allowed_updates=Update.ALL_TYPES,
        drop_pending_updates=True,
        timeout=TIMEOUT,
        read_timeout=TIMEOUT,
        write_timeout=TIMEOUT,
        connect_timeout=TIMEOUT,
        pool_timeout=TIMEOUT
    )

if __name__ == '__main__':
    main() 