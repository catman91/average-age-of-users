# Ипортируем библиотеку для лучшего отображения списка из словарей

import pprint


# Инициализируем  4-е словаря account1, account2...

account1 = {'login': 'ivan', 'password': 'q1'}
account2 = {'login': 'petr', 'password': 'q2'}
account3 = {'login': 'olga', 'password': 'q3'}
account4 = {'login': 'anna', 'password': 'q4'}

# Инициализируем  4-е словаря user1, user2...

user1 = {'name': 'Иван', 'age': 20, 'account': account1}
user2 = {'name': 'Петр', 'age': 25, 'account': account2}
user3 = {'name': 'Ольга', 'age': 18, 'account': account3}
user4 = {'name': 'Анна', 'age': 27, 'account': account4}

# Инициализируем список user_list, состоящий из 4-х словарей user1,user2...

user_list = [user1, user2, user3, user4]

# Инициализируем пользовательский ввод ключа словаря 'name' или 'account'
#c преобразованием ключа в нижний регистр

key = input ('Введите ключ (name или account): ').lower()

# Проверяем введенный пользователем ключ на соответствие и выводим значения по ключам

try:
    print (f'значение ключа {key} для юзера 1 = {user1[key]} \n'
           f'значение ключа {key} для юзера 2 = {user2[key]} \n'
           f'значение ключа {key} для юзера 3 = {user3[key]} \n'
           f'значение ключа {key} для юзера 4 = {user4[key]}')      
except KeyError:
    print ('Введенный ключ не найден') 
    
# Инициализируем пользовательский ввод порядкового номера для юзера из списка user_list

number = input ('Введите порядковый номер: ')

# Проверяем введенный порядковый номер и выводим данные по user

try:
    print (f"Данные по юзеру № {number}: \n"
           f"Имя: {user_list[int(number)-1]['name']} \n"
           f"Возраст: {user_list[int(number)-1]['age']} \n"
           f"Логин: {user_list[int(number)-1]['account']['login']} \n"
           f"Пароль: {user_list[int(number)-1]['account']['password']}") 
except IndexError:
    print ('Пользователь с указанным номером не найден') 

# Инициализируем пользовательский ввод номера пользователя для юзера 
# чтобы переместить его в конец списка user_list

user_end = input ('Введите номер пользователя, которого нужно переместить в конец: ')

# Выводим на экран список словарей ДО изменения 

print ('Cписок до изменения:')
pprint.pprint (user_list)

# Исключаем выбранного юзера и добавляем его в конец списка

new_user = user_list.pop(int(user_end)-1)
user_list.append(new_user)

# Выводим на экран список словарей ПОСЛЕ изменения 
print ('Cписок после изменения:')
pprint.pprint (user_list)

# Считаем средний возраст пользователей

average_age = (user1['age'] + user2['age'] + user3['age'] + user4['age']) / 4

# Инициализируем сообщение со средним возрастом всех юзеров

print (f'Средний возраст всех пользователей: {average_age}')