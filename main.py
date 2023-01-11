import openai
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

openai.api_key = "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"

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Salut ! Je suis un bot OpenAI, comment puis-je t'aider aujourd'hui ?")

def message(update, context):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt='> ' + update.message.text,
        max_tokens=2048,
        n =1,
        stop=None,
        temperature=0.5
    )
    context.bot.send_message(chat_id=update.effective_chat.id, text=response.choices[0].text)

app = ApplicationBuilder().token("5863362545:AAHzI5paf8aus3WVOO9a8KJGR80h3m8ONfQ").build()


app.run_polling()
