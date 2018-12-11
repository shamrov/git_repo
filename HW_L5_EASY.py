import os
from sys import argv
from shutil import copy

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

def make_dir(dir):
    dir_path = os.path.join(os.getcwd(), dir)
    try:
        os.mkdir(dir_path)
    except:
        print(dir_path + 'Уже есть такая директория')

path_dir = [('dir_' + str(i + 1)) for i in range(9)]
for i in path_dir:
    make_dir(i)

def del_dir(dir):
    dir_path = os.path.join(os.getcwd(), dir)
    try:
        os.rmdir(dir_path)
    except:
        pass

list_dir = os.listdir()
for i in list_dir:
    del_dir(i)

# Другой вариант создания директорий(Заранее заданные директории)

def create_dir():
    list_dir = ["dir_1", "dir_2", "dir_3", "dir_4", "dir_5", "dir_6", "dir_7", "dir_8", "dir_9"]
    for i in list_dir:
        os.mkdir(i)

    
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def dirname():
    for i in os.listdir(os.getcwd()):
        print(i)

# list_dir = dirname()

# Так же можно сделать и с переменной к примеру for i in os.listdir(main)Только тогда нам нужно
# будет указать переменной main путь к директории.

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def duplicate_file():
    newfile = argv[0] + '.duplicate'
    copy(argv[0], newfile)
    if os.path.exists(newfile):
        print(newfile, "Был успешно создан")
        return True
    else:
        print("Возникли проблемы с копированием")
        return False

# duplicate_file()

# Копирование указанного файла

def duplicate_file(namefile):
    newfile = namefile + '.duplicate'
    copy(namefile, newfile)
    if os.path.exists(newfile):
        print(newfile, "Был успешно создан")
        return True
    else:
        print("Возникли проблемы с копированием")
        return False

# Копирование файлов из указанной директории

def dupl_files(dirname):
    file_list = os.listdir(dirname)
    for f in file_list:
        fullname = os.path.join(fullname, f)
        duplicate_file(fullname)

# duplicate_file('HW_L5_EASY.py')




