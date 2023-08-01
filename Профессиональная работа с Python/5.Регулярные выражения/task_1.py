import re
import csv

with open("phonebook_raw.csv", 'r', encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    new_contacts_list = []


def format_contacts_name():
    name_pattern = r'([А-Я])'
    changed_name = r' \1'
    for column in contacts_list[1:]:
        line = column[0] + column[1] + column[2]
        if len((re.sub(name_pattern, changed_name, line).split())) == 3:
            column[0] = re.sub(name_pattern, changed_name, line).split()[0]
            column[1] = re.sub(name_pattern, changed_name, line).split()[1]
            column[2] = re.sub(name_pattern, changed_name, line).split()[2]
        elif len((re.sub(name_pattern, changed_name, line).split())) == 2:
            column[0] = re.sub(name_pattern, changed_name, line).split()[0]
            column[1] = re.sub(name_pattern, changed_name, line).split()[1]
            column[2] = ''
        elif len((re.sub(name_pattern, changed_name, line).split())) == 1:
            column[0] = re.sub(name_pattern, changed_name, line).split()[0]
            column[1] = ''
            column[2] = ''
    return


def format_contacts_phone_number():
    phone_pattern = re.compile(
        r'(\+7|8)?\s*\(?(\d{3})\)?\s*\D?(\d{3})[-\s+]?(\d{2})-?(\d{2})((\s)?\(?(доб.)?\s?(\d+)\)?)?')
    changed_phone = r'+7(\2)\3-\4-\5\7\8\9'
    for column in contacts_list:
        column[5] = phone_pattern.sub(changed_phone, column[5])
    return


def merging_duplicates():
    for column in contacts_list[1:]:
        for contact in contacts_list:
            if column[0] == contact[0] and column[1] == contact[1]:
                if column[2] == '':
                    column[2] = contact[2]
                if column[3] == '':
                    column[3] = contact[3]
                if column[4] == '':
                    column[4] = contact[4]
                if column[5] == '':
                    column[5] = contact[5]
                if column[6] == '':
                    column[6] = contact[6]
    for contact in contacts_list:
        if contact not in new_contacts_list and len(contact) == 7:
            new_contacts_list.append(contact)
    return


if __name__ == '__main__':
    format_contacts_name()
    format_contacts_phone_number()
    merging_duplicates()

    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(new_contacts_list)
