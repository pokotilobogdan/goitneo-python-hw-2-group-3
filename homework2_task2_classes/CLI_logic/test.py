from main import *
#
# # Створення нової адресної книги
#
# book = AddressBook()
#
# # Створення запису для John
#
# john_record = Record("John")
# print("Created record for John.")
# print(john_record, '\n')
#
# john_record.add_phone("1234567890")
# print("Added first phone to John.")
# print(john_record, '\n')
#
# john_record.add_phone("1234567890")
# print(john_record, '\n')
#
# john_record.add_phone("123490")
# print(john_record, '\n')
#
# john_record.add_phone("5555555555")
# print("Added second phone to John.")
# print(john_record, '\n')
#
# john_record.add_phone("6666666666")
# print("Added third phone to John.")
# print(john_record, '\n')
#
# print("Looking for number 1234567890:")
# john_record.find_phone("1234567890")
# print("Found a phone of John.")
# print()
#
# print("Trying to remove number 12345:")
# john_record.remove_phone("12345")
# print()
#
# print("Trying to remove number 6666666666:")
# john_record.remove_phone("6666666666")
# print()
#
# print("Trying to find number 112890 in John record:")
# john_record.find_phone("112890")
# print()
#
# print("Editing from 1234567890 to 1111111111")
# john_record.edit_phone("1234567890", "1111111111")
# print(john_record, '\n')
#
# print("Editing from 1111111111 to 5555555555")
# john_record.edit_phone("1111111111", "5555555555")
# print(john_record, '\n')
#
#     # Додавання запису John до адресної книги
#
# book.add_record(john_record)
#
#     # Створення та додавання нового запису для Jane
#
# jane_record = Record("Jane")
# print("Created record for Jane.")
# print(jane_record, '\n')
#
# jane_record.add_phone("9876543210")
# print("Added first phone to Jane.")
# print(jane_record, '\n')
#
# book.add_record(jane_record)
#
# # Виведення всіх записів у книзі
#
# print("List of all stuff")
# for name, record in book.data.items():
#     print(record)
# print()
#
# # Знаходження та редагування телефону для John
#
# print("Trying to FIND the record for John")
# john = book.find("John")
# print(john)
#
#
# john.edit_phone("5555555555", "4444444444")
# print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555
#
# # Пошук конкретного телефону у записі John
#
# found_phone = john.find_phone("4444444444")
# print(f"{john.name}: {found_phone}")  # Виведення: 5555555555
#
# # Видалення запису Jane
#
# book.delete("Jane")
#
# print("List of all stuff")
# for name, record in book.data.items():
#     print(record)

# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# Видалення запису Jane
book.delete("Jane")
