from enum import Enum
from random import randint


class Move(Enum):
    SLEEP = 'спит'
    EAT = 'кушает'
    PLAY = 'играет'


class Cat:
    img_cat = {
        'happy_100': '/static/media/happy_100.jpeg',
        'happy_50': '/static/media/happy_50.jpeg',
        'happy_0': '/static/media/happy_0.jpeg',
        'sleep': '/static/media/sleep.jpeg'
    }

    cat = {
        'img_cat': img_cat.get('happy_100'),
        'name': None,
        'age': randint(1, 20),
        'satiety': 50,
        'happiness': 50,
        'stat': Move.SLEEP.value
    }

    @classmethod
    def get_stats(cls, select):
        if cls.cat.get('stat') != Move.SLEEP.value and select == 'eat':
            cls.cat['satiety'] = min(cls.cat['satiety'] + 15, 100)
            if cls.cat['satiety'] == 100:
                cls.cat['happiness'] = max(cls.cat['happiness'] - 30, 0)
            else:
                cls.cat['happiness'] = min(cls.cat['happiness'] + 5, 100)
            cls.cat['stat'] = Move.EAT.value
        elif cls.cat.get('stat') == Move.SLEEP.value and select == 'play':
            cls.cat['happiness'] = max(cls.cat['happiness'] - 5, 0)
            cls.cat['stat'] = Move.PLAY.value
        elif select == 'play':
            cls.cat['satiety'] = max(cls.cat['satiety'] - 10, 0)
            if randint(1, 3) == 1:
                cls.cat['happiness'] = 0
            else:
                cls.cat['happiness'] = min(cls.cat['happiness'] + 15, 100)
            cls.cat['stat'] = Move.PLAY.value
        elif select == 'sleep':
            cls.cat['stat'] = Move.SLEEP.value
        print(cls.cat['stat'], Move.SLEEP.value)
        if cls.cat['stat'] == Move.SLEEP.value:
            cls.cat['img_cat'] = cls.img_cat.get('sleep')
        else:
            if 70 < cls.cat['happiness'] <= 100:
                cls.cat['img_cat'] = cls.img_cat.get('happy_100')
            elif 30 < cls.cat['happiness'] <= 70:
                cls.cat['img_cat'] = cls.img_cat.get('happy_50')
            else:
                cls.cat['img_cat'] = cls.img_cat.get('happy_0')

