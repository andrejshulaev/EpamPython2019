"""Напишите реализацию функции atom, которая инкапсулирует некую переменную,
предоставляя интерфейс для получения и изменения ее значения,
таким образом, что это значение нельзя было бы получить или изменить
иными способами.
Пусть функция atom принимает один аргумент, инициализирующий хранимое значение
(значение по умолчанию, в случае вызова atom без аргумента - None),
а возвращает 3 функции - get_value, set_value, process_value, delete_value,такие, что:

get_value - позволяет получить значение хранимой переменной;
set_value - позволяет установить новое значение хранимой переменной,
	возвращает его;
process_value - принимает в качестве аргументов сколько угодно функций
	и последовательно (в порядке перечисления аргументов) применяет эти функции
	к хранимой переменной, обновляя ее значение (перезаписывая получившийся
	результат) и возвращая получишееся итоговое значение.
delete_value - удаляет значение
"""

get_x, set_x, process_x, delete_x = atom('Hello python')
assert get_x() == 'Hello python'
assert process_x() == 'Hello python'
assert process_x(lambda x: x[::-1], ) == 'nohtyp olleH'
assert set_x(10) == 10
delete_x()
assert not get_x()