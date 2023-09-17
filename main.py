from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Неправильний формат номеру телефона")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        phone_obj = Phone(phone)
        self.phones.append(phone_obj)

    def remove_phone(self, phone):
        self.phones = [p for p in self.phones if str(p) != phone]

    def edit_phone(self, old_phone, new_phone):
        if old_phone in self.phones:
            self.remove_phone(old_phone)
            self.add_phone(new_phone)
        else:
            raise ValueError("Номер телефону не знайдено")

    def find_phone(self, phone):
        phone = Phone(phone)
        for phone_obj in self.phones:
            if phone_obj == phone:
                return str(phone_obj)
        return None

    def __str__(self):
        phone_str = "; ".join(str(p) for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phone_str}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]


# if __name__ == '__main__':
#     main()


