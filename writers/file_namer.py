from translate import Translator


def python_name():
    translator = Translator(to_lang='en', from_lang='ru')

    text = f'{input("Введите номер: ")} {input("Введите название: ")}'
    text = translator.translate(text)
    text = text.replace(',', '')
    text = text.split()

    text = '_'.join(text) + '.py'
    return text.lower()


print(python_name())