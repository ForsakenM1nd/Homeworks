class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value) -> None:
        super().__init__(value)

    def __str__(self) -> str:
        return self.value


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone: Phone) -> None:
        # if phone.value in [p.value for p in self.phones]:
        #     return f"{phone} in PhoneList"
        self.phones.append(phone)
        # return f"{phone} add to PhoneList"

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"



john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")
print(john_record)

jane_record = Record("Jane")
jane_record.add_phone("9876543210")
print(jane_record)