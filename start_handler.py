from telegram import Update
from telegram.ext import CommandHandler, CallbackContext


async def welcome(update: Update, context: CallbackContext) -> None:
    new_member = update.message.new_chat_members[0]
    welcome_message = f"Welcome {new_member.full_name} to the group!"
    await update.message.reply_text(welcome_message)


async def get_bot_photo(update: Update, context: CallbackContext) -> None:
    bot_user = await context.bot.get_me()
    photos = await context.bot.get_user_profile_photos(bot_user.id)
    if photos.photos:
        await context.bot.send_photo(update.effective_chat.id,
                                     photo=photos.photos[0][0].file_id)
    else:
        await update.message.reply_text(
            "The bot does not have any profile picture.")


async def request_photo(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Send me a picture to set for the profile.'
                                    )

    context.user_data['setting_group_photo'] = True


async def echo(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text

    if 'token' in user_message.lower():
        await update.message.reply_text(TOKEN, quote=True)
    elif 'hi' in user_message.lower():
        await update.message.reply_text('Hi! How can I help you today?',
                                        quote=True)
    else:
        await update.message.reply_text("Invalid Command, try again.")


async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("""Hello! Welcome to the group manager bot!
Here are some functionalities you can use:
        /1 • Generating an invite link.
        /2 • Fetching bot photo.
        /3 • Setting a picture for the group's profile.
        /4 • Contact admin.
""")
