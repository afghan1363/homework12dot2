def get_val(collection, key, default='git'):
    """
    Функция возвращает значение из словаря по переданному ключу,
    если ключ существует. В ином случае возвращается значение
    default
    :param collection: словарь
    :param key: ключ словаря
    :param default: по умолчанию 'git'
    :return: collection[key]
    """
    if key in collection.keys():
        return collection[key]
    return default
