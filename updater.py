import sys
import os
import zipfile
import datetime
import time

if __name__ == "__main__":
    PathToMain = str(r'C:\web') #path to updated folder
    PathToUpdate = str(r'C:\web_update.rar') #default path to update
    PathToLogs = str(r'app_data\log')
    LogFile = 'server.log'
    PathToTempUnrar = str(r'C:\temprar12\\')
    AmountOfZipLogFiles = 5
    if len (sys.argv) > 1: #custom path to update
        PathToUpdate = sys.argv[1]


    newzip = zipfile.ZipFile(PathToMain+'\\' +PathToLogs+'\\'+str(datetime.datetime.today().strftime("%Y-%m-%d-%H.%M.%S"))+'.zip', 'w')  # create zip
    if os.path.exists(PathToMain+'\\' +PathToLogs+'\\'+LogFile):
        newzip.write(PathToMain+'\\' +PathToLogs+'\\'+LogFile, LogFile)
        os.remove(PathToMain + '\\' + PathToLogs + '\\' + LogFile)  # delete source log
    newzip.close()  # close zip



    #refresh archive logs
    listofzip = os.listdir(PathToMain+'\\' +PathToLogs)
    listofzip = list(filter(lambda x: x.endswith('.zip'), listofzip))
    for i in range(len(listofzip)-AmountOfZipLogFiles):
        os.remove(PathToMain+'\\' +PathToLogs+'\\'+listofzip[i])
    print(listofzip)

    os.system(str(r'set path="C:\Program Files\WinRAR\\";%path%'))
    os.rename(PathToMain,PathToMain+'1')
    os.system('unrar '+'x ' + PathToUpdate+' '+PathToMain+'\\')
    os.system('rmdir /S /Q '+ PathToMain+'\\cfg')
    os.mkdir(PathToMain+'\\cfg')
    os.system('copy '+PathToMain+'1\\cfg\\* '+ PathToMain+'\\cfg\\')
    os.system('rmdir /S /Q ' + PathToMain+'\\app_data\\log')
    os.mkdir(PathToMain+'\\app_data\\log')
    os.system('copy ' + PathToMain +'1\\app_data\\log\\* ' + PathToMain + '\\app_data\\log\\')
    #delete temp dir
    os.system('rmdir /S /Q ' + PathToMain+'1')