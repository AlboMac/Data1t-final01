# Итоговая аттестация. Задание 1.
# Создание Docker-контейнера с Python-приложением
## Описание задания:
- Создайте директорию для вашего проекта, например docker_python_app, и в ней создайте файл app.py.
- В файле app.py создайте скрипт, который будет выполнять следующие задачи:
  - Вычислять количество файлов в заданном пути (по умолчанию — корневой каталог файловой системы). Задание пути производится следующим образом: в начале скрипта может определяться переменная path, содержащая путь; если же переменная не определена (закомментирована), то используется вышеупомянутое значение по умолчанию.
  - Выводить топ-10 файлов по размеру (в Кб).
  - Принимать аргумент из командной строки для вывода приветствия с указанным именем, а также текущей даты и времени.
- Теперь создайте Dockerfile в той же директории. Этот файл будет использоваться для сборки Docker-образа.
- Теперь, когда у вас есть Dockerfile и app.py, можно собрать Docker-образ.
- После того как Docker-образ собран, можно запустить контейнер с вашим приложением. 

## Сборка Docker образа
```docker build -t fsa001 .```

## Запуск контейнера с указанием имени приложения
```docker run --rm --name fsa001 fsa001 -n Aleks -p /var/log```
### Параметры запуска:
- ```параметр -n или --name``` Указание имени пользователя
- ```параметр -p или --path``` Указание пути к желаемой директории

После запуска контейнера вы должны увидеть вывод в терминале, который будет включать:

- Приветственное сообщение с указанным именем и текущим временем.
- Общее количество файлов в указанном пути.
- Топ-10 файлов по размеру в указанном пути.

## Пример вывода:
```
Привет, Aleks! Текущее время: 2025-03-30 14:35:22

Общее количество файлов в /: 4567

Топ-10 файлов по размеру (КБ):
1. /var/log/syslog — 1024.00 КБ
2. /usr/bin/python3 — 512.50 КБ
...
10. /app/app.py — 1.23 КБ
```

## Результат задания
После выполнения задания у вас будет Docker-контейнер, который при запуске:
- Выводит приветственное сообщение с именем пользователя и текущим временем.
- Вычисляет количество файлов в указанной директории.
- Выводит топ-10 файлов по размеру.

## Итоговый скриншот
![пример (1)](https://github.com/AlboMac/Data1t-final01/blob/115b1cf16fbc9962ac765574897dae0b975761e9/SCREENSHOT/Screenshot%20from%202025-03-30%2019-53-08.png)
