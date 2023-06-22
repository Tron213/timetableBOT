import os
import requests
from datetime import datetime, timedelta


def NextDay():
    current_date = datetime.now()
    next_day = current_date + timedelta(days=1)
    formatted_date = next_day.strftime("%d.%m.%Y")
    file_name=(formatted_date +"_S.pdf")
    return file_name
def month():
    current_date = datetime.now()
    next_day = current_date + timedelta(days=1)
    formatted_date = next_day.strftime("%m.%y")
    
    return formatted_date

url = "http://www.fa.ru/fil/perm/student/shedule/Documents/2022-2023/rasp_stud/"+month()+"/"+ NextDay() #год менять в ручную
filename = NextDay() 
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
#сон


