boys = ['Петр', 'Алексей', 'Роман', 'Даниил', 'Степан']
girls = ['Светлана', 'Анастасия', 'Алёна', 'Ирина', 'Татьяна']

boys.sort()
girls.sort()

couples_values = zip(boys, girls)
couples_list = list(couples_values)

if len(boys) == len(girls):
    print("Идеальные пары:")
for couple in couples_list:
    print(couple[0] + " и " + couple[1])
else:
    print("Нечетное количество человек, кто-то останется без пары((")
