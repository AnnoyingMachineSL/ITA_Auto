#pytest --headed  - все тесты запускаются в headed режиме
#pytest -k test_login.py  - -k запуск по названию файла
#pytest -x -k test_login.py  -x остановка после первого падения теста
#pytest -m negative  -m запуск по названию марок
#pytest -k test_login.py -v  - тесты с выводом всех параметров
#pytest -k test_login.py -q  - запуск без логов
#pytest -k test_login.py -s  запуск с принтами
import re

#@pytest.fixture(scope='session') - параметризация в фикстуре. session - для того
#@pytest.fixture(scope='session', autouse = True) - autouse автоматическое применение фикстуры.
# у которых ничего не возвращается

b = 'a@gmail.com'
print(re.findall('@gmail.com', b))