import os
import json
from typing import Union


class JsonFile(object):

    def __init__(self, json_file_name: str):
        """:param json_file_name: Имя файла"""
        self.json_file_name = json_file_name
        self.directory = os.path.join(os.getcwd(), 'db', self.json_file_name)

    def create_json_file(self, new_data: any = None) -> None:
        """
        Создать json файл.
        :param new_data: Новые данные
        """
        if new_data is None:
            new_data = []
        with open(self.directory, 'w', encoding='utf-8') as json_file:
            json.dump(new_data, json_file, ensure_ascii=False)

    def search_json_file_and_create(self) -> None:
        """Проверить, существует ли json файл. Если файла отсутствует - создает новый файл"""
        if not os.path.exists(self.directory):
            self.create_json_file()

    def get_all_data(self) -> any:
        """
        Получить все данные из json файла.
        :return: Данные из json файла
        """
        self.search_json_file_and_create()
        with open(self.directory, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            return data

    def get_data_by_category(self, category: str) -> any:
        """
        Получить данные из json файла по категории.
        :param category: Категория чата
        :return: Данные из json файла отфильтрованные по категории чата
        """
        data = self.get_all_data()
        return data[category]

    def insert_new_data(self, category: str, new_data: str) -> None:
        """
        Перезаписать json файл с новыми данными.
        :param category: Категория чата
        :param new_data: Новые данные
        """
        data = self.get_all_data()
        data[category].append(new_data)
        self.create_json_file(data)

    def delete_data(self, category: str, deleted_data: str) -> None:
        """
        Перезаписать json файл с новыми данными.
        :param category: Категория чата
        :param deleted_data: Данные для удаления
        """
        data = self.get_all_data()
        data[category].remove(deleted_data)
        self.create_json_file(data)

    def check_data(self, category: str, required_data: str) -> Union[bool, None]:
        """
        Проверка наличия искомых данных в json файле.
        :param category: Категория чата
        :param required_data: искомое значение
        :return: True или None
        """
        data = self.get_all_data()
        if required_data in data[category]:
            return True

    def move_between_categories(self, chat_name: str, category_A: str, category_B: str) -> None:
        """
        Нас забанили, перемещаемся между категориями
        :param chat_name: Название чата
        :param category_A: Название категории, из которой чат будет удален
        :param category_B: Название категории, в которую чат будет добавлен
        """
        self.delete_data(category_A, chat_name)
        self.insert_new_data(category_B, chat_name)

    def return_chats_in_active_category(self) -> None:
        """
        Вернуть чаты из режима ожидания в активную категорию
        """
        chats = self.get_data_by_category("waiting")
        for chat in chats:
            self.move_between_categories(chat, "waiting", "enter and exit")


ChatNames = JsonFile("chats_names.json")
