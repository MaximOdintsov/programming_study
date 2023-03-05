class Person:
    def __init__(self, name: str, age: int):
        self._name = name
        self.age = age

    def get_name(self):
        return self._name

    def set_name(self, name: str):
        self._name = name

    def get_age(self):
        return self.age

    def set_age(self, age: int):
        self.age = age


class Developer(Person):
    def __init__(self, language: str, exp: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.language = language
        self.exp = exp

    def get_language(self):
        return self.language

    def set_language(self, language: str):
        self.language = language

    def get_exp(self):
        return self.exp

    def set_exp(self, exp: int):
        self.exp = exp


person = Person('Alex', 18)
developer = Developer('python', 1, 'Alex', 18)

print('Person', person.get_name(), person.age)
print('Developer', developer.get_name(), developer.age, developer.language, developer.exp)

developer.set_name('Michael')
developer.set_exp(2)
print('Developer', developer.get_name(), developer.get_exp())