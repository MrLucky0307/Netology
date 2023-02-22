# task_1
geo_logs = [
    {'visit1': ['Москва', 'Россия']},
    {'visit2': ['Дели', 'Индия']},
    {'visit3': ['Владимир', 'Россия']},
    {'visit4': ['Лиссабон', 'Португалия']},
    {'visit5': ['Париж', 'Франция']},
    {'visit6': ['Лиссабон', 'Португалия']},
    {'visit7': ['Тула', 'Россия']},
    {'visit8': ['Тула', 'Россия']},
    {'visit9': ['Курск', 'Россия']},
    {'visit10': ['Архангельск', 'Россия']}
]


def sort_list():
    sorted_geo_logs = []
    for visit in geo_logs:
        for place in visit:
            city_country = visit[place]
            if city_country[1] == "Россия":
                sorted_geo_logs.append(visit)
    return sorted_geo_logs


# task_2
ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}


def get_unique_id():
    geo_id = []
    for values in ids:
        geo_id += (ids[values])
    unique_geo_id = list(set(geo_id))
    return unique_geo_id


# task_3
queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
]


def word_percentage():
    storage = {}
    for query in queries:
        words = query.split()
        if len(words) in storage.keys():
            storage[len(words)] += 1
        else:
            storage.update({len(words): 1})
    for key, value in storage.items():
        percentage = round((value / len(queries)) * 100, 2)
        res = f'Поисковых запросов состоящих из {key} слов(а): {percentage}% ({value} запроса)'
        print(res)


# task_4
stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}


def max_stats_chanel():
    sorted_stats = sorted(stats.values())
    sorted_stats_dict = {}
    for name in sorted_stats:
        for value in stats.keys():
            if stats[value] == name:
                sorted_stats_dict[value] = stats[value]
                break
    res = list(sorted_stats_dict.keys())[-1]
    return res


if __name__ == "__main__":
    print(sort_list())
    print(get_unique_id())
    word_percentage()
    print(max_stats_chanel())
