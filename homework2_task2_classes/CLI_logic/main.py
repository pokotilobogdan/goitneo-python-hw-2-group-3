from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value
        self.optional = False

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)
        self.optional = True


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)

    def is_valid(self) -> bool:
        if self.value.isdigit() and len(self.value) == 10:
            return True
        else:
            return False


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, new_phone):
        new_phone = Phone(new_phone)
        if new_phone.is_valid() is False:
            print(f"The phone number {new_phone} is not valid.")
            return None
        for phone in self.phones:
            if new_phone.value == phone.value:
                print(f"There is already number {new_phone} in the record. Nothing is added.")
                return None
        self.phones.append(new_phone)

    def remove_phone(self, phone_to_remove):
        for phone in self.phones:
            if phone_to_remove == phone.value:
                self.phones.remove(phone)
                return None
        print(f"There is no number {phone_to_remove} to remove.")

    def edit_phone(self, old_phone, new_phone):

        # check if there is already new_phone in the record
        # if yes - do nothing

        for phone in self.phones:
            if new_phone == phone.value:
                print(f"There is already number {new_phone} in the record. Nothing is edited.")
                return None

            self.add_phone(new_phone)           # if there is no new_phone in the contacts - add it ...
            break
        for phone in self.phones:
            if old_phone == phone.value:
                self.remove_phone(old_phone)    # ... and delete the old_phone

    def find_phone(self, phone):
        find_flag = False
        for added_phone in self.phones:     # iterating through list of added objects
            if phone == added_phone.value:    # comparing wanted number with added_object.value
                return phone
        if not find_flag:
            print(f"There is no number {phone} in this record.")


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()

    def add_record(self, new_record):
        self.data[new_record.name] = new_record

    def find(self, name):
        for contact_name, record in self.data.items():
            if contact_name.value == name:
                return record

    def delete(self, name):
        for contact_name in self.data.keys():
            if contact_name.value == name:
                self.data.pop(contact_name)
                break
