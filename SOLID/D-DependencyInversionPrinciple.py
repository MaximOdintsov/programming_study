# ПРИНЦИП ИНВЕРСИИ ЗАВИСИМОСТИ (DIP)

# Модуль высокого уровня не должен зависеть от модулей низкого уровня.
# И то, и другое должно зависеть от абстракций.

# Абстракции не должны зависеть от деталей реализации.
# Детали реализации должны зависеть от абстракций.


# АНТИПАТТЕРН 1
# (Здесь вообще все плохо)
class YandexMusicApi1:
    def __init__(self, music):
        self.music = music

    def get_music(self):
        print(f'get music {self.music} from YandexMusic')


class SpotifyMusicApi1:
    def __init__(self, music):
        self.music = music

    def find_all(self):
        print(f'get all music {self.music} from SpotifyMusic')


print("""----------------------------------------------------
АНТИПАТТЕРН 1""")
music_app = YandexMusicApi1('music')
music_app.get_music()

new_music_app = SpotifyMusicApi1('music')
new_music_app.find_all()


# АНТИПАТТЕРН 2
# Уже лучше
class MusicApi2:
    def __init__(self, music):
        self.music = music

    def get_track(self):
        print(f'Get {self.music}')


class YandexApi2(MusicApi2):
    def get_track(self):
        print(f'get track "{self.music}" from YandexMusic')
        super().get_track()


class SpotifyApi2(MusicApi2):
    def get_track(self):
        print(f'get track "{self.music}" from SpotifyMusic')
        super().get_track()


print("""----------------------------------------------------
АНТИПАТТЕРН 2""")
yandex_api = YandexApi2('Happy Nation')
spotify_api = SpotifyApi2('Selena')

for api in [yandex_api, spotify_api]:
    api.get_track()


# ПАТТЕРН
# Получается конфетка
class MusicApi3:
    def __init__(self, music):
        self.music = music

    def get_track(self):
        print(f'Get {self.music}')


class MusicClient:
    def __init__(self, music_client):
        self.music_client = music_client

    def get_track(self):
        self.music_client.get_track()


class YandexApi3(MusicApi2):
    def get_track(self):
        print(f'get track "{self.music}" from YandexMusic')
        super().get_track()


class SpotifyApi3(MusicApi2):
    def get_track(self):
        print(f'get track "{self.music}" from SpotifyMusic')
        super().get_track()


print("""----------------------------------------------------
ПАТТЕРН""")
yandex_client = YandexApi2('Happy Nation')
spotify_client = SpotifyApi2('Selena')

client = MusicClient(yandex_client)
client.get_track()
