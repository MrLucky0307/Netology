stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

sorted_stats = sorted(stats.values())
sorted_stats_dict = {}

for name in sorted_stats:
    for value in stats.keys():
        if stats[value] == name:
            sorted_stats_dict[value] = stats[value]
            break

print(list(sorted_stats_dict.keys())[-1])
