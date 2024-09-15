import os
import telebot
from dotenv import load_dotenv
load_dotenv(".env")

import telegramify_markdown
from telegramify_markdown import customize
customize.markdown_symbol.head_level_1 = "📌" 
customize.markdown_symbol.link = "🔗"  
customize.strict_markdown = True 

BOT_TOKEN = os.environ["BOT_TOKEN"]
bot = telebot.TeleBot(BOT_TOKEN)

group_chat_id = ""

def send(text):
    converted = telegramify_markdown.markdownify(
    text,
    max_line_length=None,  
            normalize_whitespace=False
)
    print(converted)
    bot.send_message(group_chat_id,converted, parse_mode="MarkdownV2")
