# -*- coding: utf-8 -*-
# Практическое задание

# • Администратор задает seed для модуля рандом через
# переменную окружения FLASK_RANDOM_SEED

# • Flask при старте сервера - устанавливает seed для
# random, генерирует случайное число для угадывания

# • Пользователь по GET запросу на адрес / получает
# сообщение: "Число загадано"

# • Пользователь по POST запросе на адрес /guess
# получает один из следующих результатов: ">", "<", "="

# • Если число угадано - загадываем новое число