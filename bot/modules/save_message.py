from telegram.ext import CallbackQueryHandler

from bot import dispatcher


def save_message(update, context):
    query = update.callback_query
    if query.data == "save":
        try:
            del query.message.reply_markup['inline_keyboard'][-1]
            query.message.copy(query.from_user.id, reply_markup=query.message.reply_markup)
            query.answer('Message Saved Successfully', show_alert=True)
        except:
            query.answer('Start the bot in private and try again', show_alert=True)


msgsave_handler = CallbackQueryHandler(save_message, pattern="save", run_async=True)

dispatcher.add_handler(msgsave_handler)
