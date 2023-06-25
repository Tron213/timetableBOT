import os
import requests
from datetime import datetime, timedelta
#http://www.fa.ru/fil/perm/student/shedule/Documents/!!! МЕНЯТЬ В РУЧНУЮ ВО ВСЕХ ССЫЛКАХ 2022-2023/rasp_stud/

def URLnext():
    current_date = datetime.now()
    next_day = current_date + timedelta(days=1)
    formatted_date = next_day.strftime("%d.%m.%Y")
    file_name=(formatted_date +"_S.pdf")
    
    current_month = datetime.now()
    next_day = current_month + timedelta(days=1)
    formatted_month = next_day.strftime("%m.%y")
    
    utl="http://www.fa.ru/fil/perm/student/shedule/Documents/2022-2023/rasp_stud/"+formatted_month+"/"+file_name
    print (utl)
    return utl


def URLtoday():
    current_date = datetime.now()
    next_day = current_date + timedelta(days=0)
    formatted_date = next_day.strftime("%d.%m.%Y")
    file_name=(formatted_date +"_S.pdf")
    
    current_month = datetime.now()
    next_day = current_month + timedelta(days=0)
    formatted_month = next_day.strftime("%m.%y")
    
    utl="http://www.fa.ru/fil/perm/student/shedule/Documents/2022-2023/rasp_stud/"+formatted_month+"/"+file_name
    print (utl)
    return utl

def fileNAME(dayz):
    current_date = datetime.now()
    next_day = current_date + timedelta(days=dayz)
    formatted_date = next_day.strftime("%d.%m.%Y")
    file_name=(formatted_date +"_S.pdf")
    return file_name



def DOWNnextday():
    url = URLnext()#год менять в ручную
    filename =fileNAME(1)
    save_path = os.path.join(os.getcwd(), filename)

    response = requests.get(url)
    if response.status_code == 200:
        content_type = response.headers.get("content-type")
        if "application/pdf" in content_type:
            with open(save_path, "wb") as file:
                file.write(response.content)
            print(f"The file '{filename}' has been downloaded successfully.")
        else:
            print("The requested file is not a PDF.")
    else:
        print("Failed to retrieve the file.")


def DOWNtoday():
    url = URLtoday()#год менять в ручную
    filename =fileNAME(0)
    save_path = os.path.join(os.getcwd(), filename)

    response = requests.get(url)
    if response.status_code == 200:
        content_type = response.headers.get("content-type")
        if "application/pdf" in content_type:
            with open(save_path, "wb") as file:
                file.write(response.content)
            print(f"The file '{filename}' has been downloaded successfully.")
        else:
            print("The requested file is not a PDF.")
    else:
        print("Failed to retrieve the file.")


