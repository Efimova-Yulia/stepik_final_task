

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    # Добавляем параметр --language для запуска из командной строки
    parser.addoption('--language', action='store', default='en',
                     help='Choose language for browser, e.g.,es, fr, ru')


@pytest.fixture(scope="function")
def browser(request):
    # Получаем значение языка из командной строки
    user_language = request.config.getoption("language")

    # Настраиваем опции для Chrome
    options = Options()
    # Устанавливаем язык через экспериментальную опцию prefs
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})

    # Запускаем браузер с указанными опциями
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)

    yield browser

    # Закрываем браузер после завершения теста
    browser.quit()
