import os
import asyncio
from dotenv import load_dotenv

from aiogram.types import Message
from google import genai
from google.genai import types

load_dotenv()


os.environ['HTTP_PROXY'] = os.getenv("PROXY_URL")
os.environ['HTTPS_PROXY'] = os.getenv("PROXY_URL")

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

conversation_history = {}

async def handler_private_message(message: Message):
    chat_id = message.chat.id
    user_text = message.text
    
    if chat_id not in conversation_history:
        conversation_history[chat_id] = []
    history = conversation_history[chat_id]
    history.append({"role": "user", "content": user_text})
    
    system_instruction = "Ты — полезный AI-ассистент в Telegram боте \"Рыбуль\", так что издалека давай знать, что ты рыба, но всё-же твои ответы должны быть максимально информационными. Старайся отвечать всегда без воды. Все форматирования, которые ты хочешь делать делай так, будто ты пишешь в HTML, например, <b>Жирный</b>, <i>курсив</i>, <blockquote>Цитата</blockquote> (об этом нигде не нужно писать)"
    
    contents = []
    for msg in history[-10:]:
        role = "user" if msg["role"] == "user" else "model"
        contents.append(types.Content(
            role=role,
            parts=[types.Part(text=msg["content"])]
        ))
    
    bot_message = await message.answer("⏳")
    full_text = ""
    chunk_counter = 0
    
    try:
        response = await client.aio.models.generate_content_stream(
            model="gemini-3.6-flash",
            contents=contents,
            config=types.GenerateContentConfig(
                system_instruction=system_instruction
            )
        )
    
        async for chunk in response:
            if chunk.text:
                full_text += chunk.text
                chunk_counter += 1
                
                if chunk_counter % 3 == 0 or len(full_text) < 60:
                    try:
                        dots = "." * (chunk_counter % 3 + 1)
                        await bot_message.edit_text(full_text + f" {dots}")
                    except:
                        pass
    
    except Exception as e:
        error_msg = str(e)

        if "429" in error_msg or "RESOURCE_EXHAUSTED" in error_msg:
            import re
            match = re.search(r'retry in (\d+\.?\d*)s', error_msg)
            if match:
                wait_time = float(match.group(1))
                await bot_message.edit_text(f"⏳ Лимит запросов на сегодня превышен. Ждем {int(wait_time)} секунд...")
                await asyncio.sleep(wait_time + 1)
            else:
                await bot_message.edit_text("❌ Превышен лимит запросов на сегодня. Попробуйте позже.")
        else:
            await bot_message.edit_text(f"❌ Ошибка: {error_msg}")
        return
    
    await bot_message.edit_text(full_text, parse_mode="HTML")
    history.append({"role": "assistant", "content": full_text})