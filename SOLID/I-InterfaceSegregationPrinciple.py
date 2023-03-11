# ПРИНЦИП РАЗДЕЛЕНИЯ ИНТЕРФЕЙСА (ISP)
# Ни один клиент не должен зависеть от методов,
# которые он НЕ ИСПОЛЬЗУЕТ

# **Много интерфейсов, специально предназначенных для клиента лучше,
# чем 1 интерфейс общего назначения


# АНТИПАТТЕРН
class PrinterIncorrect:

    def __init__(self, document):
        self.document = document

    def print(self):
        """ ВСЕ ПРИНТЕРЫ МОГУТ ПЕЧАТАТЬ """
        print('print')

    def scan(self):
        """
        НАРУШЕНИЕ ПРИНЦИПА!
        МЕТОД ИСПОЛЬЗУЕТСЯ НЕ ВО ВСЕХ КЛАССАХ-НАСЛЕДНИКАХ,
        Т.К. НЕ ВСЕ ПРИНТЕРЫ МОГУТ СКАНИРОВАТЬ
        """
        print('scan')


class NewPrinterIncorrect(PrinterIncorrect):
    def printing(self):
        self.print()

    def scanning(self):
        self.scan()


class OldPrinterIncorrect(PrinterIncorrect):
    """ Класс зависит от метода, который не использует """
    def printing(self):
        self.print()


# ПАТТЕРН
class PrinterCorrect:

    def __init__(self, document):
        self.document = document

    def print(self):
        """ ВСЕ ПРИНТЕРЫ МОГУТ ПЕЧАТАТЬ """
        print('print')


class NewPrinterCorrect(PrinterCorrect):
    def printing(self):
        self.print()

    def scan(self):
        print('scan')


class OldPrinterCorrect(PrinterCorrect):
    """ Класс зависит только от тех методов,
    которые он использует """

    def printing(self):
        self.print()