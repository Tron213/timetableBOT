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