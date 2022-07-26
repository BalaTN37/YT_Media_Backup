import os
from DirectoryCheck import *

currentPath = os.getcwd()
Path2Backup = input("Enter the path to backup : ")
print(("***********************************"))
BackupTitle = input("Enter Title (Default-File Name) : ")
print(("***********************************"))
BackupDescription = input("Enter Desciption : ")
print(("***********************************"))
BackupKeyword = input("Enter Keywords (Separated by \",\") : ")
print(("***********************************"))
BackupPrivacyState = input("Enter Privacy State (0-Private(default), 1-Unlisted, 2-Public ): ")
print(("***********************************"))


videoPathsinDirectory = []
photoPathsinDirectory = []
IsItDirectory(Path2Backup, videoPathsinDirectory, photoPathsinDirectory)

print("Total Files Found : ")
print((int(len(videoPathsinDirectory))))
UploadCheck = int(input("Do you want to upload All Files : 1 - Yes"))

if(UploadCheck !=  1):
    sys.exit()
    
for i in range(0, len(videoPathsinDirectory)):
     #print(videoPathsinDirectory[i])
    tail = os.path.basename(videoPathsinDirectory[i])
    executionCmd = currentPath + "\\uploadVideo.py --file=\"" + videoPathsinDirectory[i] + "\" --title=\""
     
    if(int(len(videoPathsinDirectory)) == 1):
        if(BackupTitle==""):
            executionCmd = executionCmd + tail
        else:
            executionCmd = executionCmd + BackupTitle
    else:
        if(BackupTitle==""):
            executionCmd = executionCmd + tail + " " + "Part" + str(i+1)
        else:
            executionCmd = executionCmd + BackupTitle + " " + "Part" + str(i+1)
    
    executionCmd = executionCmd + "\" --description=\"" + "#YTMediaBackUp " + BackupDescription
    executionCmd = executionCmd + "\" --keywords=\"" + BackupKeyword 
    executionCmd = executionCmd + "\" --category=\"22"
    executionCmd = executionCmd + "\" --privacyStatus=\""
    
    if(BackupPrivacyState=="2"):
        executionCmd = executionCmd + "public\""
    elif(BackupPrivacyState=="1"):
        executionCmd = executionCmd + "unlisted\""
    else:
        executionCmd = executionCmd + "private\""
        
    os.system(executionCmd)
    print("\n ExecutionCommand : ")
    print(executionCmd)
    
print("Photo Path")
for i in range(0, len(photoPathsinDirectory)):
     print(photoPathsinDirectory[i])     
     
#executionCmd = currentPath + "\uploadVideo.py --file=" + Path2Backup

#D:\GIT\BackupContents_Youtube\uploadVideo.py --file="D:\Temp\17_7\Cycling_2022_07_17_17_59_23.mp4"  --title="Automation Test"   --description="Auto upload test"  --keywords="Automation Test 1" --category="22" --privacyStatus="private"
