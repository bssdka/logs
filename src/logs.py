
import os
import datetime

"""
Привет! Ознакамливаетесь с кодом данного скрипта? Я расскажу вам о нём. Это простая библиотека python для логирования вашего кода. 
Её можно полностью настроить под себя, чтобы у вас не было проблем с чтением ошибок. 
Вся нужная информация по настройке скрипта приложена в файле README.md. 

--------------------------------------------------------------------------------------------------------------------------

Hi! Are you familiar with the code of this script? I'll tell you about it. It is a simple python library for logging your code. 
It can be fully customized so that you don't have problems with reading errors. 
All the necessary information on customizing the script is attached in the README.md file. 
"""

# clear file LOGS.txt
with open('LOGS.txt', 'w'):
    pass

file = open('LOGS.txt', 'a+')
        
def logger(status, description) -> str:
    date = datetime.datetime.now()
    FORMAT = f'{str(date)} \n : {status} \n : {description} \n'
        
    file.write(FORMAT)