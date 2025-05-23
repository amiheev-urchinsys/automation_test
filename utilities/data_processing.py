import json


class DataProcessing:

    def get_list_from_file(self, file_name, list_title):
        """
        Returns the list with data from the given file

        :param file_name: Give file name with its extension
        :param list_title: Give key name that has list value
        :return: List with data
        """
        with open("../data/" + file_name + "") as f:
            file_data = json.load(f)
            required_list = file_data[list_title]
        return required_list

    def get_value_by_key(self, data, target_key):
        """
        Recursively searches for a key in a nested dictionary/list and returns its value.

        :param data: The JSON data (dictionary or list).
        :param target_key: The key whose value is being searched for.
        :return: The value of the target_key if found, otherwise None.
        """
        # Если data - это список, рекурсивно проверяем каждый элемент
        if isinstance(data, list):
            for item in data:
                result = self.get_value_by_key(item, target_key)
                if result:
                    return result

        # Если data - это словарь, проверяем наличие ключа
        elif isinstance(data, dict):
            for key, value in data.items():
                if key == target_key:
                    return value
                # Если ключ не найден, но значение является словарем или списком, продолжаем искать
                elif isinstance(value, (dict, list)):
                    result = self.get_value_by_key(value, target_key)
                    if result:
                        return result

        return None  # Возвращаем None, если ключ не найден
