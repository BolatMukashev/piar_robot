from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest
from telethon.errors.rpcerrorlist import ChannelPrivateError, FloodWaitError
from json_classes import ChatNames
import time


async def join_to_many_chats(client: object) -> None:
    chats = ChatNames.get_data_by_category("enter and exit")
    for chat in chats:
        try:
            await join_to_chat(client, chat)
        except ChannelPrivateError:
            ChatNames.move_between_categories(chat, "enter and exit", "banned")


async def leave_many_chats(client: object) -> None:
    ChatNames.return_chats_in_active_category()
    chats = ChatNames.get_data_by_category("enter and exit")
    for chat in chats:
        await leave_chat(client, chat)


async def send_messages_to_many_chats(client: object, text: str = '👍🏻') -> None:
    t = 30
    chats = ChatNames.get_data_by_category("enter and exit")
    for chat in chats:
        try:
            await send_message(client, chat, text)
            ChatNames.move_between_categories(chat, "enter and exit", "waiting")
            time.sleep(t)
            t += 5
        except FloodWaitError as e:
            print(f"Бан за флуд\n{e}")
            break


async def join_to_chat(client: object, chat_name: str) -> None:
    """
    Присоедениться к чату
    :param client: аккаунт
    :param chat_name: название чата
    """
    await client(JoinChannelRequest(chat_name))


async def leave_chat(client: object, chat_name: str) -> None:
    """
    Покинуть чат
    :param client: аккаунт
    :param chat_name: название чата
    """
    await client(LeaveChannelRequest(chat_name))


async def send_message(client: object, name: str, text: str) -> None:
    """
    Отправить сообщение в чат или пользователю
    :param client: аккаунт
    :param name: название чата или имя пользователя
    :param text: тект сообщения
    """
    await client.send_message(name, text)
