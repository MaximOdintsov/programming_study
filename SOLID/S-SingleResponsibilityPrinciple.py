# ПРИНЦИП ЕДИНСТВЕННОЙ ОТВЕТСТВЕННОСТИ (SRP)

# У каждого класса должна быть только одна ответственность
# и он не должен брать на себя другие обязанности.

# У класса должна быть одна и только одна причина для изменения


# АНТИПАТТЕРН GodObject
class TelephoneDirectoryGodObject:
    def __init__(self):
        self.telephone_directory = {}

    def add_contact(self, phone, name):
        self.telephone_directory[phone] = name

    def delete_contact(self, phone):
        self.telephone_directory.pop(phone)

    def change_contact(self, phone, name):
        self.telephone_directory[phone] = name

    def get_contact(self, phone):
        return self.telephone_directory.get(phone)

    def filter_db(self, phone, name, db_config):
        database = db_config
        if phone and name:
            database.filter(phone=phone, name=name)
        elif phone:
            database.filter(phone=phone)
        if name:
            database.filter(name=name)

    def save_to_database(self, phone, name, db_config):
        """ НАРУШЕНИЕ ПРИНЦИПА ЕДИНОЙ ОТВЕТСТВЕННОСТИ """
        database = db_config
        self.telephone_directory[phone] = name
        database.save()

    def filter_file(self, phone, name, file):
        file = file
        if phone and name:
            file.filter(phone=phone, name=name)
        elif phone:
            file.filter(phone=phone)
        if name:
            file.filter(name=name)

    def save_to_file(self, phone, name, file):
        """ НАРУШЕНИЕ ПРИНЦИПА ЕДИНОЙ ОТВЕТСТВЕННОСТИ """
        file = file
        self.telephone_directory[phone] = name
        file.write()


# ПАТТЕРН
class TelephoneDirectorySingleResponsibilityPrinciple:
    def __init__(self):
        self.telephone_directory = {}

    def add_contact(self, phone, name):
        self.telephone_directory[phone] = name

    def delete_contact(self, phone):
        self.telephone_directory.pop(phone)

    def change_contact(self, phone, name):
        self.telephone_directory[phone] = name

    def get_contact(self, phone):
        return self.telephone_directory.get(phone)


class DataBase:

    def __init__(self, phone, name, db_config):
        self.database = db_config
        self.phone = phone
        self.name = name

    def get(self):
        self.database.get(phone=self.phone, name=self.name)

    def filter(self):
        if self.phone and self.name:
            self.database.filter(phone=self.phone, name=self.name)
        elif self.phone:
            self.database.filter(phone=self.phone)
        if self.name:
            self.database.filter(name=self.name)

    def save(self):
        self.database.phone = self.phone
        self.database.name = self.name
        self.database.save()


class File:
    def __init__(self, phone, name, file):
        self.file = file
        self.phone = phone
        self.name = name

    def get(self):
        self.file.get(phone=self.phone, name=self.name)

    def filter(self):
        if self.phone and self.name:
            self.file.filter(phone=self.phone, name=self.name)
        elif self.phone:
            self.file.filter(phone=self.phone)
        if self.name:
            self.file.filter(name=self.name)

    def save(self):
        self.file.phone = self.phone
        self.file.name = self.name
        self.file.save()