from src.admin.admin_panel import *
from config import dp


# @dp.message_handler(commands='toshiqoy')
# async def helper(message: types.Message):
#     await message.reply('hoz')
#     import shutil
#     shutil.make_archive("../for_mandat", 'zip', "../for_mandat")
#     await message.reply_document(document=open("../for_mandat.zip", 'rb'))


@dp.message_handler(content_types="any")
async def helper(message: types.Message):
    id = message.message_id
    await dp.bot.copy_message(chat_id=message.from_user.id, from_chat_id=message.from_user.id, message_id=id)


if __name__ == "__main__":
    executor.start_polling(dp)
