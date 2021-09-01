from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest


async def join_to_chat(client: object, chat_name: str) -> None:
    """
    Присоедениться к чату
    :param client: аккаунт
    :param chat_name: название чата
    """
    client(JoinChannelRequest(chat_name))


async def leave_chat(client: object, chat_name: str) -> None:
    """
    Покинуть чат
    :param client: аккаунт
    :param chat_name: название чата
    """
    await client(LeaveChannelRequest(chat_name))
