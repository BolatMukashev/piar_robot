from telethon import TelegramClient
from functions import *
from config import API_ID, API_HASH, USER_NAME
from json_classes import ChatNames

client = TelegramClient(USER_NAME, API_ID, API_HASH)
test_chat_name = "@golangl"


async def main():
    # info
    me = await client.get_me()
    all_info = me.stringify()
    # await client.send_message('me', all_info)

    # username = me.username
    # phone = me.phone
    # print(username)
    # print(phone)
    # await client.send_message('me', username)
    # await client.send_message('me', phone)

    # You can print all the dialogs/conversations that you are part of:
    # async for dialog in client.iter_dialogs():
    #     print(dialog.name, 'has ID', dialog.id)

    # сообщение в чат или пользователю
    # await client.send_message('@bizAdamdar777', '😳')

    # message = await client.send_message(
    #     'me',
    #     'Тут стили от маркдоун **жирный**, `код`, __курсив__ и [url сайта](https://google.com)!',
    #     link_preview=False
    # )

    # Отправка сообщения возвращает объект этого сообщения?
    # print(message.raw_text)

    # Если есть объект сообщения, на него можно отвечать напрямую?
    # await message.reply('Cool!')

    # отправка файлов
    # await client.send_file('me', 'promo_photo.jpg')

    # Проитерироваться по истории чата:
    # async for message in client.iter_messages('me'):
    #     print(message.id, message.text)
    #
    #     # Скачать файлы из сообщения
    #     # Возвращает путь, куда фото было скачано
    #     if message.photo:
    #         path = await message.download_media()
    #         print('File saved to', path)  # printed after download is done

    chats = ChatNames.get_data_by_category("enter and exit")
    await join_to_many_chats(client, chats)

    # await leave_chat(client, test_chat_name)


if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(main())
