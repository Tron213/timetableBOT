import sqlite3
from sqlite3 import Error




def IDTELE(IDTG,IDG):
    connection=sqlite3.connect('students.db')
    cursor=connection.cursor()
    teleID=(IDTG)
    teleID=str(teleID)
    groupID=(IDG)
    groupID=str(groupID)
    ADDTELE="INSERT INTO USERS(tgid,numgrp) VALUES(?,?)"
    cursor.execute(ADDTELE,(teleID,groupID))
    connection.commit()
    cursor.close()
    connection.close()



def ChangeGrp(IDTG):
    connection=sqlite3.connect('students.db')
    cursor=connection.cursor()
    teleID=(IDTG)
    teleID=str(teleID)
    cursor.execute("DELETE FROM users WHERE tgid = ?", (teleID,))
    
    connection.commit()
    cursor.close()
    connection.close()


import os

def delete_files_in_folder(folder_path):

    # Перебираем все файлы в указанной папке
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        # Проверяем, является ли путь файлом
        if os.path.isfile(file_path):
            os.remove(file_path)

    print(f"Все файлы из папки {folder_path} успешно удалены.")

# Пример использования скрипта

