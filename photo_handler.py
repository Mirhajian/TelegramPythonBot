import os
from telegram import Update, InputFile
from telegram.ext import MessageHandler, filters, CallbackContext


async def set_group_profile_photo(update: Update,
                                  context: CallbackContext) -> None:
    if not context.user_data.get('setting_group_photo', False):
        return

    chat_id = update.effective_chat.id
    photo = update.message.photo[-1]
    file = await context.bot.get_file(photo.file_id)
    file_path = os.path.join('data', f'{chat_id}.jpg')
    os.makedirs('data', exist_ok=True)
    await file.download(file_path)

    with open(file_path, 'rb') as f:
        await context.bot.set_chat_photo(chat_id, InputFile(f))
    os.remove(file_path)
    await update.message.reply_text("Group profile photo updated successfully!"
                                    )

    context.user_data.pop('setting_group_photo')
