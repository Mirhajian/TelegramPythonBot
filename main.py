from telegram.ext import Updater, CommandHandler, MessageHandler, filters, ConversationHandler, CallbackContext, ChatMemberHandler
from telegram import InputFile
import os

from start_handler import start, get_bot_photo, request_photo, echo, welcome
from invite_link_handler import create_invite_link
from photo_handler import set_group_profile_photo
from admin_handler import contact_admin, forward_to_admin

TOKEN = 'YOUR_TOKEN'
CHAT_WITH_ADMIN = range(1)


async def send_startup_message(context: CallbackContext) -> None:
    try:
        await context.bot.send_message(chat_id='your_chat_id',
                                       text="Bot is starting up!")
    except Exception as e:
        print(f"Error sending startup message: {e}")


def main():
    updater = Updater(token=TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("1", create_invite_link))
    dispatcher.add_handler(CommandHandler("2", get_bot_photo))
    dispatcher.add_handler(CommandHandler("3", request_photo))

    dispatcher.add_handler(
        MessageHandler(filters.PHOTO & filters.ChatType.GROUPS,
                       set_group_profile_photo))

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("4", contact_admin)],
        states={
            CHAT_WITH_ADMIN: [
                MessageHandler(filters.TEXT & ~filters.COMMAND,
                               forward_to_admin)
            ],
        },
        fallbacks=[CommandHandler("start", start)],
    )
    dispatcher.add_handler(conv_handler)

    dispatcher.add_handler(
        MessageHandler(
            filters.TEXT & filters.ChatType.PRIVATE & ~filters.COMMAND,
            forward_to_admin))
    dispatcher.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    dispatcher.add_handler(
        ChatMemberHandler(welcome, ChatMemberHandler.MY_CHAT_MEMBER))

    job_queue = updater.job_queue
    job_queue.run_once(send_startup_message, when=0)

    updater.start_polling(
        poll_interval=10)  # Adjust polling interval as needed
    updater.idle()


if __name__ == '__main__':
    main()
