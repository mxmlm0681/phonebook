import re
import csv


def phonebook_fix(raw_data, fix_data):
    with open(raw_data, "r", encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contact_list = list(rows)

        name_pattern = r"^([\w]+)(\s)?([\w]+)?(\s)?([\w]+)?,([\w]+)?(\s)?([\w]+)?,([\w]+)?"
        name_reg = re.compile(name_pattern)

        phones_pattern = r"((\+7)|8)\s?\(?([\d]{3}?)(\)|\s|-)?\s?([\d]{3}?)(\s|-)?([\d]{2}?)(\s|-)?([\d]{2}?)(\s\(?(доб\.)?\s?([\d]*)\)?)?"
        phone_reg = re.compile(phones_pattern)

        contact_list_fix = []
        for contact in contact_list:
            contact = ','.join(contact)

            contact = name_reg.sub(r"\1,\3\6,\5\8\9", contact)
            contact = phone_reg.sub(r"+7(\3)\5-\7-\9 \11\12", contact)
            contact = contact.split(',')
            contact_list_fix.append(contact)

        contacts = []
        for contact in contact_list_fix:
            entry = (contact[0], contact[1])
            contacts.append(entry)
        contacts = set(contacts)

        phonebook_fixed = []
        for entry in contacts:
            new_entry = ['', '', '', '', '', '', '']
            for contact in contact_list_fix:
                if entry[0] and entry[1] in contact:
                    i = -1
                    for field in contact:
                        i += 1
                        if new_entry[i] != contact[i]:
                            new_entry[i] += contact[i]

            phonebook_fixed.append(new_entry)
        phonebook_fixed.sort()

        with open(fix_data, "w", encoding='utf-8') as f:
            datawriter = csv.writer(f, delimiter=',')
            datawriter.writerows(phonebook_fixed)
        return print(f'исходный файл {raw_data} исправлен и записан {fix_data}')
