import csv
import re
from phoneboock_fix import phonebook_fix


if __name__ == '__main__':
    raw_data = "phonebook_raw.csv"
    fix_data = "phonebook.csv"
    phonebook_fix(raw_data, fix_data)


