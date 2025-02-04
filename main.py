from random import randint
from graphic_arts.start_game_banner import run_screensaver


def attack(char_name: str, char_class: str) -> str:
    """Атака персонажа."""
    ...
    if char_class == 'warrior':
        damage: int = 5 + randint(3, 5)
    elif char_class == 'mage':
        damage: int = 5 + randint(5, 10)
    elif char_class == 'healer':
        damage: int = 5 + randint(-3, -1)
    return (f'{char_name} нанёс урон противнику равный {damage}')


def defence(char_name: str, char_class: str) -> str:
    """Защита персонажа."""
    ...
    if char_class == 'warrior':
        block: int = 10 + randint(5, 10)
    elif char_class == 'mage':
        block: int = 10 + randint(-2, 2)
    elif char_class == 'healer':
        block: int = 10 + randint(2, 5)
    return (f'{char_name} блокировал {block} урона')


def special(char_name: str, char_class: str) -> str:
    """Специальное умение персонажа."""
    ...
    if char_class == 'warrior':
        skill_name: str = 'применил специальное умение "Выносливость'
        skill_val: int = 80 + 25
    elif char_class == 'mage':
        skill_name: str = 'применил специальное умение "Атака'
        skill_val: int = 5 + 40
    elif char_class == 'healer':
        skill_name: str = 'применил специальное умение "Защита'
        skill_val: int = 10 + 30
    return (f'{char_name} {skill_name} {skill_val}"')


def start_training(char_name: str, char_class: str) -> str:
    """Тренировка персонажа."""
    ...
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    elif char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    elif char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: '
          'attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника, '
          'или special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = ''
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        elif cmd == 'defence':
            print(defence(char_name, char_class))
        elif cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    """Выбор класса персонажа."""
    ...
    approve_choice: str = ''
    char_class: str = ''
    while approve_choice != 'y':
        pr: str = ('Введи название персонажа, '
                   'за которого хочешь играть: '
                   'Воитель — warrior, '
                   'Маг — mage, '
                   'Лекарь — healer: ')
        char_class = input(pr)
        pr: str = ''
        if char_class == 'warrior':
            pr: str = ('Воитель — дерзкий воин '
                       'ближнего боя. Сильный, '
                       'выносливый и отважный.')
        elif char_class == 'mage':
            pr: str = ('Маг — находчивый воин '
                       'дальнего боя. Обладает '
                       'высоким интеллектом.')
        elif char_class == 'healer':
            pr: str = ('Лекарь — могущественный '
                       'заклинатель. Черпает силы '
                       'из природы, веры и духов.')
        print(pr)
        pr: str = ('Нажми (Y), чтобы подтвердить выбор, '
                   'или любую другую кнопку, '
                   'чтобы выбрать другого персонажа ')
        approve_choice = input(pr).lower()
    return char_class


if __name__ == '__main__':
    print(print.__doc__)
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))
