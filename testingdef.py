import os
#--------Ветвление, для проверки наличие удовлетвор файла по дате-----------
folder_path = "PICS"  # Replace with the path to your folder

# Specify the file names to check
file_names = ["22.90.22_1.png", "22.90.22_2.png", "22.90.22_3.png"]

# КНОПКА СЕГОДНЯ
if all(os.path.isfile(os.path.join(folder_path, name)) for name in file_names):
    #Функция отправки фото из папки
    pass

else:
    #функция скачивания пдф
    #функция скринов пдф
    #Функция отправки фото из папки
    pass


# КНОПКА ЗАВТРА
if all(os.path.isfile(os.path.join(folder_path, name)) for name in file_names):
    #Функция отправки фото из папки
    pass

else:
    #функция скачивания пдф
    #функция скринов пдф
    #Функция отправки фото из папки
    pass