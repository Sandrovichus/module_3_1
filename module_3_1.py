calls = 0


def count_calls():  # подсчет вызова функций
    global calls
    calls = calls + 1


def string_info(string):  # возврат кортежа с длиной текста, текстом в верхнем и нижнем регисте
    count_calls()
    return len(string), string.upper(), string.lower()


def is_contains(string, list_to_search):  # возврат признака наличия текста в списке, игнорируя регистр
    string_lower = string.lower()
    list_to_search_lower = [s.lower() for s in list_to_search]
    count_calls()
    return string_lower in list_to_search_lower


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(string_info('Samara'))
print(is_contains('Samara', ['Moscow', 'SaMAra']))
print(string_info('Moscow'))
print(calls)
