# ПРИНЦИП ПОДСТАНОВКИ БАРБАРЫ ЛИСКОВ (LSP)
# Объекты в программе должны быть заменяемы экземплярами их подтипов
# без негативных последствий для функциональности программы

# Методы могут только дополняться, а не заменяться

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name} покушал')

    def think(self):
        print(f'{self.name} думает')

    def sleep(self):
        print(f'{self.name} спит')


class Developer(Person):
    def __init__(self, language, name, age):
        super().__init__(name, age)
        self.language = language

    def write_code(self):
        print(f'Программист {self.name} пишет код на {self.language}')


class FrontendDeveloper(Developer):
    def use_browser_dev_tools(self):
        print(f'Фронтед-разработчик {self.name} использует Dev Tools')


# АНТИПАТТЕРН
class BackendDeveloper(Developer):
    def configure_db(self):
        print(f'Бэкенд-разработчик {self.name} разрабатывает БД')

    def sleep(self):
        """
        Нарушение принципа!
        Переопределяющийся метод НЕ ДОПОЛНЯЕТСЯ, а ЗАМЕНЯЕТСЯ!
        """
        print('Программист не спит')


class MobileDeveloper(Developer):
    def developing_mobile_apps(self):
        print(f'Мобильный разработчик {self.name} разрабатывает мобильное приложение')

    def write_code(self):
        """
        Нарушения принципа НЕТ!
        МЕТОД ДОПОЛНЯЕТСЯ, а НЕ ЗАМЕНЯЕТСЯ!
        """
        print(f'Программист пишет код по 5 часов в день')
        super().write_code()


# ЕЩЕ 1 ПРИМЕР

# АНТИПАТТЕРН
class DataBaseIncorrect:
    def connect(self):
        print('connect')

    def read(self):
        print('read')

    def write(self):
        print('write')

    def join_tables(self):
        print('join tables')


class PostgreSQLIncorrect(DataBaseIncorrect):
    def connecting(self):
        self.connect()

    def join_table(self):
        self.join_tables()


class MongoDBIncorrect(DataBaseIncorrect):
    def connecting(self):
        self.connect()

    def join_tables(self):
        """
        Происходит нарушение принципа Лисков
        """
        raise print('В NoSQL нельзя использовать метод join_tables')


# ПАТТЕРН
class DataBaseCorrect:
    def connect(self):
        print('connect')

    def read(self):
        print('read')

    def write(self):
        print('write')

    # удаляем join_tables


# Специфичные для каждого типа БД методы выносим в отдельные классы,
# после чего наследуемся уже от них
class SQL(DataBaseCorrect):
    def join_tables(self):
        print('join tables')


class NoSQL(DataBaseCorrect):
    def create_index(self):
        print('create index')


class PostgreSQL(SQL):
    def join_table(self):
        self.join_tables()


class MongoDB(NoSQL):
    def creating_index(self):
        self.create_index()
