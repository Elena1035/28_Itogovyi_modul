class TestData:
    """Класс содержащий все данные для проверок авторизации."""
    incorrect_email = {
        'l.serg@ya.ru': 'unregistered email',
        'l.serg@ya.r': 'invalid email',
        'log@gmail.ru': 'invalid email',
        'log@gmail.ru': 'invalid email',
        'example@': 'invalid email',
        'example@company': 'invalid email',
        "x" * 1: '1 symbol',
        "x" * 10: '10 symbols',
        "x" * 11: '11 symbols',
        "x" * 255: '255 symbols',
        "x" * 256: '256 symbols',
        'абвгдеёжзийклмнопрстуфхцчшщъыьэюя': 'russian',
        '的一是不了人我在有他这为之大来以个中上们': 'chinese',
        '|!@#$%^&*()-_=+`~?"№;:[]{}': 'specials',
        '12345678': 'digit'
    }

    incorrect_phone = {
        '9134225289': 'unregistered phone',
        '0000000000': 'invalid phone',
        "1" * 10: '10 symbols',
        "1" * 11: '11 symbols',
        "1" * 255: '255 symbols',
        "1" * 256: '256 symbols',
        'абвгдеёжзийклмнопрстуфхцчшщъыьэюя': 'russian',
        '的一是不了人我在有他这为之大来以个中上们': 'chinese',
        '|!@#$%^&*()-_=+`~?"№;:[]{}': 'specials'
    }

    incorrect_login = {
        'Lena23': 'unregistered login',
        'asd23eqw.': 'invalid login',
        'user_name!': 'invalid login',
        "x" * 1: '1 symbol',
        "x" * 5: '5 symbols',
        "x" * 6: '6 symbols',
        "x" * 255: '255 symbols',
        "x" * 256: '256 symbols',
        'абвгдеёжзийклмнопрстуфхцчшщъыьэюя': 'russian',
        '的一是不了人我在有他这为之大来以个中上们': 'chinese',
        '|!@#$%^&*()-_=+`~?"№;:[]{}': 'specials',
        '12345678': 'digit'
    }

    incorrect_ls = {
        '315161013851': 'unregistered ls',
        '000000000000': 'invalid ls',
        "1" * 12: '12 symbol',
        "1" * 13: '13 symbols',
        "1" * 255: '255 symbols',
        "1" * 256: '256 symbols'
    }

    incorrect_password = {
        'Zxcvb123454': 'unregistered password',
        "x" * 1: '1 symbol',
        "x" * 7: '7 symbols',
        "x" * 8: '8 symbols',
        "x" * 255: '255 symbols',
        "x" * 256: '256 symbols',
        'абвгдеёжзийклмнопрстуфхцчшщъыьэюя': 'russian',
        '的一是不了人我在有他这为之大来以个中上们': 'chinese',
        '|!@#$%^&*()-_=+`~?"№;:[]{}': 'specials',
        '12345678': 'digit'
    }

    VALID_EMAIL = "nzlskmx149@mastro.club"
    VALID_PHONE = "9151126929"
    VALID_PASSWORD = "Marlen2000"
