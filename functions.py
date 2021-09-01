from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest


async def join_to_many_chats(client: object, chats_names: list) -> None:
    for chat in chats_names:
        await join_to_chat(client, chat)


async def leave_many_chats(client: object, chats_names: list) -> None:
    for chat in chats_names:
        await leave_chat(client, chat)


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
