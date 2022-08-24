"""Задача 1. 50 баллов
Написать функцию которая будет добавлять код страны
к номеру телефона с помощью замыкания
внешний вид вызова функции."""

def number_country():
    user_telephone = '+044'
    def phone():
        my_number = '838372893'
        result = user_telephone + my_number
        print(result)
        return number_country

    return phone
f = number_country()
print(f())


