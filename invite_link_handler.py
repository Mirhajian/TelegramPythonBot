import os
from telegram import Update, InputFile, ChatInviteLink
from telegram.ext import CommandHandler, CallbackContext


async def create_invite_link(update: Update, context: CallbackContext) -> None:
    if not update.message.chat.type in ['group', 'supergroup']:
        await update.message.reply_text(
            'This function only works in group chats.')
        return

    try:
        invite_link: ChatInviteLink = await context.bot.create_chat_invite_link(
            chat_id=update.message.chat_id, expire_date=None, member_limit=1)
        await update.message.reply_text(
            f'Invite Link: {invite_link.invite_link}')
    except Exception as e:
        await update.message.reply_text(
            f'Unable to create a link. Check permissions for the bot. {e}')
