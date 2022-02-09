import datetime

log_file = open("log.txt","a")

def logTime():
    log_file.write(" \n")
    x = str(datetime.datetime.now())
    log_file.write(x+" \n")
    

def endLog():
    x = str(datetime.datetime.now())
    log_file.write(x+" \n")
   




def Print__(text):
    log_file.write(text+" \n")
    print(text)

    