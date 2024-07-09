from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, ConversationHandler, CallbackContext

ADMIN_ID = '298965457'
CHAT_WITH_ADMIN = range(1)


async def contact_admin(update: Update, context: CallbackContext) -> None:
    if context.user_data.get('contacting_admin', False):
        await update.message.reply_text(
            "You are already in contact with the admin.")
        return

    await update.message.reply_text(
        "Please send your message. Type 'cancel' to stop chatting with the admin."
    )
    context.user_data['contacting_admin'] = True


async def forward_to_admin(update: Update, context: CallbackContext):
    if update.message.text.lower() == 'cancel':
        await update.message.reply_text(
            "You have exited the chat with the admin.")
        return ConversationHandler.END

    message = update.message
    await context.bot.forward_message(chat_id=ADMIN_ID,
                                      from_chat_id=message.chat_id,
                                      message_id=message.message_id)
    await update.message.reply_text("Your message has been sent to the admin.")
